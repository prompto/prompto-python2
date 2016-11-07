# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .OParserListener import OParserListener
else:
    from OParserListener import OParserListener
from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\u00ab\u08c7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u01a4\n\2\3\2\3\2\5")
        buf.write(u"\2\u01a8\n\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\6\5\6\u01c3\n\6\3\6\3\6\3\6\3\6\3\6\5\6\u01ca")
        buf.write(u"\n\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u01d2\n\6\5\6\u01d4")
        buf.write(u"\n\6\3\6\3\6\3\7\5\7\u01d9\n\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write(u"\7\5\7\u01e1\n\7\3\7\3\7\5\7\u01e5\n\7\3\7\3\7\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\5\b\u01ef\n\b\3\b\3\b\3\t\3\t\3\t")
        buf.write(u"\3\t\3\t\3\t\7\t\u01f9\n\t\f\t\16\t\u01fc\13\t\3\n\3")
        buf.write(u"\n\3\n\5\n\u0201\n\n\3\n\5\n\u0204\n\n\3\13\5\13\u0207")
        buf.write(u"\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u0210\n")
        buf.write(u"\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u0218\n\f\3\f\3\f\3")
        buf.write(u"\r\5\r\u021d\n\r\3\r\3\r\3\r\3\r\5\r\u0223\n\r\3\r\3")
        buf.write(u"\r\3\16\3\16\3\16\3\16\5\16\u022b\n\16\3\16\3\16\3\17")
        buf.write(u"\5\17\u0230\n\17\3\17\3\17\3\17\3\17\5\17\u0236\n\17")
        buf.write(u"\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0241")
        buf.write(u"\n\20\3\20\3\20\3\20\5\20\u0246\n\20\3\20\3\20\3\21\5")
        buf.write(u"\21\u024b\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write(u"\u0254\n\21\3\21\3\21\3\21\5\21\u0259\n\21\3\21\3\21")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write(u"\23\3\23\3\23\3\23\7\23\u026b\n\23\f\23\16\23\u026e\13")
        buf.write(u"\23\3\24\3\24\5\24\u0272\n\24\3\24\3\24\3\24\3\24\5\24")
        buf.write(u"\u0278\n\24\3\24\3\24\3\24\3\25\5\25\u027e\n\25\3\25")
        buf.write(u"\3\25\3\25\3\25\5\25\u0284\n\25\3\25\3\25\3\25\5\25\u0289")
        buf.write(u"\n\25\3\25\3\25\3\26\5\26\u028e\n\26\3\26\5\26\u0291")
        buf.write(u"\n\26\3\26\3\26\3\26\3\26\5\26\u0297\n\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u02ae\n")
        buf.write(u"\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u02b8")
        buf.write(u"\n\31\3\31\3\31\3\31\5\31\u02bd\n\31\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\5\32\u02c4\n\32\5\32\u02c6\n\32\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u02dd\n")
        buf.write(u"\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write(u"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u02fb\n\35")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3")
        buf.write(u"\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u0312\n \5 \u0314")
        buf.write(u"\n \3 \3 \3!\3!\3!\3!\5!\u031c\n!\3!\3!\3!\3!\3!\5!\u0323")
        buf.write(u"\n!\5!\u0325\n!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u032d\n\"")
        buf.write(u"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\5#\u0337\n#\3#\3#\3#\3")
        buf.write(u"#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\5%\u034c")
        buf.write(u"\n%\3%\3%\5%\u0350\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write(u"&\3&\3&\3&\3&\3&\7&\u0362\n&\f&\16&\u0365\13&\3\'\3\'")
        buf.write(u"\3\'\3\'\3(\3(\3(\3(\3(\3(\5(\u0371\n(\3(\3(\5(\u0375")
        buf.write(u"\n(\3(\3(\3(\3(\3(\3(\5(\u037d\n(\3(\5(\u0380\n(\3(\3")
        buf.write(u"(\3(\5(\u0385\n(\3(\5(\u0388\n(\3)\3)\3)\3)\3)\3)\5)")
        buf.write(u"\u0390\n)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u039b\n)\3)\3")
        buf.write(u")\5)\u039f\n)\3*\3*\3*\3+\3+\5+\u03a6\n+\3+\3+\3,\3,")
        buf.write(u"\3,\5,\u03ad\n,\3,\3,\3-\3-\3-\3-\3-\5-\u03b6\n-\3.\3")
        buf.write(u".\3.\3.\3.\7.\u03bd\n.\f.\16.\u03c0\13.\3/\3/\3/\3/\3")
        buf.write(u"/\3/\5/\u03c8\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\5\60\u03e1\n\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\7")
        buf.write(u"\60\u044e\n\60\f\60\16\60\u0451\13\60\3\61\3\61\3\61")
        buf.write(u"\3\61\3\62\3\62\3\63\3\63\3\63\3\63\3\63\7\63\u045e\n")
        buf.write(u"\63\f\63\16\63\u0461\13\63\3\64\3\64\3\64\3\64\3\64\3")
        buf.write(u"\64\3\64\3\64\5\64\u046b\n\64\3\65\3\65\3\65\3\65\3\65")
        buf.write(u"\3\66\3\66\3\66\5\66\u0475\n\66\3\66\3\66\3\67\3\67\3")
        buf.write(u"\67\3\67\38\38\38\38\38\38\38\38\39\39\39\39\39\39\3")
        buf.write(u"9\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\5:\u0498\n:\3:")
        buf.write(u"\3:\3:\3:\3:\3:\3:\3:\3:\5:\u04a3\n:\3:\3:\3:\5:\u04a8")
        buf.write(u"\n:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u04b2\n:\3:\3:\3:\3:\3")
        buf.write(u":\5:\u04b9\n:\3:\3:\3:\3:\3:\3:\5:\u04c1\n:\5:\u04c3")
        buf.write(u"\n:\3;\3;\5;\u04c7\n;\3;\3;\3;\3;\3;\3;\3;\5;\u04d0\n")
        buf.write(u";\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u04de\n<\3=")
        buf.write(u"\3=\3=\5=\u04e3\n=\3=\3=\3>\3>\3>\3>\3>\5>\u04ec\n>\3")
        buf.write(u">\3>\3>\7>\u04f1\n>\f>\16>\u04f4\13>\3?\3?\3?\3?\3@\3")
        buf.write(u"@\3@\3@\3@\3A\3A\3A\3A\3A\3A\5A\u0505\nA\3B\3B\3B\3B")
        buf.write(u"\3B\3C\3C\3D\5D\u050f\nD\3D\3D\3D\3E\3E\3E\3E\7E\u0518")
        buf.write(u"\nE\fE\16E\u051b\13E\3F\3F\3F\7F\u0520\nF\fF\16F\u0523")
        buf.write(u"\13F\3F\3F\3F\3F\3F\5F\u052a\nF\3G\3G\3H\3H\5H\u0530")
        buf.write(u"\nH\3I\3I\3I\3I\7I\u0536\nI\fI\16I\u0539\13I\3J\3J\3")
        buf.write(u"J\3J\7J\u053f\nJ\fJ\16J\u0542\13J\3K\3K\3K\7K\u0547\n")
        buf.write(u"K\fK\16K\u054a\13K\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u0556")
        buf.write(u"\nL\3M\5M\u0559\nM\3M\3M\5M\u055d\nM\3M\3M\3N\5N\u0562")
        buf.write(u"\nN\3N\3N\5N\u0566\nN\3N\3N\3O\3O\3O\7O\u056d\nO\fO\16")
        buf.write(u"O\u0570\13O\3P\3P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3")
        buf.write(u"Q\3Q\3Q\3Q\3Q\5Q\u0584\nQ\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\7Q")
        buf.write(u"\u058e\nQ\fQ\16Q\u0591\13Q\3R\3R\5R\u0595\nR\3S\3S\3")
        buf.write(u"S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\5S\u05a5\nS\3T\3T")
        buf.write(u"\3U\5U\u05aa\nU\3U\3U\3V\3V\3W\3W\3W\5W\u05b3\nW\3X\3")
        buf.write(u"X\3X\7X\u05b8\nX\fX\16X\u05bb\13X\3Y\3Y\5Y\u05bf\nY\3")
        buf.write(u"Z\3Z\3Z\5Z\u05c4\nZ\3[\3[\3\\\3\\\3]\3]\3^\3^\3_\3_\3")
        buf.write(u"_\7_\u05d1\n_\f_\16_\u05d4\13_\3`\3`\5`\u05d8\n`\3`\5")
        buf.write(u"`\u05db\n`\3a\3a\5a\u05df\na\3b\3b\3b\5b\u05e4\nb\3c")
        buf.write(u"\3c\3c\3d\3d\5d\u05eb\nd\3e\3e\3e\3e\3e\3e\3e\3e\3e\7")
        buf.write(u"e\u05f6\ne\fe\16e\u05f9\13e\3f\3f\3f\3f\7f\u05ff\nf\f")
        buf.write(u"f\16f\u0602\13f\3g\3g\3g\3g\3g\5g\u0609\ng\3h\3h\3h\3")
        buf.write(u"h\7h\u060f\nh\fh\16h\u0612\13h\3i\3i\3i\5i\u0617\ni\3")
        buf.write(u"j\3j\3j\3j\3j\3j\3j\3j\3j\3j\5j\u0623\nj\3k\3k\5k\u0627")
        buf.write(u"\nk\3l\3l\3l\3l\3l\3l\7l\u062f\nl\fl\16l\u0632\13l\3")
        buf.write(u"m\3m\5m\u0636\nm\3n\3n\3n\3n\5n\u063c\nn\3n\3n\3n\7n")
        buf.write(u"\u0641\nn\fn\16n\u0644\13n\3n\3n\5n\u0648\nn\3o\3o\3")
        buf.write(u"o\7o\u064d\no\fo\16o\u0650\13o\3p\3p\3p\7p\u0655\np\f")
        buf.write(u"p\16p\u0658\13p\3q\3q\3q\3q\5q\u065e\nq\3r\3r\3s\3s\3")
        buf.write(u"s\3s\7s\u0666\ns\fs\16s\u0669\13s\3t\3t\3t\3t\3t\3t\3")
        buf.write(u"t\3t\3t\3t\5t\u0675\nt\3u\3u\5u\u0679\nu\3u\5u\u067c")
        buf.write(u"\nu\3v\3v\5v\u0680\nv\3v\5v\u0683\nv\3w\3w\3w\3w\7w\u0689")
        buf.write(u"\nw\fw\16w\u068c\13w\3x\3x\3x\3x\7x\u0692\nx\fx\16x\u0695")
        buf.write(u"\13x\3y\3y\3y\3y\7y\u069b\ny\fy\16y\u069e\13y\3z\3z\3")
        buf.write(u"z\3z\7z\u06a4\nz\fz\16z\u06a7\13z\3{\3{\3{\3{\3{\3{\3")
        buf.write(u"{\3{\3{\3{\3{\3{\3{\3{\5{\u06b7\n{\3|\3|\3|\3|\3|\3|")
        buf.write(u"\3|\3|\3|\3|\3|\3|\3|\3|\5|\u06c7\n|\3}\3}\3}\7}\u06cc")
        buf.write(u"\n}\f}\16}\u06cf\13}\3~\3~\3~\3~\5~\u06d5\n~\3\177\3")
        buf.write(u"\177\3\u0080\3\u0080\3\u0080\3\u0080\3\u0081\3\u0081")
        buf.write(u"\5\u0081\u06df\n\u0081\3\u0082\3\u0082\3\u0082\3\u0082")
        buf.write(u"\3\u0082\5\u0082\u06e6\n\u0082\3\u0083\5\u0083\u06e9")
        buf.write(u"\n\u0083\3\u0083\3\u0083\5\u0083\u06ed\n\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0084\5\u0084\u06f2\n\u0084\3\u0084\3\u0084")
        buf.write(u"\5\u0084\u06f6\n\u0084\3\u0084\3\u0084\3\u0085\3\u0085")
        buf.write(u"\3\u0085\3\u0085\3\u0085\7\u0085\u06ff\n\u0085\f\u0085")
        buf.write(u"\16\u0085\u0702\13\u0085\5\u0085\u0704\n\u0085\3\u0086")
        buf.write(u"\3\u0086\3\u0086\7\u0086\u0709\n\u0086\f\u0086\16\u0086")
        buf.write(u"\u070c\13\u0086\3\u0087\3\u0087\3\u0087\3\u0087\3\u0088")
        buf.write(u"\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088")
        buf.write(u"\3\u0088\5\u0088\u071b\n\u0088\3\u0089\3\u0089\3\u0089")
        buf.write(u"\3\u0089\3\u008a\3\u008a\3\u008a\3\u008a\3\u008a\7\u008a")
        buf.write(u"\u0726\n\u008a\f\u008a\16\u008a\u0729\13\u008a\3\u008b")
        buf.write(u"\3\u008b\3\u008b\3\u008b\5\u008b\u072f\n\u008b\3\u008c")
        buf.write(u"\3\u008c\3\u008c\7\u008c\u0734\n\u008c\f\u008c\16\u008c")
        buf.write(u"\u0737\13\u008c\3\u008d\3\u008d\3\u008d\7\u008d\u073c")
        buf.write(u"\n\u008d\f\u008d\16\u008d\u073f\13\u008d\3\u008d\5\u008d")
        buf.write(u"\u0742\n\u008d\3\u008e\3\u008e\3\u008e\3\u008e\3\u008e")
        buf.write(u"\3\u008e\5\u008e\u074a\n\u008e\3\u008f\3\u008f\3\u008f")
        buf.write(u"\3\u0090\3\u0090\3\u0090\3\u0091\3\u0091\3\u0091\3\u0092")
        buf.write(u"\3\u0092\3\u0092\3\u0093\3\u0093\3\u0093\3\u0094\3\u0094")
        buf.write(u"\3\u0095\3\u0095\3\u0096\3\u0096\3\u0097\3\u0097\3\u0098")
        buf.write(u"\3\u0098\3\u0099\3\u0099\3\u009a\3\u009a\3\u009b\3\u009b")
        buf.write(u"\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\5\u009b\u0770")
        buf.write(u"\n\u009b\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\7\u009c")
        buf.write(u"\u0777\n\u009c\f\u009c\16\u009c\u077a\13\u009c\3\u009d")
        buf.write(u"\3\u009d\3\u009d\3\u009d\3\u009d\3\u009d\3\u009d\5\u009d")
        buf.write(u"\u0783\n\u009d\3\u009e\3\u009e\3\u009f\3\u009f\3\u009f")
        buf.write(u"\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a0\5\u00a0\u078f")
        buf.write(u"\n\u00a0\3\u00a1\3\u00a1\3\u00a1\5\u00a1\u0794\n\u00a1")
        buf.write(u"\3\u00a1\3\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2\3\u00a2")
        buf.write(u"\3\u00a2\7\u00a2\u079e\n\u00a2\f\u00a2\16\u00a2\u07a1")
        buf.write(u"\13\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a4\3\u00a4")
        buf.write(u"\3\u00a4\3\u00a4\3\u00a5\3\u00a5\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a6\3\u00a6\5\u00a6\u07b2\n\u00a6\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a8\3\u00a8\3\u00a8\5\u00a8\u07b9\n\u00a8\3\u00a9")
        buf.write(u"\3\u00a9\3\u00a9\3\u00a9\3\u00a9\7\u00a9\u07c0\n\u00a9")
        buf.write(u"\f\u00a9\16\u00a9\u07c3\13\u00a9\3\u00aa\3\u00aa\3\u00aa")
        buf.write(u"\3\u00aa\5\u00aa\u07c9\n\u00aa\3\u00ab\3\u00ab\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\3\u00ab\5\u00ab\u07d1\n\u00ab\3\u00ac")
        buf.write(u"\3\u00ac\3\u00ac\5\u00ac\u07d6\n\u00ac\3\u00ac\3\u00ac")
        buf.write(u"\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\5\u00ad")
        buf.write(u"\u07e0\n\u00ad\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\3\u00ae\7\u00ae\u07e8\n\u00ae\f\u00ae\16\u00ae\u07eb")
        buf.write(u"\13\u00ae\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af")
        buf.write(u"\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af\7\u00af\u07f8")
        buf.write(u"\n\u00af\f\u00af\16\u00af\u07fb\13\u00af\3\u00b0\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1\5\u00b1\u0804")
        buf.write(u"\n\u00b1\3\u00b1\3\u00b1\3\u00b1\7\u00b1\u0809\n\u00b1")
        buf.write(u"\f\u00b1\16\u00b1\u080c\13\u00b1\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\3\u00b2\5\u00b2\u0813\n\u00b2\3\u00b3\3\u00b3")
        buf.write(u"\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4")
        buf.write(u"\5\u00b4\u081e\n\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\7\u00b5\u0825\n\u00b5\f\u00b5\16\u00b5\u0828")
        buf.write(u"\13\u00b5\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6\5\u00b6")
        buf.write(u"\u082f\n\u00b6\3\u00b7\3\u00b7\3\u00b8\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b9\3\u00b9\3\u00b9\5\u00b9\u0839\n\u00b9\3\u00ba")
        buf.write(u"\3\u00ba\3\u00ba\5\u00ba\u083e\n\u00ba\3\u00ba\3\u00ba")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bb\7\u00bb")
        buf.write(u"\u0848\n\u00bb\f\u00bb\16\u00bb\u084b\13\u00bb\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bc\3\u00bc\3\u00bd\3\u00bd\3\u00bd\3\u00bd")
        buf.write(u"\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\7\u00be")
        buf.write(u"\u085b\n\u00be\f\u00be\16\u00be\u085e\13\u00be\3\u00bf")
        buf.write(u"\3\u00bf\3\u00bf\3\u00bf\3\u00bf\7\u00bf\u0865\n\u00bf")
        buf.write(u"\f\u00bf\16\u00bf\u0868\13\u00bf\3\u00c0\3\u00c0\3\u00c0")
        buf.write(u"\3\u00c0\3\u00c0\5\u00c0\u086f\n\u00c0\3\u00c1\3\u00c1")
        buf.write(u"\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write(u"\5\u00c2\u087a\n\u00c2\3\u00c3\3\u00c3\3\u00c3\3\u00c3")
        buf.write(u"\3\u00c3\7\u00c3\u0881\n\u00c3\f\u00c3\16\u00c3\u0884")
        buf.write(u"\13\u00c3\3\u00c4\3\u00c4\3\u00c4\3\u00c4\3\u00c4\5\u00c4")
        buf.write(u"\u088b\n\u00c4\3\u00c5\3\u00c5\3\u00c6\3\u00c6\3\u00c6")
        buf.write(u"\3\u00c7\3\u00c7\3\u00c7\5\u00c7\u0895\n\u00c7\3\u00c8")
        buf.write(u"\3\u00c8\3\u00c8\5\u00c8\u089a\n\u00c8\3\u00c8\3\u00c8")
        buf.write(u"\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\7\u00c9")
        buf.write(u"\u08a4\n\u00c9\f\u00c9\16\u00c9\u08a7\13\u00c9\3\u00ca")
        buf.write(u"\3\u00ca\3\u00ca\3\u00ca\3\u00cb\3\u00cb\3\u00cb\3\u00cb")
        buf.write(u"\3\u00cc\3\u00cc\3\u00cc\5\u00cc\u08b4\n\u00cc\3\u00cc")
        buf.write(u"\3\u00cc\3\u00cc\7\u00cc\u08b9\n\u00cc\f\u00cc\16\u00cc")
        buf.write(u"\u08bc\13\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd")
        buf.write(u"\5\u00cd\u08c3\n\u00cd\3\u00ce\3\u00ce\3\u00ce\2\31\20")
        buf.write(u"$JZ^dz\u00a0\u00c8\u0112\u0136\u0142\u0150\u015a\u015c")
        buf.write(u"\u0160\u0168\u0174\u017a\u017c\u0184\u0190\u0196\u00cf")
        buf.write(u"\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write(u"\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write(u"\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094")
        buf.write(u"\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6")
        buf.write(u"\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8")
        buf.write(u"\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca")
        buf.write(u"\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da\u00dc")
        buf.write(u"\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee")
        buf.write(u"\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe\u0100")
        buf.write(u"\u0102\u0104\u0106\u0108\u010a\u010c\u010e\u0110\u0112")
        buf.write(u"\u0114\u0116\u0118\u011a\u011c\u011e\u0120\u0122\u0124")
        buf.write(u"\u0126\u0128\u012a\u012c\u012e\u0130\u0132\u0134\u0136")
        buf.write(u"\u0138\u013a\u013c\u013e\u0140\u0142\u0144\u0146\u0148")
        buf.write(u"\u014a\u014c\u014e\u0150\u0152\u0154\u0156\u0158\u015a")
        buf.write(u"\u015c\u015e\u0160\u0162\u0164\u0166\u0168\u016a\u016c")
        buf.write(u"\u016e\u0170\u0172\u0174\u0176\u0178\u017a\u017c\u017e")
        buf.write(u"\u0180\u0182\u0184\u0186\u0188\u018a\u018c\u018e\u0190")
        buf.write(u"\u0192\u0194\u0196\u0198\u019a\2\13\3\2\36\37\4\2\u008c")
        buf.write(u"\u008c\u00a0\u00a0\4\2\u0088\u0088\u0090\u0090\4\2GG")
        buf.write(u"XX\4\2##rr\b\2\608\u0082\u0082\u008f\u008f\u0099\u0099")
        buf.write(u"\u009e\u00a0\u00a2\u00a2\b\2\608\u0082\u0082\u0088\u0088")
        buf.write(u"\u008f\u0090\u0099\u0099\u009e\u00a0\7\2\608\u0082\u0082")
        buf.write(u"\u008f\u008f\u0099\u0099\u009e\u00a2\7\2\608\u0082\u0082")
        buf.write(u"\u008f\u008f\u0099\u0099\u009e\u00a0\u094c\2\u019c\3")
        buf.write(u"\2\2\2\4\u01ad\3\2\2\2\6\u01b6\3\2\2\2\b\u01bc\3\2\2")
        buf.write(u"\2\n\u01c2\3\2\2\2\f\u01d8\3\2\2\2\16\u01e8\3\2\2\2\20")
        buf.write(u"\u01f2\3\2\2\2\22\u0203\3\2\2\2\24\u0206\3\2\2\2\26\u0213")
        buf.write(u"\3\2\2\2\30\u021c\3\2\2\2\32\u0226\3\2\2\2\34\u022f\3")
        buf.write(u"\2\2\2\36\u0239\3\2\2\2 \u024a\3\2\2\2\"\u025c\3\2\2")
        buf.write(u"\2$\u0262\3\2\2\2&\u026f\3\2\2\2(\u027d\3\2\2\2*\u028d")
        buf.write(u"\3\2\2\2,\u029d\3\2\2\2.\u02af\3\2\2\2\60\u02b2\3\2\2")
        buf.write(u"\2\62\u02c5\3\2\2\2\64\u02dc\3\2\2\2\66\u02de\3\2\2\2")
        buf.write(u"8\u02fa\3\2\2\2:\u02fc\3\2\2\2<\u0302\3\2\2\2>\u0308")
        buf.write(u"\3\2\2\2@\u0324\3\2\2\2B\u0326\3\2\2\2D\u0333\3\2\2\2")
        buf.write(u"F\u033f\3\2\2\2H\u0345\3\2\2\2J\u0351\3\2\2\2L\u0366")
        buf.write(u"\3\2\2\2N\u036a\3\2\2\2P\u039e\3\2\2\2R\u03a0\3\2\2\2")
        buf.write(u"T\u03a3\3\2\2\2V\u03a9\3\2\2\2X\u03b5\3\2\2\2Z\u03b7")
        buf.write(u"\3\2\2\2\\\u03c7\3\2\2\2^\u03e0\3\2\2\2`\u0452\3\2\2")
        buf.write(u"\2b\u0456\3\2\2\2d\u0458\3\2\2\2f\u046a\3\2\2\2h\u046c")
        buf.write(u"\3\2\2\2j\u0471\3\2\2\2l\u0478\3\2\2\2n\u047c\3\2\2\2")
        buf.write(u"p\u0484\3\2\2\2r\u04c2\3\2\2\2t\u04c4\3\2\2\2v\u04dd")
        buf.write(u"\3\2\2\2x\u04df\3\2\2\2z\u04eb\3\2\2\2|\u04f5\3\2\2\2")
        buf.write(u"~\u04f9\3\2\2\2\u0080\u0504\3\2\2\2\u0082\u0506\3\2\2")
        buf.write(u"\2\u0084\u050b\3\2\2\2\u0086\u050e\3\2\2\2\u0088\u0513")
        buf.write(u"\3\2\2\2\u008a\u0521\3\2\2\2\u008c\u052b\3\2\2\2\u008e")
        buf.write(u"\u052f\3\2\2\2\u0090\u0531\3\2\2\2\u0092\u053a\3\2\2")
        buf.write(u"\2\u0094\u0543\3\2\2\2\u0096\u0555\3\2\2\2\u0098\u0558")
        buf.write(u"\3\2\2\2\u009a\u0561\3\2\2\2\u009c\u0569\3\2\2\2\u009e")
        buf.write(u"\u0571\3\2\2\2\u00a0\u0583\3\2\2\2\u00a2\u0594\3\2\2")
        buf.write(u"\2\u00a4\u05a4\3\2\2\2\u00a6\u05a6\3\2\2\2\u00a8\u05a9")
        buf.write(u"\3\2\2\2\u00aa\u05ad\3\2\2\2\u00ac\u05b2\3\2\2\2\u00ae")
        buf.write(u"\u05b4\3\2\2\2\u00b0\u05be\3\2\2\2\u00b2\u05c3\3\2\2")
        buf.write(u"\2\u00b4\u05c5\3\2\2\2\u00b6\u05c7\3\2\2\2\u00b8\u05c9")
        buf.write(u"\3\2\2\2\u00ba\u05cb\3\2\2\2\u00bc\u05cd\3\2\2\2\u00be")
        buf.write(u"\u05da\3\2\2\2\u00c0\u05de\3\2\2\2\u00c2\u05e0\3\2\2")
        buf.write(u"\2\u00c4\u05e5\3\2\2\2\u00c6\u05ea\3\2\2\2\u00c8\u05ec")
        buf.write(u"\3\2\2\2\u00ca\u05fa\3\2\2\2\u00cc\u0608\3\2\2\2\u00ce")
        buf.write(u"\u060a\3\2\2\2\u00d0\u0616\3\2\2\2\u00d2\u0622\3\2\2")
        buf.write(u"\2\u00d4\u0624\3\2\2\2\u00d6\u0628\3\2\2\2\u00d8\u0633")
        buf.write(u"\3\2\2\2\u00da\u0637\3\2\2\2\u00dc\u0649\3\2\2\2\u00de")
        buf.write(u"\u0651\3\2\2\2\u00e0\u065d\3\2\2\2\u00e2\u065f\3\2\2")
        buf.write(u"\2\u00e4\u0661\3\2\2\2\u00e6\u0674\3\2\2\2\u00e8\u0676")
        buf.write(u"\3\2\2\2\u00ea\u067d\3\2\2\2\u00ec\u0684\3\2\2\2\u00ee")
        buf.write(u"\u068d\3\2\2\2\u00f0\u0696\3\2\2\2\u00f2\u069f\3\2\2")
        buf.write(u"\2\u00f4\u06b6\3\2\2\2\u00f6\u06c6\3\2\2\2\u00f8\u06c8")
        buf.write(u"\3\2\2\2\u00fa\u06d4\3\2\2\2\u00fc\u06d6\3\2\2\2\u00fe")
        buf.write(u"\u06d8\3\2\2\2\u0100\u06de\3\2\2\2\u0102\u06e5\3\2\2")
        buf.write(u"\2\u0104\u06e8\3\2\2\2\u0106\u06f1\3\2\2\2\u0108\u06f9")
        buf.write(u"\3\2\2\2\u010a\u0705\3\2\2\2\u010c\u070d\3\2\2\2\u010e")
        buf.write(u"\u071a\3\2\2\2\u0110\u071c\3\2\2\2\u0112\u0720\3\2\2")
        buf.write(u"\2\u0114\u072e\3\2\2\2\u0116\u0730\3\2\2\2\u0118\u0738")
        buf.write(u"\3\2\2\2\u011a\u0749\3\2\2\2\u011c\u074b\3\2\2\2\u011e")
        buf.write(u"\u074e\3\2\2\2\u0120\u0751\3\2\2\2\u0122\u0754\3\2\2")
        buf.write(u"\2\u0124\u0757\3\2\2\2\u0126\u075a\3\2\2\2\u0128\u075c")
        buf.write(u"\3\2\2\2\u012a\u075e\3\2\2\2\u012c\u0760\3\2\2\2\u012e")
        buf.write(u"\u0762\3\2\2\2\u0130\u0764\3\2\2\2\u0132\u0766\3\2\2")
        buf.write(u"\2\u0134\u076f\3\2\2\2\u0136\u0771\3\2\2\2\u0138\u0782")
        buf.write(u"\3\2\2\2\u013a\u0784\3\2\2\2\u013c\u0786\3\2\2\2\u013e")
        buf.write(u"\u078e\3\2\2\2\u0140\u0790\3\2\2\2\u0142\u0797\3\2\2")
        buf.write(u"\2\u0144\u07a2\3\2\2\2\u0146\u07a6\3\2\2\2\u0148\u07aa")
        buf.write(u"\3\2\2\2\u014a\u07b1\3\2\2\2\u014c\u07b3\3\2\2\2\u014e")
        buf.write(u"\u07b8\3\2\2\2\u0150\u07ba\3\2\2\2\u0152\u07c8\3\2\2")
        buf.write(u"\2\u0154\u07d0\3\2\2\2\u0156\u07d2\3\2\2\2\u0158\u07df")
        buf.write(u"\3\2\2\2\u015a\u07e1\3\2\2\2\u015c\u07ec\3\2\2\2\u015e")
        buf.write(u"\u07fc\3\2\2\2\u0160\u0803\3\2\2\2\u0162\u0812\3\2\2")
        buf.write(u"\2\u0164\u0814\3\2\2\2\u0166\u081d\3\2\2\2\u0168\u081f")
        buf.write(u"\3\2\2\2\u016a\u082e\3\2\2\2\u016c\u0830\3\2\2\2\u016e")
        buf.write(u"\u0832\3\2\2\2\u0170\u0838\3\2\2\2\u0172\u083a\3\2\2")
        buf.write(u"\2\u0174\u0841\3\2\2\2\u0176\u084c\3\2\2\2\u0178\u0850")
        buf.write(u"\3\2\2\2\u017a\u0854\3\2\2\2\u017c\u085f\3\2\2\2\u017e")
        buf.write(u"\u086e\3\2\2\2\u0180\u0870\3\2\2\2\u0182\u0879\3\2\2")
        buf.write(u"\2\u0184\u087b\3\2\2\2\u0186\u088a\3\2\2\2\u0188\u088c")
        buf.write(u"\3\2\2\2\u018a\u088e\3\2\2\2\u018c\u0894\3\2\2\2\u018e")
        buf.write(u"\u0896\3\2\2\2\u0190\u089d\3\2\2\2\u0192\u08a8\3\2\2")
        buf.write(u"\2\u0194\u08ac\3\2\2\2\u0196\u08b3\3\2\2\2\u0198\u08c2")
        buf.write(u"\3\2\2\2\u019a\u08c4\3\2\2\2\u019c\u019d\7^\2\2\u019d")
        buf.write(u"\u019e\7P\2\2\u019e\u01a3\5\u00b8]\2\u019f\u01a0\7\22")
        buf.write(u"\2\2\u01a0\u01a1\5\u00dep\2\u01a1\u01a2\7\23\2\2\u01a2")
        buf.write(u"\u01a4\3\2\2\2\u01a3\u019f\3\2\2\2\u01a3\u01a4\3\2\2")
        buf.write(u"\2\u01a4\u01a7\3\2\2\2\u01a5\u01a6\7b\2\2\u01a6\u01a8")
        buf.write(u"\5\u00b8]\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write(u"\u01a9\3\2\2\2\u01a9\u01aa\7\26\2\2\u01aa\u01ab\5\u0092")
        buf.write(u"J\2\u01ab\u01ac\7\27\2\2\u01ac\3\3\2\2\2\u01ad\u01ae")
        buf.write(u"\7^\2\2\u01ae\u01af\5\u00b8]\2\u01af\u01b0\7\22\2\2\u01b0")
        buf.write(u"\u01b1\5\u00a4S\2\u01b1\u01b2\7\23\2\2\u01b2\u01b3\7")
        buf.write(u"\26\2\2\u01b3\u01b4\5\u0090I\2\u01b4\u01b5\7\27\2\2\u01b5")
        buf.write(u"\5\3\2\2\2\u01b6\u01b7\5\u00ba^\2\u01b7\u01b8\7\22\2")
        buf.write(u"\2\u01b8\u01b9\5z>\2\u01b9\u01ba\7\23\2\2\u01ba\u01bb")
        buf.write(u"\7\16\2\2\u01bb\7\3\2\2\2\u01bc\u01bd\5\u00ba^\2\u01bd")
        buf.write(u"\u01be\7)\2\2\u01be\u01bf\5^\60\2\u01bf\u01c0\7\16\2")
        buf.write(u"\2\u01c0\t\3\2\2\2\u01c1\u01c3\7\u008c\2\2\u01c2\u01c1")
        buf.write(u"\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4")
        buf.write(u"\u01c5\7I\2\2\u01c5\u01c6\5\u00b6\\\2\u01c6\u01c7\7\r")
        buf.write(u"\2\2\u01c7\u01c9\5\u00a0Q\2\u01c8\u01ca\5\u0096L\2\u01c9")
        buf.write(u"\u01c8\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01d3\3\2\2")
        buf.write(u"\2\u01cb\u01cc\7\u0095\2\2\u01cc\u01d1\7l\2\2\u01cd\u01ce")
        buf.write(u"\7\22\2\2\u01ce\u01cf\5\u00dco\2\u01cf\u01d0\7\23\2\2")
        buf.write(u"\u01d0\u01d2\3\2\2\2\u01d1\u01cd\3\2\2\2\u01d1\u01d2")
        buf.write(u"\3\2\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01cb\3\2\2\2\u01d3")
        buf.write(u"\u01d4\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\7\16\2")
        buf.write(u"\2\u01d6\13\3\2\2\2\u01d7\u01d9\7\u008c\2\2\u01d8\u01d7")
        buf.write(u"\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\3\2\2\2\u01da")
        buf.write(u"\u01db\7P\2\2\u01db\u01e0\5\u00b8]\2\u01dc\u01dd\7\22")
        buf.write(u"\2\2\u01dd\u01de\5\u00dep\2\u01de\u01df\7\23\2\2\u01df")
        buf.write(u"\u01e1\3\2\2\2\u01e0\u01dc\3\2\2\2\u01e0\u01e1\3\2\2")
        buf.write(u"\2\u01e1\u01e4\3\2\2\2\u01e2\u01e3\7b\2\2\u01e3\u01e5")
        buf.write(u"\5\20\t\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write(u"\u01e6\3\2\2\2\u01e6\u01e7\5\22\n\2\u01e7\r\3\2\2\2\u01e8")
        buf.write(u"\u01e9\7\u008a\2\2\u01e9\u01ee\5\u00b8]\2\u01ea\u01eb")
        buf.write(u"\7\22\2\2\u01eb\u01ec\5\u00dep\2\u01ec\u01ed\7\23\2\2")
        buf.write(u"\u01ed\u01ef\3\2\2\2\u01ee\u01ea\3\2\2\2\u01ee\u01ef")
        buf.write(u"\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\5\22\n\2\u01f1")
        buf.write(u"\17\3\2\2\2\u01f2\u01f3\b\t\1\2\u01f3\u01f4\5\u00b8]")
        buf.write(u"\2\u01f4\u01fa\3\2\2\2\u01f5\u01f6\f\3\2\2\u01f6\u01f7")
        buf.write(u"\7\17\2\2\u01f7\u01f9\5\u00b8]\2\u01f8\u01f5\3\2\2\2")
        buf.write(u"\u01f9\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb")
        buf.write(u"\3\2\2\2\u01fb\21\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u0204")
        buf.write(u"\7\16\2\2\u01fe\u0200\7\26\2\2\u01ff\u0201\5\u00caf\2")
        buf.write(u"\u0200\u01ff\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0202")
        buf.write(u"\3\2\2\2\u0202\u0204\7\27\2\2\u0203\u01fd\3\2\2\2\u0203")
        buf.write(u"\u01fe\3\2\2\2\u0204\23\3\2\2\2\u0205\u0207\5\u00a0Q")
        buf.write(u"\2\u0206\u0205\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208")
        buf.write(u"\3\2\2\2\u0208\u0209\7|\2\2\u0209\u020a\5\u011a\u008e")
        buf.write(u"\2\u020a\u020b\7\22\2\2\u020b\u020c\5\u00c0a\2\u020c")
        buf.write(u"\u020d\7\23\2\2\u020d\u020f\7\26\2\2\u020e\u0210\5\u00ec")
        buf.write(u"w\2\u020f\u020e\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0211")
        buf.write(u"\3\2\2\2\u0211\u0212\7\27\2\2\u0212\25\3\2\2\2\u0213")
        buf.write(u"\u0214\7\u0089\2\2\u0214\u0215\5\u00b4[\2\u0215\u0217")
        buf.write(u"\7\26\2\2\u0216\u0218\5\u00ecw\2\u0217\u0216\3\2\2\2")
        buf.write(u"\u0217\u0218\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021a")
        buf.write(u"\7\27\2\2\u021a\27\3\2\2\2\u021b\u021d\7t\2\2\u021c\u021b")
        buf.write(u"\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021e\3\2\2\2\u021e")
        buf.write(u"\u021f\7\u0089\2\2\u021f\u0220\5\u00b4[\2\u0220\u0222")
        buf.write(u"\7\26\2\2\u0221\u0223\5\u00e4s\2\u0222\u0221\3\2\2\2")
        buf.write(u"\u0222\u0223\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0225")
        buf.write(u"\7\27\2\2\u0225\31\3\2\2\2\u0226\u0227\7i\2\2\u0227\u0228")
        buf.write(u"\5\u00b4[\2\u0228\u022a\7\26\2\2\u0229\u022b\5\u00ec")
        buf.write(u"w\2\u022a\u0229\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c")
        buf.write(u"\3\2\2\2\u022c\u022d\7\27\2\2\u022d\33\3\2\2\2\u022e")
        buf.write(u"\u0230\7t\2\2\u022f\u022e\3\2\2\2\u022f\u0230\3\2\2\2")
        buf.write(u"\u0230\u0231\3\2\2\2\u0231\u0232\7i\2\2\u0232\u0233\5")
        buf.write(u"\u00b4[\2\u0233\u0235\7\26\2\2\u0234\u0236\5\u00e4s\2")
        buf.write(u"\u0235\u0234\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0237")
        buf.write(u"\3\2\2\2\u0237\u0238\7\27\2\2\u0238\35\3\2\2\2\u0239")
        buf.write(u"\u023a\7t\2\2\u023a\u023b\7\u0084\2\2\u023b\u0240\5\u00b8")
        buf.write(u"]\2\u023c\u023d\7\22\2\2\u023d\u023e\5\u00dep\2\u023e")
        buf.write(u"\u023f\7\23\2\2\u023f\u0241\3\2\2\2\u0240\u023c\3\2\2")
        buf.write(u"\2\u0240\u0241\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243")
        buf.write(u"\7\26\2\2\u0243\u0245\5\"\22\2\u0244\u0246\5\u00ceh\2")
        buf.write(u"\u0245\u0244\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247")
        buf.write(u"\3\2\2\2\u0247\u0248\7\27\2\2\u0248\37\3\2\2\2\u0249")
        buf.write(u"\u024b\7\u008c\2\2\u024a\u0249\3\2\2\2\u024a\u024b\3")
        buf.write(u"\2\2\2\u024b\u024c\3\2\2\2\u024c\u024d\7t\2\2\u024d\u024e")
        buf.write(u"\7P\2\2\u024e\u0253\5\u00b8]\2\u024f\u0250\7\22\2\2\u0250")
        buf.write(u"\u0251\5\u00dep\2\u0251\u0252\7\23\2\2\u0252\u0254\3")
        buf.write(u"\2\2\2\u0253\u024f\3\2\2\2\u0253\u0254\3\2\2\2\u0254")
        buf.write(u"\u0255\3\2\2\2\u0255\u0256\7\26\2\2\u0256\u0258\5\"\22")
        buf.write(u"\2\u0257\u0259\5\u00ceh\2\u0258\u0257\3\2\2\2\u0258\u0259")
        buf.write(u"\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u025b\7\27\2\2\u025b")
        buf.write(u"!\3\2\2\2\u025c\u025d\7P\2\2\u025d\u025e\7K\2\2\u025e")
        buf.write(u"\u025f\7\26\2\2\u025f\u0260\5$\23\2\u0260\u0261\7\27")
        buf.write(u"\2\2\u0261#\3\2\2\2\u0262\u0263\b\23\1\2\u0263\u0264")
        buf.write(u"\5\u00d2j\2\u0264\u0265\7\16\2\2\u0265\u026c\3\2\2\2")
        buf.write(u"\u0266\u0267\f\3\2\2\u0267\u0268\5\u00d2j\2\u0268\u0269")
        buf.write(u"\7\16\2\2\u0269\u026b\3\2\2\2\u026a\u0266\3\2\2\2\u026b")
        buf.write(u"\u026e\3\2\2\2\u026c\u026a\3\2\2\2\u026c\u026d\3\2\2")
        buf.write(u"\2\u026d%\3\2\2\2\u026e\u026c\3\2\2\2\u026f\u0271\7A")
        buf.write(u"\2\2\u0270\u0272\5\u00a0Q\2\u0271\u0270\3\2\2\2\u0271")
        buf.write(u"\u0272\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0274\7p\2\2")
        buf.write(u"\u0274\u0275\5\u00b0Y\2\u0275\u0277\7\22\2\2\u0276\u0278")
        buf.write(u"\5\u00bc_\2\u0277\u0276\3\2\2\2\u0277\u0278\3\2\2\2\u0278")
        buf.write(u"\u0279\3\2\2\2\u0279\u027a\7\23\2\2\u027a\u027b\7\16")
        buf.write(u"\2\2\u027b\'\3\2\2\2\u027c\u027e\5\u00a0Q\2\u027d\u027c")
        buf.write(u"\3\2\2\2\u027d\u027e\3\2\2\2\u027e\u027f\3\2\2\2\u027f")
        buf.write(u"\u0280\7p\2\2\u0280\u0281\5\u00b0Y\2\u0281\u0283\7\22")
        buf.write(u"\2\2\u0282\u0284\5\u00bc_\2\u0283\u0282\3\2\2\2\u0283")
        buf.write(u"\u0284\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u0286\7\23\2")
        buf.write(u"\2\u0286\u0288\7\26\2\2\u0287\u0289\5\u00ecw\2\u0288")
        buf.write(u"\u0287\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028a\3\2\2")
        buf.write(u"\2\u028a\u028b\7\27\2\2\u028b)\3\2\2\2\u028c\u028e\5")
        buf.write(u"\u00c6d\2\u028d\u028c\3\2\2\2\u028d\u028e\3\2\2\2\u028e")
        buf.write(u"\u0290\3\2\2\2\u028f\u0291\7t\2\2\u0290\u028f\3\2\2\2")
        buf.write(u"\u0290\u0291\3\2\2\2\u0291\u0292\3\2\2\2\u0292\u0293")
        buf.write(u"\7p\2\2\u0293\u0294\5\u00b0Y\2\u0294\u0296\7\22\2\2\u0295")
        buf.write(u"\u0297\5\u00bc_\2\u0296\u0295\3\2\2\2\u0296\u0297\3\2")
        buf.write(u"\2\2\u0297\u0298\3\2\2\2\u0298\u0299\7\23\2\2\u0299\u029a")
        buf.write(u"\7\26\2\2\u029a\u029b\5\u00e4s\2\u029b\u029c\7\27\2\2")
        buf.write(u"\u029c+\3\2\2\2\u029d\u029e\7\u008f\2\2\u029e\u029f\7")
        buf.write(u"p\2\2\u029f\u02a0\7\u00a3\2\2\u02a0\u02a1\7\22\2\2\u02a1")
        buf.write(u"\u02a2\7\23\2\2\u02a2\u02a3\7\26\2\2\u02a3\u02a4\5\u00ec")
        buf.write(u"w\2\u02a4\u02a5\7\27\2\2\u02a5\u02ad\7\u0094\2\2\u02a6")
        buf.write(u"\u02a7\7\26\2\2\u02a7\u02a8\5\u00eex\2\u02a8\u02a9\7")
        buf.write(u"\27\2\2\u02a9\u02ae\3\2\2\2\u02aa\u02ab\5\u00ba^\2\u02ab")
        buf.write(u"\u02ac\7\16\2\2\u02ac\u02ae\3\2\2\2\u02ad\u02a6\3\2\2")
        buf.write(u"\2\u02ad\u02aa\3\2\2\2\u02ae-\3\2\2\2\u02af\u02b0\5^")
        buf.write(u"\60\2\u02b0\u02b1\7\16\2\2\u02b1/\3\2\2\2\u02b2\u02b7")
        buf.write(u"\5\u00c6d\2\u02b3\u02b4\7\22\2\2\u02b4\u02b5\5\u00de")
        buf.write(u"p\2\u02b5\u02b6\7\23\2\2\u02b6\u02b8\3\2\2\2\u02b7\u02b3")
        buf.write(u"\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9")
        buf.write(u"\u02bc\5\u00b4[\2\u02ba\u02bb\7)\2\2\u02bb\u02bd\5\u0100")
        buf.write(u"\u0081\2\u02bc\u02ba\3\2\2\2\u02bc\u02bd\3\2\2\2\u02bd")
        buf.write(u"\61\3\2\2\2\u02be\u02c6\5\64\33\2\u02bf\u02c3\7\26\2")
        buf.write(u"\2\u02c0\u02c1\5\u00ecw\2\u02c1\u02c2\7\27\2\2\u02c2")
        buf.write(u"\u02c4\3\2\2\2\u02c3\u02c0\3\2\2\2\u02c3\u02c4\3\2\2")
        buf.write(u"\2\u02c4\u02c6\3\2\2\2\u02c5\u02be\3\2\2\2\u02c5\u02bf")
        buf.write(u"\3\2\2\2\u02c6\63\3\2\2\2\u02c7\u02c8\5V,\2\u02c8\u02c9")
        buf.write(u"\7\16\2\2\u02c9\u02dd\3\2\2\2\u02ca\u02dd\5~@\2\u02cb")
        buf.write(u"\u02dd\5\u0082B\2\u02cc\u02dd\58\35\2\u02cd\u02dd\5\66")
        buf.write(u"\34\2\u02ce\u02dd\5R*\2\u02cf\u02dd\5T+\2\u02d0\u02dd")
        buf.write(u"\5H%\2\u02d1\u02dd\5> \2\u02d2\u02dd\5B\"\2\u02d3\u02dd")
        buf.write(u"\5F$\2\u02d4\u02dd\5D#\2\u02d5\u02dd\5N(\2\u02d6\u02dd")
        buf.write(u"\5L\'\2\u02d7\u02dd\5n8\2\u02d8\u02dd\5:\36\2\u02d9\u02dd")
        buf.write(u"\5<\37\2\u02da\u02dd\5(\25\2\u02db\u02dd\5\u00e2r\2\u02dc")
        buf.write(u"\u02c7\3\2\2\2\u02dc\u02ca\3\2\2\2\u02dc\u02cb\3\2\2")
        buf.write(u"\2\u02dc\u02cc\3\2\2\2\u02dc\u02cd\3\2\2\2\u02dc\u02ce")
        buf.write(u"\3\2\2\2\u02dc\u02cf\3\2\2\2\u02dc\u02d0\3\2\2\2\u02dc")
        buf.write(u"\u02d1\3\2\2\2\u02dc\u02d2\3\2\2\2\u02dc\u02d3\3\2\2")
        buf.write(u"\2\u02dc\u02d4\3\2\2\2\u02dc\u02d5\3\2\2\2\u02dc\u02d6")
        buf.write(u"\3\2\2\2\u02dc\u02d7\3\2\2\2\u02dc\u02d8\3\2\2\2\u02dc")
        buf.write(u"\u02d9\3\2\2\2\u02dc\u02da\3\2\2\2\u02dc\u02db\3\2\2")
        buf.write(u"\2\u02dd\65\3\2\2\2\u02de\u02df\7f\2\2\u02df\u02e0\7")
        buf.write(u"\22\2\2\u02e0\u02e1\7\23\2\2\u02e1\u02e2\7\16\2\2\u02e2")
        buf.write(u"\67\3\2\2\2\u02e3\u02e4\7W\2\2\u02e4\u02e5\7\22\2\2\u02e5")
        buf.write(u"\u02e6\5\u009cO\2\u02e6\u02e7\7\23\2\2\u02e7\u02e8\7")
        buf.write(u"\16\2\2\u02e8\u02fb\3\2\2\2\u02e9\u02ea\7\u008d\2\2\u02ea")
        buf.write(u"\u02eb\7\22\2\2\u02eb\u02ec\5\u009cO\2\u02ec\u02ed\7")
        buf.write(u"\23\2\2\u02ed\u02ee\7\16\2\2\u02ee\u02fb\3\2\2\2\u02ef")
        buf.write(u"\u02f0\7W\2\2\u02f0\u02f1\7\22\2\2\u02f1\u02f2\5\u009c")
        buf.write(u"O\2\u02f2\u02f3\7\23\2\2\u02f3\u02f4\7D\2\2\u02f4\u02f5")
        buf.write(u"\7\u008d\2\2\u02f5\u02f6\7\22\2\2\u02f6\u02f7\5\u009c")
        buf.write(u"O\2\u02f7\u02f8\7\23\2\2\u02f8\u02f9\7\16\2\2\u02f9\u02fb")
        buf.write(u"\3\2\2\2\u02fa\u02e3\3\2\2\2\u02fa\u02e9\3\2\2\2\u02fa")
        buf.write(u"\u02ef\3\2\2\2\u02fb9\3\2\2\2\u02fc\u02fd\7\u0095\2\2")
        buf.write(u"\u02fd\u02fe\7\22\2\2\u02fe\u02ff\5\u0110\u0089\2\u02ff")
        buf.write(u"\u0300\7\23\2\2\u0300\u0301\5\62\32\2\u0301;\3\2\2\2")
        buf.write(u"\u0302\u0303\7\u0095\2\2\u0303\u0304\7\22\2\2\u0304\u0305")
        buf.write(u"\5\u00b8]\2\u0305\u0306\7\23\2\2\u0306\u0307\5\62\32")
        buf.write(u"\2\u0307=\3\2\2\2\u0308\u0309\7\u008e\2\2\u0309\u030a")
        buf.write(u"\7\22\2\2\u030a\u030b\5^\60\2\u030b\u030c\7\23\2\2\u030c")
        buf.write(u"\u030d\7\26\2\2\u030d\u0313\5\u00f0y\2\u030e\u030f\7")
        buf.write(u"U\2\2\u030f\u0311\7\r\2\2\u0310\u0312\5\u00ecw\2\u0311")
        buf.write(u"\u0310\3\2\2\2\u0311\u0312\3\2\2\2\u0312\u0314\3\2\2")
        buf.write(u"\2\u0313\u030e\3\2\2\2\u0313\u0314\3\2\2\2\u0314\u0315")
        buf.write(u"\3\2\2\2\u0315\u0316\7\27\2\2\u0316?\3\2\2\2\u0317\u0318")
        buf.write(u"\7N\2\2\u0318\u0319\5\u00f6|\2\u0319\u031b\7\r\2\2\u031a")
        buf.write(u"\u031c\5\u00ecw\2\u031b\u031a\3\2\2\2\u031b\u031c\3\2")
        buf.write(u"\2\2\u031c\u0325\3\2\2\2\u031d\u031e\7N\2\2\u031e\u031f")
        buf.write(u"\7k\2\2\u031f\u0320\5\u00f4{\2\u0320\u0322\7\r\2\2\u0321")
        buf.write(u"\u0323\5\u00ecw\2\u0322\u0321\3\2\2\2\u0322\u0323\3\2")
        buf.write(u"\2\2\u0323\u0325\3\2\2\2\u0324\u0317\3\2\2\2\u0324\u031d")
        buf.write(u"\3\2\2\2\u0325A\3\2\2\2\u0326\u0327\7g\2\2\u0327\u0328")
        buf.write(u"\7[\2\2\u0328\u0329\7\22\2\2\u0329\u032c\5\u00b4[\2\u032a")
        buf.write(u"\u032b\7\17\2\2\u032b\u032d\5\u00b4[\2\u032c\u032a\3")
        buf.write(u"\2\2\2\u032c\u032d\3\2\2\2\u032d\u032e\3\2\2\2\u032e")
        buf.write(u"\u032f\7k\2\2\u032f\u0330\5^\60\2\u0330\u0331\7\23\2")
        buf.write(u"\2\u0331\u0332\5\62\32\2\u0332C\3\2\2\2\u0333\u0334\7")
        buf.write(u"Y\2\2\u0334\u0336\7\26\2\2\u0335\u0337\5\u00ecw\2\u0336")
        buf.write(u"\u0335\3\2\2\2\u0336\u0337\3\2\2\2\u0337\u0338\3\2\2")
        buf.write(u"\2\u0338\u0339\7\27\2\2\u0339\u033a\7\u0098\2\2\u033a")
        buf.write(u"\u033b\7\22\2\2\u033b\u033c\5^\60\2\u033c\u033d\7\23")
        buf.write(u"\2\2\u033d\u033e\7\16\2\2\u033eE\3\2\2\2\u033f\u0340")
        buf.write(u"\7\u0098\2\2\u0340\u0341\7\22\2\2\u0341\u0342\5^\60\2")
        buf.write(u"\u0342\u0343\7\23\2\2\u0343\u0344\5\62\32\2\u0344G\3")
        buf.write(u"\2\2\2\u0345\u0346\7j\2\2\u0346\u0347\7\22\2\2\u0347")
        buf.write(u"\u0348\5^\60\2\u0348\u0349\7\23\2\2\u0349\u034b\5\62")
        buf.write(u"\32\2\u034a\u034c\5J&\2\u034b\u034a\3\2\2\2\u034b\u034c")
        buf.write(u"\3\2\2\2\u034c\u034f\3\2\2\2\u034d\u034e\7\\\2\2\u034e")
        buf.write(u"\u0350\5\62\32\2\u034f\u034d\3\2\2\2\u034f\u0350\3\2")
        buf.write(u"\2\2\u0350I\3\2\2\2\u0351\u0352\b&\1\2\u0352\u0353\7")
        buf.write(u"\\\2\2\u0353\u0354\7j\2\2\u0354\u0355\7\22\2\2\u0355")
        buf.write(u"\u0356\5^\60\2\u0356\u0357\7\23\2\2\u0357\u0358\5\62")
        buf.write(u"\32\2\u0358\u0363\3\2\2\2\u0359\u035a\f\3\2\2\u035a\u035b")
        buf.write(u"\7\\\2\2\u035b\u035c\7j\2\2\u035c\u035d\7\22\2\2\u035d")
        buf.write(u"\u035e\5^\60\2\u035e\u035f\7\23\2\2\u035f\u0360\5\62")
        buf.write(u"\32\2\u0360\u0362\3\2\2\2\u0361\u0359\3\2\2\2\u0362\u0365")
        buf.write(u"\3\2\2\2\u0363\u0361\3\2\2\2\u0363\u0364\3\2\2\2\u0364")
        buf.write(u"K\3\2\2\2\u0365\u0363\3\2\2\2\u0366\u0367\7\u0091\2\2")
        buf.write(u"\u0367\u0368\5^\60\2\u0368\u0369\7\16\2\2\u0369M\3\2")
        buf.write(u"\2\2\u036a\u036b\7\u0093\2\2\u036b\u036c\7\22\2\2\u036c")
        buf.write(u"\u036d\5\u00b4[\2\u036d\u036e\7\23\2\2\u036e\u0370\7")
        buf.write(u"\26\2\2\u036f\u0371\5\u00ecw\2\u0370\u036f\3\2\2\2\u0370")
        buf.write(u"\u0371\3\2\2\2\u0371\u0372\3\2\2\2\u0372\u0374\7\27\2")
        buf.write(u"\2\u0373\u0375\5\u00f2z\2\u0374\u0373\3\2\2\2\u0374\u0375")
        buf.write(u"\3\2\2\2\u0375\u037f\3\2\2\2\u0376\u0377\7O\2\2\u0377")
        buf.write(u"\u0378\7\22\2\2\u0378\u0379\7E\2\2\u0379\u037a\7\23\2")
        buf.write(u"\2\u037a\u037c\7\26\2\2\u037b\u037d\5\u00ecw\2\u037c")
        buf.write(u"\u037b\3\2\2\2\u037c\u037d\3\2\2\2\u037d\u037e\3\2\2")
        buf.write(u"\2\u037e\u0380\7\27\2\2\u037f\u0376\3\2\2\2\u037f\u0380")
        buf.write(u"\3\2\2\2\u0380\u0387\3\2\2\2\u0381\u0382\7e\2\2\u0382")
        buf.write(u"\u0384\7\26\2\2\u0383\u0385\5\u00ecw\2\u0384\u0383\3")
        buf.write(u"\2\2\2\u0384\u0385\3\2\2\2\u0385\u0386\3\2\2\2\u0386")
        buf.write(u"\u0388\7\27\2\2\u0387\u0381\3\2\2\2\u0387\u0388\3\2\2")
        buf.write(u"\2\u0388O\3\2\2\2\u0389\u038a\7O\2\2\u038a\u038b\7\22")
        buf.write(u"\2\2\u038b\u038c\5\u00ba^\2\u038c\u038d\7\23\2\2\u038d")
        buf.write(u"\u038f\7\26\2\2\u038e\u0390\5\u00ecw\2\u038f\u038e\3")
        buf.write(u"\2\2\2\u038f\u0390\3\2\2\2\u0390\u0391\3\2\2\2\u0391")
        buf.write(u"\u0392\7\27\2\2\u0392\u039f\3\2\2\2\u0393\u0394\7O\2")
        buf.write(u"\2\u0394\u0395\7k\2\2\u0395\u0396\7\22\2\2\u0396\u0397")
        buf.write(u"\5\u0094K\2\u0397\u0398\7\23\2\2\u0398\u039a\7\26\2\2")
        buf.write(u"\u0399\u039b\5\u00ecw\2\u039a\u0399\3\2\2\2\u039a\u039b")
        buf.write(u"\3\2\2\2\u039b\u039c\3\2\2\2\u039c\u039d\7\27\2\2\u039d")
        buf.write(u"\u039f\3\2\2\2\u039e\u0389\3\2\2\2\u039e\u0393\3\2\2")
        buf.write(u"\2\u039fQ\3\2\2\2\u03a0\u03a1\7L\2\2\u03a1\u03a2\7\16")
        buf.write(u"\2\2\u03a2S\3\2\2\2\u03a3\u03a5\7\u0085\2\2\u03a4\u03a6")
        buf.write(u"\5^\60\2\u03a5\u03a4\3\2\2\2\u03a5\u03a6\3\2\2\2\u03a6")
        buf.write(u"\u03a7\3\2\2\2\u03a7\u03a8\7\16\2\2\u03a8U\3\2\2\2\u03a9")
        buf.write(u"\u03aa\5X-\2\u03aa\u03ac\7\22\2\2\u03ab\u03ad\5z>\2\u03ac")
        buf.write(u"\u03ab\3\2\2\2\u03ac\u03ad\3\2\2\2\u03ad\u03ae\3\2\2")
        buf.write(u"\2\u03ae\u03af\7\23\2\2\u03afW\3\2\2\2\u03b0\u03b6\5")
        buf.write(u"\u00b0Y\2\u03b1\u03b2\5Z.\2\u03b2\u03b3\7\21\2\2\u03b3")
        buf.write(u"\u03b4\5\u00b0Y\2\u03b4\u03b6\3\2\2\2\u03b5\u03b0\3\2")
        buf.write(u"\2\2\u03b5\u03b1\3\2\2\2\u03b6Y\3\2\2\2\u03b7\u03b8\b")
        buf.write(u".\1\2\u03b8\u03b9\5\u00b2Z\2\u03b9\u03be\3\2\2\2\u03ba")
        buf.write(u"\u03bb\f\3\2\2\u03bb\u03bd\5\\/\2\u03bc\u03ba\3\2\2\2")
        buf.write(u"\u03bd\u03c0\3\2\2\2\u03be\u03bc\3\2\2\2\u03be\u03bf")
        buf.write(u"\3\2\2\2\u03bf[\3\2\2\2\u03c0\u03be\3\2\2\2\u03c1\u03c2")
        buf.write(u"\7\21\2\2\u03c2\u03c8\5\u00b4[\2\u03c3\u03c4\7\24\2\2")
        buf.write(u"\u03c4\u03c5\5^\60\2\u03c5\u03c6\7\25\2\2\u03c6\u03c8")
        buf.write(u"\3\2\2\2\u03c7\u03c1\3\2\2\2\u03c7\u03c3\3\2\2\2\u03c8")
        buf.write(u"]\3\2\2\2\u03c9\u03ca\b\60\1\2\u03ca\u03cb\7\37\2\2\u03cb")
        buf.write(u"\u03e1\5^\60$\u03cc\u03cd\7\31\2\2\u03cd\u03e1\5^\60")
        buf.write(u"#\u03ce\u03cf\7\22\2\2\u03cf\u03d0\5\u00c6d\2\u03d0\u03d1")
        buf.write(u"\7\23\2\2\u03d1\u03d2\5^\60\17\u03d2\u03e1\3\2\2\2\u03d3")
        buf.write(u"\u03e1\5d\63\2\u03d4\u03e1\5f\64\2\u03d5\u03d6\7:\2\2")
        buf.write(u"\u03d6\u03d7\7\22\2\2\u03d7\u03d8\5^\60\2\u03d8\u03d9")
        buf.write(u"\7\23\2\2\u03d9\u03e1\3\2\2\2\u03da\u03db\7`\2\2\u03db")
        buf.write(u"\u03dc\7\22\2\2\u03dc\u03dd\5\u00b4[\2\u03dd\u03de\7")
        buf.write(u"\23\2\2\u03de\u03e1\3\2\2\2\u03df\u03e1\5b\62\2\u03e0")
        buf.write(u"\u03c9\3\2\2\2\u03e0\u03cc\3\2\2\2\u03e0\u03ce\3\2\2")
        buf.write(u"\2\u03e0\u03d3\3\2\2\2\u03e0\u03d4\3\2\2\2\u03e0\u03d5")
        buf.write(u"\3\2\2\2\u03e0\u03da\3\2\2\2\u03e0\u03df\3\2\2\2\u03e1")
        buf.write(u"\u044f\3\2\2\2\u03e2\u03e3\f\"\2\2\u03e3\u03e4\5\u0128")
        buf.write(u"\u0095\2\u03e4\u03e5\5^\60#\u03e5\u044e\3\2\2\2\u03e6")
        buf.write(u"\u03e7\f!\2\2\u03e7\u03e8\5\u012a\u0096\2\u03e8\u03e9")
        buf.write(u"\5^\60\"\u03e9\u044e\3\2\2\2\u03ea\u03eb\f \2\2\u03eb")
        buf.write(u"\u03ec\5\u012e\u0098\2\u03ec\u03ed\5^\60!\u03ed\u044e")
        buf.write(u"\3\2\2\2\u03ee\u03ef\f\37\2\2\u03ef\u03f0\5\u012c\u0097")
        buf.write(u"\2\u03f0\u03f1\5^\60 \u03f1\u044e\3\2\2\2\u03f2\u03f3")
        buf.write(u"\f\36\2\2\u03f3\u03f4\t\2\2\2\u03f4\u044e\5^\60\37\u03f5")
        buf.write(u"\u03f6\f\35\2\2\u03f6\u03f7\7&\2\2\u03f7\u044e\5^\60")
        buf.write(u"\36\u03f8\u03f9\f\34\2\2\u03f9\u03fa\7\'\2\2\u03fa\u044e")
        buf.write(u"\5^\60\35\u03fb\u03fc\f\33\2\2\u03fc\u03fd\7$\2\2\u03fd")
        buf.write(u"\u044e\5^\60\34\u03fe\u03ff\f\32\2\2\u03ff\u0400\7%\2")
        buf.write(u"\2\u0400\u044e\5^\60\33\u0401\u0402\f\27\2\2\u0402\u0403")
        buf.write(u"\7n\2\2\u0403\u0404\7v\2\2\u0404\u044e\5^\60\30\u0405")
        buf.write(u"\u0406\f\26\2\2\u0406\u0407\7n\2\2\u0407\u044e\5^\60")
        buf.write(u"\27\u0408\u0409\f\25\2\2\u0409\u040a\7+\2\2\u040a\u044e")
        buf.write(u"\5^\60\26\u040b\u040c\f\24\2\2\u040c\u040d\7*\2\2\u040d")
        buf.write(u"\u044e\5^\60\25\u040e\u040f\f\23\2\2\u040f\u0410\7,\2")
        buf.write(u"\2\u0410\u044e\5^\60\24\u0411\u0412\f\22\2\2\u0412\u0413")
        buf.write(u"\7\35\2\2\u0413\u044e\5^\60\23\u0414\u0415\f\21\2\2\u0415")
        buf.write(u"\u0416\7\33\2\2\u0416\u044e\5^\60\22\u0417\u0418\f\20")
        buf.write(u"\2\2\u0418\u0419\7\30\2\2\u0419\u041a\5^\60\2\u041a\u041b")
        buf.write(u"\7\r\2\2\u041b\u041c\5^\60\21\u041c\u044e\3\2\2\2\u041d")
        buf.write(u"\u041e\f\16\2\2\u041e\u041f\7k\2\2\u041f\u044e\5^\60")
        buf.write(u"\17\u0420\u0421\f\r\2\2\u0421\u0422\7S\2\2\u0422\u044e")
        buf.write(u"\5^\60\16\u0423\u0424\f\f\2\2\u0424\u0425\7S\2\2\u0425")
        buf.write(u"\u0426\7B\2\2\u0426\u044e\5^\60\r\u0427\u0428\f\13\2")
        buf.write(u"\2\u0428\u0429\7S\2\2\u0429\u042a\7E\2\2\u042a\u044e")
        buf.write(u"\5^\60\f\u042b\u042c\f\n\2\2\u042c\u042d\7v\2\2\u042d")
        buf.write(u"\u042e\7k\2\2\u042e\u044e\5^\60\13\u042f\u0430\f\t\2")
        buf.write(u"\2\u0430\u0431\7v\2\2\u0431\u0432\7S\2\2\u0432\u044e")
        buf.write(u"\5^\60\n\u0433\u0434\f\b\2\2\u0434\u0435\7v\2\2\u0435")
        buf.write(u"\u0436\7S\2\2\u0436\u0437\7B\2\2\u0437\u044e\5^\60\t")
        buf.write(u"\u0438\u0439\f\7\2\2\u0439\u043a\7v\2\2\u043a\u043b\7")
        buf.write(u"S\2\2\u043b\u043c\7E\2\2\u043c\u044e\5^\60\b\u043d\u043e")
        buf.write(u"\f\31\2\2\u043e\u043f\7n\2\2\u043f\u0440\7v\2\2\u0440")
        buf.write(u"\u044e\5`\61\2\u0441\u0442\f\30\2\2\u0442\u0443\7n\2")
        buf.write(u"\2\u0443\u044e\5`\61\2\u0444\u0445\f\3\2\2\u0445\u0446")
        buf.write(u"\7g\2\2\u0446\u0447\7[\2\2\u0447\u0448\7\22\2\2\u0448")
        buf.write(u"\u0449\5\u00b4[\2\u0449\u044a\7k\2\2\u044a\u044b\5^\60")
        buf.write(u"\2\u044b\u044c\7\23\2\2\u044c\u044e\3\2\2\2\u044d\u03e2")
        buf.write(u"\3\2\2\2\u044d\u03e6\3\2\2\2\u044d\u03ea\3\2\2\2\u044d")
        buf.write(u"\u03ee\3\2\2\2\u044d\u03f2\3\2\2\2\u044d\u03f5\3\2\2")
        buf.write(u"\2\u044d\u03f8\3\2\2\2\u044d\u03fb\3\2\2\2\u044d\u03fe")
        buf.write(u"\3\2\2\2\u044d\u0401\3\2\2\2\u044d\u0405\3\2\2\2\u044d")
        buf.write(u"\u0408\3\2\2\2\u044d\u040b\3\2\2\2\u044d\u040e\3\2\2")
        buf.write(u"\2\u044d\u0411\3\2\2\2\u044d\u0414\3\2\2\2\u044d\u0417")
        buf.write(u"\3\2\2\2\u044d\u041d\3\2\2\2\u044d\u0420\3\2\2\2\u044d")
        buf.write(u"\u0423\3\2\2\2\u044d\u0427\3\2\2\2\u044d\u042b\3\2\2")
        buf.write(u"\2\u044d\u042f\3\2\2\2\u044d\u0433\3\2\2\2\u044d\u0438")
        buf.write(u"\3\2\2\2\u044d\u043d\3\2\2\2\u044d\u0441\3\2\2\2\u044d")
        buf.write(u"\u0444\3\2\2\2\u044e\u0451\3\2\2\2\u044f\u044d\3\2\2")
        buf.write(u"\2\u044f\u0450\3\2\2\2\u0450_\3\2\2\2\u0451\u044f\3\2")
        buf.write(u"\2\2\u0452\u0453\6\61\"\3\u0453\u0454\7\u00a0\2\2\u0454")
        buf.write(u"\u0455\5\u00c6d\2\u0455a\3\2\2\2\u0456\u0457\5\u00b8")
        buf.write(u"]\2\u0457c\3\2\2\2\u0458\u0459\b\63\1\2\u0459\u045a\5")
        buf.write(u"\u00fa~\2\u045a\u045f\3\2\2\2\u045b\u045c\f\3\2\2\u045c")
        buf.write(u"\u045e\5v<\2\u045d\u045b\3\2\2\2\u045e\u0461\3\2\2\2")
        buf.write(u"\u045f\u045d\3\2\2\2\u045f\u0460\3\2\2\2\u0460e\3\2\2")
        buf.write(u"\2\u0461\u045f\3\2\2\2\u0462\u046b\5h\65\2\u0463\u046b")
        buf.write(u"\5j\66\2\u0464\u046b\5p9\2\u0465\u046b\5r:\2\u0466\u046b")
        buf.write(u"\5l\67\2\u0467\u046b\5t;\2\u0468\u046b\5V,\2\u0469\u046b")
        buf.write(u"\5x=\2\u046a\u0462\3\2\2\2\u046a\u0463\3\2\2\2\u046a")
        buf.write(u"\u0464\3\2\2\2\u046a\u0465\3\2\2\2\u046a\u0466\3\2\2")
        buf.write(u"\2\u046a\u0467\3\2\2\2\u046a\u0468\3\2\2\2\u046a\u0469")
        buf.write(u"\3\2\2\2\u046bg\3\2\2\2\u046c\u046d\7<\2\2\u046d\u046e")
        buf.write(u"\7\22\2\2\u046e\u046f\5^\60\2\u046f\u0470\7\23\2\2\u0470")
        buf.write(u"i\3\2\2\2\u0471\u0472\7;\2\2\u0472\u0474\7\22\2\2\u0473")
        buf.write(u"\u0475\5^\60\2\u0474\u0473\3\2\2\2\u0474\u0475\3\2\2")
        buf.write(u"\2\u0475\u0476\3\2\2\2\u0476\u0477\7\23\2\2\u0477k\3")
        buf.write(u"\2\2\2\u0478\u0479\7\u0082\2\2\u0479\u047a\7h\2\2\u047a")
        buf.write(u"\u047b\5^\60\2\u047bm\3\2\2\2\u047c\u047d\7\u0099\2\2")
        buf.write(u"\u047d\u047e\7\22\2\2\u047e\u047f\5^\60\2\u047f\u0480")
        buf.write(u"\7\23\2\2\u0480\u0481\7\u0092\2\2\u0481\u0482\5^\60\2")
        buf.write(u"\u0482\u0483\7\16\2\2\u0483o\3\2\2\2\u0484\u0485\7d\2")
        buf.write(u"\2\u0485\u0486\7\22\2\2\u0486\u0487\5^\60\2\u0487\u0488")
        buf.write(u"\7\23\2\2\u0488\u0489\7\u0095\2\2\u0489\u048a\7\22\2")
        buf.write(u"\2\u048a\u048b\5\u00b4[\2\u048b\u048c\7\23\2\2\u048c")
        buf.write(u"\u048d\7\u0097\2\2\u048d\u048e\7\22\2\2\u048e\u048f\5")
        buf.write(u"^\60\2\u048f\u0490\7\23\2\2\u0490q\3\2\2\2\u0491\u0492")
        buf.write(u"\7c\2\2\u0492\u0497\7z\2\2\u0493\u0494\7\22\2\2\u0494")
        buf.write(u"\u0495\5\u00a8U\2\u0495\u0496\7\23\2\2\u0496\u0498\3")
        buf.write(u"\2\2\2\u0497\u0493\3\2\2\2\u0497\u0498\3\2\2\2\u0498")
        buf.write(u"\u0499\3\2\2\2\u0499\u049a\7\u0097\2\2\u049a\u049b\7")
        buf.write(u"\22\2\2\u049b\u049c\5^\60\2\u049c\u049d\7\23\2\2\u049d")
        buf.write(u"\u04c3\3\2\2\2\u049e\u04b1\7c\2\2\u049f\u04a0\7B\2\2")
        buf.write(u"\u04a0\u04a2\7\22\2\2\u04a1\u04a3\5\u00a8U\2\u04a2\u04a1")
        buf.write(u"\3\2\2\2\u04a2\u04a3\3\2\2\2\u04a3\u04a4\3\2\2\2\u04a4")
        buf.write(u"\u04b2\7\23\2\2\u04a5\u04a7\7\22\2\2\u04a6\u04a8\5\u00a8")
        buf.write(u"U\2\u04a7\u04a6\3\2\2\2\u04a7\u04a8\3\2\2\2\u04a8\u04a9")
        buf.write(u"\3\2\2\2\u04a9\u04aa\7\23\2\2\u04aa\u04ab\7\u0087\2\2")
        buf.write(u"\u04ab\u04ac\7\22\2\2\u04ac\u04ad\5^\60\2\u04ad\u04ae")
        buf.write(u"\7\u0092\2\2\u04ae\u04af\5^\60\2\u04af\u04b0\7\23\2\2")
        buf.write(u"\u04b0\u04b2\3\2\2\2\u04b1\u049f\3\2\2\2\u04b1\u04a5")
        buf.write(u"\3\2\2\2\u04b2\u04b8\3\2\2\2\u04b3\u04b4\7\u0097\2\2")
        buf.write(u"\u04b4\u04b5\7\22\2\2\u04b5\u04b6\5^\60\2\u04b6\u04b7")
        buf.write(u"\7\23\2\2\u04b7\u04b9\3\2\2\2\u04b8\u04b3\3\2\2\2\u04b8")
        buf.write(u"\u04b9\3\2\2\2\u04b9\u04c0\3\2\2\2\u04ba\u04bb\7~\2\2")
        buf.write(u"\u04bb\u04bc\7M\2\2\u04bc\u04bd\7\22\2\2\u04bd\u04be")
        buf.write(u"\5\u0116\u008c\2\u04be\u04bf\7\23\2\2\u04bf\u04c1\3\2")
        buf.write(u"\2\2\u04c0\u04ba\3\2\2\2\u04c0\u04c1\3\2\2\2\u04c1\u04c3")
        buf.write(u"\3\2\2\2\u04c2\u0491\3\2\2\2\u04c2\u049e\3\2\2\2\u04c3")
        buf.write(u"s\3\2\2\2\u04c4\u04c6\7\u008b\2\2\u04c5\u04c7\7X\2\2")
        buf.write(u"\u04c6\u04c5\3\2\2\2\u04c6\u04c7\3\2\2\2\u04c7\u04c8")
        buf.write(u"\3\2\2\2\u04c8\u04c9\7\22\2\2\u04c9\u04cf\5d\63\2\u04ca")
        buf.write(u"\u04cb\7\17\2\2\u04cb\u04cc\5\u011e\u0090\2\u04cc\u04cd")
        buf.write(u"\7)\2\2\u04cd\u04ce\5d\63\2\u04ce\u04d0\3\2\2\2\u04cf")
        buf.write(u"\u04ca\3\2\2\2\u04cf\u04d0\3\2\2\2\u04d0\u04d1\3\2\2")
        buf.write(u"\2\u04d1\u04d2\7\23\2\2\u04d2u\3\2\2\2\u04d3\u04d4\7")
        buf.write(u"\21\2\2\u04d4\u04de\5\u00b4[\2\u04d5\u04d6\7\24\2\2\u04d6")
        buf.write(u"\u04d7\5^\60\2\u04d7\u04d8\7\25\2\2\u04d8\u04de\3\2\2")
        buf.write(u"\2\u04d9\u04da\7\24\2\2\u04da\u04db\5\u010e\u0088\2\u04db")
        buf.write(u"\u04dc\7\25\2\2\u04dc\u04de\3\2\2\2\u04dd\u04d3\3\2\2")
        buf.write(u"\2\u04dd\u04d5\3\2\2\2\u04dd\u04d9\3\2\2\2\u04dew\3\2")
        buf.write(u"\2\2\u04df\u04e0\5\u00a8U\2\u04e0\u04e2\7\22\2\2\u04e1")
        buf.write(u"\u04e3\5z>\2\u04e2\u04e1\3\2\2\2\u04e2\u04e3\3\2\2\2")
        buf.write(u"\u04e3\u04e4\3\2\2\2\u04e4\u04e5\7\23\2\2\u04e5y\3\2")
        buf.write(u"\2\2\u04e6\u04e7\b>\1\2\u04e7\u04e8\5^\60\2\u04e8\u04e9")
        buf.write(u"\6>$\3\u04e9\u04ec\3\2\2\2\u04ea\u04ec\5|?\2\u04eb\u04e6")
        buf.write(u"\3\2\2\2\u04eb\u04ea\3\2\2\2\u04ec\u04f2\3\2\2\2\u04ed")
        buf.write(u"\u04ee\f\3\2\2\u04ee\u04ef\7\17\2\2\u04ef\u04f1\5|?\2")
        buf.write(u"\u04f0\u04ed\3\2\2\2\u04f1\u04f4\3\2\2\2\u04f2\u04f0")
        buf.write(u"\3\2\2\2\u04f2\u04f3\3\2\2\2\u04f3{\3\2\2\2\u04f4\u04f2")
        buf.write(u"\3\2\2\2\u04f5\u04f6\5\u00b4[\2\u04f6\u04f7\5\u0126\u0094")
        buf.write(u"\2\u04f7\u04f8\5^\60\2\u04f8}\3\2\2\2\u04f9\u04fa\5\u0112")
        buf.write(u"\u008a\2\u04fa\u04fb\5\u0126\u0094\2\u04fb\u04fc\5^\60")
        buf.write(u"\2\u04fc\u04fd\7\16\2\2\u04fd\177\3\2\2\2\u04fe\u04ff")
        buf.write(u"\7\21\2\2\u04ff\u0505\5\u00b4[\2\u0500\u0501\7\24\2\2")
        buf.write(u"\u0501\u0502\5^\60\2\u0502\u0503\7\25\2\2\u0503\u0505")
        buf.write(u"\3\2\2\2\u0504\u04fe\3\2\2\2\u0504\u0500\3\2\2\2\u0505")
        buf.write(u"\u0081\3\2\2\2\u0506\u0507\5\u00dco\2\u0507\u0508\5\u0126")
        buf.write(u"\u0094\2\u0508\u0509\5^\60\2\u0509\u050a\7\16\2\2\u050a")
        buf.write(u"\u0083\3\2\2\2\u050b\u050c\7x\2\2\u050c\u0085\3\2\2\2")
        buf.write(u"\u050d\u050f\5\u0088E\2\u050e\u050d\3\2\2\2\u050e\u050f")
        buf.write(u"\3\2\2\2\u050f\u0510\3\2\2\2\u0510\u0511\5\u0130\u0099")
        buf.write(u"\2\u0511\u0512\7\2\2\3\u0512\u0087\3\2\2\2\u0513\u0519")
        buf.write(u"\5\u008aF\2\u0514\u0515\5\u0132\u009a\2\u0515\u0516\5")
        buf.write(u"\u008aF\2\u0516\u0518\3\2\2\2\u0517\u0514\3\2\2\2\u0518")
        buf.write(u"\u051b\3\2\2\2\u0519\u0517\3\2\2\2\u0519\u051a\3\2\2")
        buf.write(u"\2\u051a\u0089\3\2\2\2\u051b\u0519\3\2\2\2\u051c\u051d")
        buf.write(u"\5\u00e2r\2\u051d\u051e\5\u0132\u009a\2\u051e\u0520\3")
        buf.write(u"\2\2\2\u051f\u051c\3\2\2\2\u0520\u0523\3\2\2\2\u0521")
        buf.write(u"\u051f\3\2\2\2\u0521\u0522\3\2\2\2\u0522\u0529\3\2\2")
        buf.write(u"\2\u0523\u0521\3\2\2\2\u0524\u052a\5\n\6\2\u0525\u052a")
        buf.write(u"\5\u00acW\2\u0526\u052a\5\u008cG\2\u0527\u052a\5\u008e")
        buf.write(u"H\2\u0528\u052a\5\u00e0q\2\u0529\u0524\3\2\2\2\u0529")
        buf.write(u"\u0525\3\2\2\2\u0529\u0526\3\2\2\2\u0529\u0527\3\2\2")
        buf.write(u"\2\u0529\u0528\3\2\2\2\u052a\u008b\3\2\2\2\u052b\u052c")
        buf.write(u"\5\36\20\2\u052c\u008d\3\2\2\2\u052d\u0530\5\2\2\2\u052e")
        buf.write(u"\u0530\5\4\3\2\u052f\u052d\3\2\2\2\u052f\u052e\3\2\2")
        buf.write(u"\2\u0530\u008f\3\2\2\2\u0531\u0537\5\b\5\2\u0532\u0533")
        buf.write(u"\5\u0132\u009a\2\u0533\u0534\5\b\5\2\u0534\u0536\3\2")
        buf.write(u"\2\2\u0535\u0532\3\2\2\2\u0536\u0539\3\2\2\2\u0537\u0535")
        buf.write(u"\3\2\2\2\u0537\u0538\3\2\2\2\u0538\u0091\3\2\2\2\u0539")
        buf.write(u"\u0537\3\2\2\2\u053a\u0540\5\6\4\2\u053b\u053c\5\u0132")
        buf.write(u"\u009a\2\u053c\u053d\5\6\4\2\u053d\u053f\3\2\2\2\u053e")
        buf.write(u"\u053b\3\2\2\2\u053f\u0542\3\2\2\2\u0540\u053e\3\2\2")
        buf.write(u"\2\u0540\u0541\3\2\2\2\u0541\u0093\3\2\2\2\u0542\u0540")
        buf.write(u"\3\2\2\2\u0543\u0548\5\u00ba^\2\u0544\u0545\7\17\2\2")
        buf.write(u"\u0545\u0547\5\u00ba^\2\u0546\u0544\3\2\2\2\u0547\u054a")
        buf.write(u"\3\2\2\2\u0548\u0546\3\2\2\2\u0548\u0549\3\2\2\2\u0549")
        buf.write(u"\u0095\3\2\2\2\u054a\u0548\3\2\2\2\u054b\u054c\7k\2\2")
        buf.write(u"\u054c\u0556\5\u0098M\2\u054d\u054e\7k\2\2\u054e\u0556")
        buf.write(u"\5\u009aN\2\u054f\u0550\7k\2\2\u0550\u0556\5\u009eP\2")
        buf.write(u"\u0551\u0552\7o\2\2\u0552\u0556\7\u00a3\2\2\u0553\u0554")
        buf.write(u"\7o\2\2\u0554\u0556\5^\60\2\u0555\u054b\3\2\2\2\u0555")
        buf.write(u"\u054d\3\2\2\2\u0555\u054f\3\2\2\2\u0555\u0551\3\2\2")
        buf.write(u"\2\u0555\u0553\3\2\2\2\u0556\u0097\3\2\2\2\u0557\u0559")
        buf.write(u"\7s\2\2\u0558\u0557\3\2\2\2\u0558\u0559\3\2\2\2\u0559")
        buf.write(u"\u055a\3\2\2\2\u055a\u055c\7\24\2\2\u055b\u055d\5\u009c")
        buf.write(u"O\2\u055c\u055b\3\2\2\2\u055c\u055d\3\2\2\2\u055d\u055e")
        buf.write(u"\3\2\2\2\u055e\u055f\7\25\2\2\u055f\u0099\3\2\2\2\u0560")
        buf.write(u"\u0562\7s\2\2\u0561\u0560\3\2\2\2\u0561\u0562\3\2\2\2")
        buf.write(u"\u0562\u0563\3\2\2\2\u0563\u0565\7&\2\2\u0564\u0566\5")
        buf.write(u"\u009cO\2\u0565\u0564\3\2\2\2\u0565\u0566\3\2\2\2\u0566")
        buf.write(u"\u0567\3\2\2\2\u0567\u0568\7$\2\2\u0568\u009b\3\2\2\2")
        buf.write(u"\u0569\u056e\5^\60\2\u056a\u056b\7\17\2\2\u056b\u056d")
        buf.write(u"\5^\60\2\u056c\u056a\3\2\2\2\u056d\u0570\3\2\2\2\u056e")
        buf.write(u"\u056c\3\2\2\2\u056e\u056f\3\2\2\2\u056f\u009d\3\2\2")
        buf.write(u"\2\u0570\u056e\3\2\2\2\u0571\u0572\7\24\2\2\u0572\u0573")
        buf.write(u"\5^\60\2\u0573\u0574\7\20\2\2\u0574\u0575\5^\60\2\u0575")
        buf.write(u"\u0576\7\25\2\2\u0576\u009f\3\2\2\2\u0577\u0578\bQ\1")
        buf.write(u"\2\u0578\u0584\5\u00a2R\2\u0579\u057a\7@\2\2\u057a\u057b")
        buf.write(u"\7&\2\2\u057b\u057c\5\u00a0Q\2\u057c\u057d\7$\2\2\u057d")
        buf.write(u"\u0584\3\2\2\2\u057e\u057f\7?\2\2\u057f\u0580\7&\2\2")
        buf.write(u"\u0580\u0581\5\u00a0Q\2\u0581\u0582\7$\2\2\u0582\u0584")
        buf.write(u"\3\2\2\2\u0583\u0577\3\2\2\2\u0583\u0579\3\2\2\2\u0583")
        buf.write(u"\u057e\3\2\2\2\u0584\u058f\3\2\2\2\u0585\u0586\f\7\2")
        buf.write(u"\2\u0586\u058e\7(\2\2\u0587\u0588\f\6\2\2\u0588\u0589")
        buf.write(u"\7\24\2\2\u0589\u058e\7\25\2\2\u058a\u058b\f\5\2\2\u058b")
        buf.write(u"\u058c\7\26\2\2\u058c\u058e\7\27\2\2\u058d\u0585\3\2")
        buf.write(u"\2\2\u058d\u0587\3\2\2\2\u058d\u058a\3\2\2\2\u058e\u0591")
        buf.write(u"\3\2\2\2\u058f\u058d\3\2\2\2\u058f\u0590\3\2\2\2\u0590")
        buf.write(u"\u00a1\3\2\2\2\u0591\u058f\3\2\2\2\u0592\u0595\5\u00a4")
        buf.write(u"S\2\u0593\u0595\5\u00a6T\2\u0594\u0592\3\2\2\2\u0594")
        buf.write(u"\u0593\3\2\2\2\u0595\u00a3\3\2\2\2\u0596\u05a5\7\60\2")
        buf.write(u"\2\u0597\u05a5\7\61\2\2\u0598\u05a5\7\62\2\2\u0599\u05a5")
        buf.write(u"\7=\2\2\u059a\u05a5\7\63\2\2\u059b\u05a5\7\64\2\2\u059c")
        buf.write(u"\u05a5\7;\2\2\u059d\u05a5\7\65\2\2\u059e\u05a5\7\67\2")
        buf.write(u"\2\u059f\u05a5\7\66\2\2\u05a0\u05a5\78\2\2\u05a1\u05a5")
        buf.write(u"\7:\2\2\u05a2\u05a5\7<\2\2\u05a3\u05a5\7>\2\2\u05a4\u0596")
        buf.write(u"\3\2\2\2\u05a4\u0597\3\2\2\2\u05a4\u0598\3\2\2\2\u05a4")
        buf.write(u"\u0599\3\2\2\2\u05a4\u059a\3\2\2\2\u05a4\u059b\3\2\2")
        buf.write(u"\2\u05a4\u059c\3\2\2\2\u05a4\u059d\3\2\2\2\u05a4\u059e")
        buf.write(u"\3\2\2\2\u05a4\u059f\3\2\2\2\u05a4\u05a0\3\2\2\2\u05a4")
        buf.write(u"\u05a1\3\2\2\2\u05a4\u05a2\3\2\2\2\u05a4\u05a3\3\2\2")
        buf.write(u"\2\u05a5\u00a5\3\2\2\2\u05a6\u05a7\7\u009f\2\2\u05a7")
        buf.write(u"\u00a7\3\2\2\2\u05a8\u05aa\7s\2\2\u05a9\u05a8\3\2\2\2")
        buf.write(u"\u05a9\u05aa\3\2\2\2\u05aa\u05ab\3\2\2\2\u05ab\u05ac")
        buf.write(u"\5\u00a6T\2\u05ac\u00a9\3\2\2\2\u05ad\u05ae\7:\2\2\u05ae")
        buf.write(u"\u00ab\3\2\2\2\u05af\u05b3\5\f\7\2\u05b0\u05b3\5 \21")
        buf.write(u"\2\u05b1\u05b3\5\16\b\2\u05b2\u05af\3\2\2\2\u05b2\u05b0")
        buf.write(u"\3\2\2\2\u05b2\u05b1\3\2\2\2\u05b3\u00ad\3\2\2\2\u05b4")
        buf.write(u"\u05b9\5\u00b8]\2\u05b5\u05b6\7\17\2\2\u05b6\u05b8\5")
        buf.write(u"\u00b8]\2\u05b7\u05b5\3\2\2\2\u05b8\u05bb\3\2\2\2\u05b9")
        buf.write(u"\u05b7\3\2\2\2\u05b9\u05ba\3\2\2\2\u05ba\u00af\3\2\2")
        buf.write(u"\2\u05bb\u05b9\3\2\2\2\u05bc\u05bf\5\u00b4[\2\u05bd\u05bf")
        buf.write(u"\5\u00b8]\2\u05be\u05bc\3\2\2\2\u05be\u05bd\3\2\2\2\u05bf")
        buf.write(u"\u00b1\3\2\2\2\u05c0\u05c4\5\u00b4[\2\u05c1\u05c4\5\u00b8")
        buf.write(u"]\2\u05c2\u05c4\5\u00ba^\2\u05c3\u05c0\3\2\2\2\u05c3")
        buf.write(u"\u05c1\3\2\2\2\u05c3\u05c2\3\2\2\2\u05c4\u00b3\3\2\2")
        buf.write(u"\2\u05c5\u05c6\7\u00a0\2\2\u05c6\u00b5\3\2\2\2\u05c7")
        buf.write(u"\u05c8\t\3\2\2\u05c8\u00b7\3\2\2\2\u05c9\u05ca\7\u009f")
        buf.write(u"\2\2\u05ca\u00b9\3\2\2\2\u05cb\u05cc\7\u009e\2\2\u05cc")
        buf.write(u"\u00bb\3\2\2\2\u05cd\u05d2\5\u00be`\2\u05ce\u05cf\7\17")
        buf.write(u"\2\2\u05cf\u05d1\5\u00be`\2\u05d0\u05ce\3\2\2\2\u05d1")
        buf.write(u"\u05d4\3\2\2\2\u05d2\u05d0\3\2\2\2\u05d2\u05d3\3\2\2")
        buf.write(u"\2\u05d3\u00bd\3\2\2\2\u05d4\u05d2\3\2\2\2\u05d5\u05db")
        buf.write(u"\5\u00c4c\2\u05d6\u05d8\7s\2\2\u05d7\u05d6\3\2\2\2\u05d7")
        buf.write(u"\u05d8\3\2\2\2\u05d8\u05d9\3\2\2\2\u05d9\u05db\5\u00c0")
        buf.write(u"a\2\u05da\u05d5\3\2\2\2\u05da\u05d7\3\2\2\2\u05db\u00bf")
        buf.write(u"\3\2\2\2\u05dc\u05df\5\u00c2b\2\u05dd\u05df\5\60\31\2")
        buf.write(u"\u05de\u05dc\3\2\2\2\u05de\u05dd\3\2\2\2\u05df\u00c1")
        buf.write(u"\3\2\2\2\u05e0\u05e3\5\u00b4[\2\u05e1\u05e2\7)\2\2\u05e2")
        buf.write(u"\u05e4\5\u0100\u0081\2\u05e3\u05e1\3\2\2\2\u05e3\u05e4")
        buf.write(u"\3\2\2\2\u05e4\u00c3\3\2\2\2\u05e5\u05e6\5\u00aaV\2\u05e6")
        buf.write(u"\u05e7\5\u00b4[\2\u05e7\u00c5\3\2\2\2\u05e8\u05eb\5\u00a0")
        buf.write(u"Q\2\u05e9\u05eb\5\u00c8e\2\u05ea\u05e8\3\2\2\2\u05ea")
        buf.write(u"\u05e9\3\2\2\2\u05eb\u00c7\3\2\2\2\u05ec\u05ed\be\1\2")
        buf.write(u"\u05ed\u05ee\7E\2\2\u05ee\u05f7\3\2\2\2\u05ef\u05f0\f")
        buf.write(u"\4\2\2\u05f0\u05f1\7\24\2\2\u05f1\u05f6\7\25\2\2\u05f2")
        buf.write(u"\u05f3\f\3\2\2\u05f3\u05f4\7\26\2\2\u05f4\u05f6\7\27")
        buf.write(u"\2\2\u05f5\u05ef\3\2\2\2\u05f5\u05f2\3\2\2\2\u05f6\u05f9")
        buf.write(u"\3\2\2\2\u05f7\u05f5\3\2\2\2\u05f7\u05f8\3\2\2\2\u05f8")
        buf.write(u"\u00c9\3\2\2\2\u05f9\u05f7\3\2\2\2\u05fa\u0600\5\u00cc")
        buf.write(u"g\2\u05fb\u05fc\5\u0132\u009a\2\u05fc\u05fd\5\u00ccg")
        buf.write(u"\2\u05fd\u05ff\3\2\2\2\u05fe\u05fb\3\2\2\2\u05ff\u0602")
        buf.write(u"\3\2\2\2\u0600\u05fe\3\2\2\2\u0600\u0601\3\2\2\2\u0601")
        buf.write(u"\u00cb\3\2\2\2\u0602\u0600\3\2\2\2\u0603\u0609\5\26\f")
        buf.write(u"\2\u0604\u0609\5\32\16\2\u0605\u0609\5(\25\2\u0606\u0609")
        buf.write(u"\5&\24\2\u0607\u0609\5\24\13\2\u0608\u0603\3\2\2\2\u0608")
        buf.write(u"\u0604\3\2\2\2\u0608\u0605\3\2\2\2\u0608\u0606\3\2\2")
        buf.write(u"\2\u0608\u0607\3\2\2\2\u0609\u00cd\3\2\2\2\u060a\u0610")
        buf.write(u"\5\u00d0i\2\u060b\u060c\5\u0132\u009a\2\u060c\u060d\5")
        buf.write(u"\u00d0i\2\u060d\u060f\3\2\2\2\u060e\u060b\3\2\2\2\u060f")
        buf.write(u"\u0612\3\2\2\2\u0610\u060e\3\2\2\2\u0610\u0611\3\2\2")
        buf.write(u"\2\u0611\u00cf\3\2\2\2\u0612\u0610\3\2\2\2\u0613\u0617")
        buf.write(u"\5\34\17\2\u0614\u0617\5\30\r\2\u0615\u0617\5*\26\2\u0616")
        buf.write(u"\u0613\3\2\2\2\u0616\u0614\3\2\2\2\u0616\u0615\3\2\2")
        buf.write(u"\2\u0617\u00d1\3\2\2\2\u0618\u0619\7\7\2\2\u0619\u0623")
        buf.write(u"\5\u017c\u00bf\2\u061a\u061b\7\b\2\2\u061b\u0623\5\u0196")
        buf.write(u"\u00cc\2\u061c\u061d\7\t\2\2\u061d\u0623\5\u00d4k\2\u061e")
        buf.write(u"\u061f\7\n\2\2\u061f\u0623\5\u00d4k\2\u0620\u0621\7\13")
        buf.write(u"\2\2\u0621\u0623\5\u00d8m\2\u0622\u0618\3\2\2\2\u0622")
        buf.write(u"\u061a\3\2\2\2\u0622\u061c\3\2\2\2\u0622\u061e\3\2\2")
        buf.write(u"\2\u0622\u0620\3\2\2\2\u0623\u00d3\3\2\2\2\u0624\u0626")
        buf.write(u"\5\u00b2Z\2\u0625\u0627\5\u00d6l\2\u0626\u0625\3\2\2")
        buf.write(u"\2\u0626\u0627\3\2\2\2\u0627\u00d5\3\2\2\2\u0628\u0629")
        buf.write(u"\7h\2\2\u0629\u062a\5\u0120\u0091\2\u062a\u062b\7\r\2")
        buf.write(u"\2\u062b\u0630\5\u00b2Z\2\u062c\u062d\7\21\2\2\u062d")
        buf.write(u"\u062f\5\u00b2Z\2\u062e\u062c\3\2\2\2\u062f\u0632\3\2")
        buf.write(u"\2\2\u0630\u062e\3\2\2\2\u0630\u0631\3\2\2\2\u0631\u00d7")
        buf.write(u"\3\2\2\2\u0632\u0630\3\2\2\2\u0633\u0635\5\u00b2Z\2\u0634")
        buf.write(u"\u0636\5\u00dan\2\u0635\u0634\3\2\2\2\u0635\u0636\3\2")
        buf.write(u"\2\2\u0636\u00d9\3\2\2\2\u0637\u0638\7h\2\2\u0638\u0639")
        buf.write(u"\5\u0120\u0091\2\u0639\u063b\7\r\2\2\u063a\u063c\7!\2")
        buf.write(u"\2\u063b\u063a\3\2\2\2\u063b\u063c\3\2\2\2\u063c\u063d")
        buf.write(u"\3\2\2\2\u063d\u0642\5\u014c\u00a7\2\u063e\u063f\7!\2")
        buf.write(u"\2\u063f\u0641\5\u014c\u00a7\2\u0640\u063e\3\2\2\2\u0641")
        buf.write(u"\u0644\3\2\2\2\u0642\u0640\3\2\2\2\u0642\u0643\3\2\2")
        buf.write(u"\2\u0643\u0647\3\2\2\2\u0644\u0642\3\2\2\2\u0645\u0646")
        buf.write(u"\7\21\2\2\u0646\u0648\5\u014c\u00a7\2\u0647\u0645\3\2")
        buf.write(u"\2\2\u0647\u0648\3\2\2\2\u0648\u00db\3\2\2\2\u0649\u064e")
        buf.write(u"\5\u00b4[\2\u064a\u064b\7\17\2\2\u064b\u064d\5\u00b4")
        buf.write(u"[\2\u064c\u064a\3\2\2\2\u064d\u0650\3\2\2\2\u064e\u064c")
        buf.write(u"\3\2\2\2\u064e\u064f\3\2\2\2\u064f\u00dd\3\2\2\2\u0650")
        buf.write(u"\u064e\3\2\2\2\u0651\u0656\5\u00b6\\\2\u0652\u0653\7")
        buf.write(u"\17\2\2\u0653\u0655\5\u00b6\\\2\u0654\u0652\3\2\2\2\u0655")
        buf.write(u"\u0658\3\2\2\2\u0656\u0654\3\2\2\2\u0656\u0657\3\2\2")
        buf.write(u"\2\u0657\u00df\3\2\2\2\u0658\u0656\3\2\2\2\u0659\u065e")
        buf.write(u"\5&\24\2\u065a\u065e\5(\25\2\u065b\u065e\5*\26\2\u065c")
        buf.write(u"\u065e\5,\27\2\u065d\u0659\3\2\2\2\u065d\u065a\3\2\2")
        buf.write(u"\2\u065d\u065b\3\2\2\2\u065d\u065c\3\2\2\2\u065e\u00e1")
        buf.write(u"\3\2\2\2\u065f\u0660\7\6\2\2\u0660\u00e3\3\2\2\2\u0661")
        buf.write(u"\u0667\5\u00e6t\2\u0662\u0663\5\u0132\u009a\2\u0663\u0664")
        buf.write(u"\5\u00e6t\2\u0664\u0666\3\2\2\2\u0665\u0662\3\2\2\2\u0666")
        buf.write(u"\u0669\3\2\2\2\u0667\u0665\3\2\2\2\u0667\u0668\3\2\2")
        buf.write(u"\2\u0668\u00e5\3\2\2\2\u0669\u0667\3\2\2\2\u066a\u066b")
        buf.write(u"\7\7\2\2\u066b\u0675\5\u0166\u00b4\2\u066c\u066d\7\b")
        buf.write(u"\2\2\u066d\u0675\5\u0182\u00c2\2\u066e\u066f\7\t\2\2")
        buf.write(u"\u066f\u0675\5\u00e8u\2\u0670\u0671\7\n\2\2\u0671\u0675")
        buf.write(u"\5\u00e8u\2\u0672\u0673\7\13\2\2\u0673\u0675\5\u00ea")
        buf.write(u"v\2\u0674\u066a\3\2\2\2\u0674\u066c\3\2\2\2\u0674\u066e")
        buf.write(u"\3\2\2\2\u0674\u0670\3\2\2\2\u0674\u0672\3\2\2\2\u0675")
        buf.write(u"\u00e7\3\2\2\2\u0676\u0678\5\u014e\u00a8\2\u0677\u0679")
        buf.write(u"\7\16\2\2\u0678\u0677\3\2\2\2\u0678\u0679\3\2\2\2\u0679")
        buf.write(u"\u067b\3\2\2\2\u067a\u067c\5\u00d6l\2\u067b\u067a\3\2")
        buf.write(u"\2\2\u067b\u067c\3\2\2\2\u067c\u00e9\3\2\2\2\u067d\u067f")
        buf.write(u"\5\u0134\u009b\2\u067e\u0680\7\16\2\2\u067f\u067e\3\2")
        buf.write(u"\2\2\u067f\u0680\3\2\2\2\u0680\u0682\3\2\2\2\u0681\u0683")
        buf.write(u"\5\u00dan\2\u0682\u0681\3\2\2\2\u0682\u0683\3\2\2\2\u0683")
        buf.write(u"\u00eb\3\2\2\2\u0684\u068a\5\64\33\2\u0685\u0686\5\u0132")
        buf.write(u"\u009a\2\u0686\u0687\5\64\33\2\u0687\u0689\3\2\2\2\u0688")
        buf.write(u"\u0685\3\2\2\2\u0689\u068c\3\2\2\2\u068a\u0688\3\2\2")
        buf.write(u"\2\u068a\u068b\3\2\2\2\u068b\u00ed\3\2\2\2\u068c\u068a")
        buf.write(u"\3\2\2\2\u068d\u0693\5.\30\2\u068e\u068f\5\u0132\u009a")
        buf.write(u"\2\u068f\u0690\5.\30\2\u0690\u0692\3\2\2\2\u0691\u068e")
        buf.write(u"\3\2\2\2\u0692\u0695\3\2\2\2\u0693\u0691\3\2\2\2\u0693")
        buf.write(u"\u0694\3\2\2\2\u0694\u00ef\3\2\2\2\u0695\u0693\3\2\2")
        buf.write(u"\2\u0696\u069c\5@!\2\u0697\u0698\5\u0132\u009a\2\u0698")
        buf.write(u"\u0699\5@!\2\u0699\u069b\3\2\2\2\u069a\u0697\3\2\2\2")
        buf.write(u"\u069b\u069e\3\2\2\2\u069c\u069a\3\2\2\2\u069c\u069d")
        buf.write(u"\3\2\2\2\u069d\u00f1\3\2\2\2\u069e\u069c\3\2\2\2\u069f")
        buf.write(u"\u06a5\5P)\2\u06a0\u06a1\5\u0132\u009a\2\u06a1\u06a2")
        buf.write(u"\5P)\2\u06a2\u06a4\3\2\2\2\u06a3\u06a0\3\2\2\2\u06a4")
        buf.write(u"\u06a7\3\2\2\2\u06a5\u06a3\3\2\2\2\u06a5\u06a6\3\2\2")
        buf.write(u"\2\u06a6\u00f3\3\2\2\2\u06a7\u06a5\3\2\2\2\u06a8\u06a9")
        buf.write(u"\7\24\2\2\u06a9\u06aa\5\u00f6|\2\u06aa\u06ab\7\20\2\2")
        buf.write(u"\u06ab\u06ac\5\u00f6|\2\u06ac\u06ad\7\25\2\2\u06ad\u06b7")
        buf.write(u"\3\2\2\2\u06ae\u06af\7\24\2\2\u06af\u06b0\5\u00f8}\2")
        buf.write(u"\u06b0\u06b1\7\25\2\2\u06b1\u06b7\3\2\2\2\u06b2\u06b3")
        buf.write(u"\7&\2\2\u06b3\u06b4\5\u00f8}\2\u06b4\u06b5\7$\2\2\u06b5")
        buf.write(u"\u06b7\3\2\2\2\u06b6\u06a8\3\2\2\2\u06b6\u06ae\3\2\2")
        buf.write(u"\2\u06b6\u06b2\3\2\2\2\u06b7\u00f5\3\2\2\2\u06b8\u06c7")
        buf.write(u"\7\u009c\2\2\u06b9\u06c7\7\u009d\2\2\u06ba\u06c7\7\u00a5")
        buf.write(u"\2\2\u06bb\u06c7\7\u00a6\2\2\u06bc\u06c7\7\u009b\2\2")
        buf.write(u"\u06bd\u06c7\7\u00aa\2\2\u06be\u06c7\7\u00a9\2\2\u06bf")
        buf.write(u"\u06c7\7\u00a3\2\2\u06c0\u06c7\7\u00a7\2\2\u06c1\u06c7")
        buf.write(u"\7\u00a8\2\2\u06c2\u06c7\7\u009a\2\2\u06c3\u06c7\7\u00ab")
        buf.write(u"\2\2\u06c4\u06c7\7\u00a4\2\2\u06c5\u06c7\5\u0084C\2\u06c6")
        buf.write(u"\u06b8\3\2\2\2\u06c6\u06b9\3\2\2\2\u06c6\u06ba\3\2\2")
        buf.write(u"\2\u06c6\u06bb\3\2\2\2\u06c6\u06bc\3\2\2\2\u06c6\u06bd")
        buf.write(u"\3\2\2\2\u06c6\u06be\3\2\2\2\u06c6\u06bf\3\2\2\2\u06c6")
        buf.write(u"\u06c0\3\2\2\2\u06c6\u06c1\3\2\2\2\u06c6\u06c2\3\2\2")
        buf.write(u"\2\u06c6\u06c3\3\2\2\2\u06c6\u06c4\3\2\2\2\u06c6\u06c5")
        buf.write(u"\3\2\2\2\u06c7\u00f7\3\2\2\2\u06c8\u06cd\5\u00f6|\2\u06c9")
        buf.write(u"\u06ca\7\17\2\2\u06ca\u06cc\5\u00f6|\2\u06cb\u06c9\3")
        buf.write(u"\2\2\2\u06cc\u06cf\3\2\2\2\u06cd\u06cb\3\2\2\2\u06cd")
        buf.write(u"\u06ce\3\2\2\2\u06ce\u00f9\3\2\2\2\u06cf\u06cd\3\2\2")
        buf.write(u"\2\u06d0\u06d5\5\u00fe\u0080\2\u06d1\u06d5\5\u0100\u0081")
        buf.write(u"\2\u06d2\u06d5\5\u00b2Z\2\u06d3\u06d5\5\u00fc\177\2\u06d4")
        buf.write(u"\u06d0\3\2\2\2\u06d4\u06d1\3\2\2\2\u06d4\u06d2\3\2\2")
        buf.write(u"\2\u06d4\u06d3\3\2\2\2\u06d5\u00fb\3\2\2\2\u06d6\u06d7")
        buf.write(u"\t\4\2\2\u06d7\u00fd\3\2\2\2\u06d8\u06d9\7\22\2\2\u06d9")
        buf.write(u"\u06da\5^\60\2\u06da\u06db\7\23\2\2\u06db\u00ff\3\2\2")
        buf.write(u"\2\u06dc\u06df\5\u00f6|\2\u06dd\u06df\5\u0102\u0082\2")
        buf.write(u"\u06de\u06dc\3\2\2\2\u06de\u06dd\3\2\2\2\u06df\u0101")
        buf.write(u"\3\2\2\2\u06e0\u06e6\5\u009eP\2\u06e1\u06e6\5\u0098M")
        buf.write(u"\2\u06e2\u06e6\5\u009aN\2\u06e3\u06e6\5\u0106\u0084\2")
        buf.write(u"\u06e4\u06e6\5\u0104\u0083\2\u06e5\u06e0\3\2\2\2\u06e5")
        buf.write(u"\u06e1\3\2\2\2\u06e5\u06e2\3\2\2\2\u06e5\u06e3\3\2\2")
        buf.write(u"\2\u06e5\u06e4\3\2\2\2\u06e6\u0103\3\2\2\2\u06e7\u06e9")
        buf.write(u"\7s\2\2\u06e8\u06e7\3\2\2\2\u06e8\u06e9\3\2\2\2\u06e9")
        buf.write(u"\u06ea\3\2\2\2\u06ea\u06ec\7\22\2\2\u06eb\u06ed\5\u0108")
        buf.write(u"\u0085\2\u06ec\u06eb\3\2\2\2\u06ec\u06ed\3\2\2\2\u06ed")
        buf.write(u"\u06ee\3\2\2\2\u06ee\u06ef\7\23\2\2\u06ef\u0105\3\2\2")
        buf.write(u"\2\u06f0\u06f2\7s\2\2\u06f1\u06f0\3\2\2\2\u06f1\u06f2")
        buf.write(u"\3\2\2\2\u06f2\u06f3\3\2\2\2\u06f3\u06f5\7\26\2\2\u06f4")
        buf.write(u"\u06f6\5\u010a\u0086\2\u06f5\u06f4\3\2\2\2\u06f5\u06f6")
        buf.write(u"\3\2\2\2\u06f6\u06f7\3\2\2\2\u06f7\u06f8\7\27\2\2\u06f8")
        buf.write(u"\u0107\3\2\2\2\u06f9\u06fa\5^\60\2\u06fa\u0703\7\17\2")
        buf.write(u"\2\u06fb\u0700\5^\60\2\u06fc\u06fd\7\17\2\2\u06fd\u06ff")
        buf.write(u"\5^\60\2\u06fe\u06fc\3\2\2\2\u06ff\u0702\3\2\2\2\u0700")
        buf.write(u"\u06fe\3\2\2\2\u0700\u0701\3\2\2\2\u0701\u0704\3\2\2")
        buf.write(u"\2\u0702\u0700\3\2\2\2\u0703\u06fb\3\2\2\2\u0703\u0704")
        buf.write(u"\3\2\2\2\u0704\u0109\3\2\2\2\u0705\u070a\5\u010c\u0087")
        buf.write(u"\2\u0706\u0707\7\17\2\2\u0707\u0709\5\u010c\u0087\2\u0708")
        buf.write(u"\u0706\3\2\2\2\u0709\u070c\3\2\2\2\u070a\u0708\3\2\2")
        buf.write(u"\2\u070a\u070b\3\2\2\2\u070b\u010b\3\2\2\2\u070c\u070a")
        buf.write(u"\3\2\2\2\u070d\u070e\5^\60\2\u070e\u070f\7\r\2\2\u070f")
        buf.write(u"\u0710\5^\60\2\u0710\u010d\3\2\2\2\u0711\u0712\5^\60")
        buf.write(u"\2\u0712\u0713\7\r\2\2\u0713\u0714\5^\60\2\u0714\u071b")
        buf.write(u"\3\2\2\2\u0715\u0716\5^\60\2\u0716\u0717\7\r\2\2\u0717")
        buf.write(u"\u071b\3\2\2\2\u0718\u0719\7\r\2\2\u0719\u071b\5^\60")
        buf.write(u"\2\u071a\u0711\3\2\2\2\u071a\u0715\3\2\2\2\u071a\u0718")
        buf.write(u"\3\2\2\2\u071b\u010f\3\2\2\2\u071c\u071d\5\u00b4[\2\u071d")
        buf.write(u"\u071e\5\u0126\u0094\2\u071e\u071f\5^\60\2\u071f\u0111")
        buf.write(u"\3\2\2\2\u0720\u0721\b\u008a\1\2\u0721\u0722\5\u00b4")
        buf.write(u"[\2\u0722\u0727\3\2\2\2\u0723\u0724\f\3\2\2\u0724\u0726")
        buf.write(u"\5\u0080A\2\u0725\u0723\3\2\2\2\u0726\u0729\3\2\2\2\u0727")
        buf.write(u"\u0725\3\2\2\2\u0727\u0728\3\2\2\2\u0728\u0113\3\2\2")
        buf.write(u"\2\u0729\u0727\3\2\2\2\u072a\u072b\6\u008b,\3\u072b\u072c")
        buf.write(u"\7\u00a0\2\2\u072c\u072f\5\u00c6d\2\u072d\u072f\5^\60")
        buf.write(u"\2\u072e\u072a\3\2\2\2\u072e\u072d\3\2\2\2\u072f\u0115")
        buf.write(u"\3\2\2\2\u0730\u0735\5\u0118\u008d\2\u0731\u0732\7\17")
        buf.write(u"\2\2\u0732\u0734\5\u0118\u008d\2\u0733\u0731\3\2\2\2")
        buf.write(u"\u0734\u0737\3\2\2\2\u0735\u0733\3\2\2\2\u0735\u0736")
        buf.write(u"\3\2\2\2\u0736\u0117\3\2\2\2\u0737\u0735\3\2\2\2\u0738")
        buf.write(u"\u073d\5\u00b4[\2\u0739\u073a\7\21\2\2\u073a\u073c\5")
        buf.write(u"\u00b4[\2\u073b\u0739\3\2\2\2\u073c\u073f\3\2\2\2\u073d")
        buf.write(u"\u073b\3\2\2\2\u073d\u073e\3\2\2\2\u073e\u0741\3\2\2")
        buf.write(u"\2\u073f\u073d\3\2\2\2\u0740\u0742\t\5\2\2\u0741\u0740")
        buf.write(u"\3\2\2\2\u0741\u0742\3\2\2\2\u0742\u0119\3\2\2\2\u0743")
        buf.write(u"\u074a\7\36\2\2\u0744\u074a\7\37\2\2\u0745\u074a\5\u0128")
        buf.write(u"\u0095\2\u0746\u074a\5\u012a\u0096\2\u0747\u074a\5\u012c")
        buf.write(u"\u0097\2\u0748\u074a\5\u012e\u0098\2\u0749\u0743\3\2")
        buf.write(u"\2\2\u0749\u0744\3\2\2\2\u0749\u0745\3\2\2\2\u0749\u0746")
        buf.write(u"\3\2\2\2\u0749\u0747\3\2\2\2\u0749\u0748\3\2\2\2\u074a")
        buf.write(u"\u011b\3\2\2\2\u074b\u074c\7\u00a0\2\2\u074c\u074d\6")
        buf.write(u"\u008f-\3\u074d\u011d\3\2\2\2\u074e\u074f\7\u00a0\2\2")
        buf.write(u"\u074f\u0750\6\u0090.\3\u0750\u011f\3\2\2\2\u0751\u0752")
        buf.write(u"\7\u00a0\2\2\u0752\u0753\6\u0091/\3\u0753\u0121\3\2\2")
        buf.write(u"\2\u0754\u0755\7\u00a0\2\2\u0755\u0756\6\u0092\60\3\u0756")
        buf.write(u"\u0123\3\2\2\2\u0757\u0758\7\u00a0\2\2\u0758\u0759\6")
        buf.write(u"\u0093\61\3\u0759\u0125\3\2\2\2\u075a\u075b\7)\2\2\u075b")
        buf.write(u"\u0127\3\2\2\2\u075c\u075d\7 \2\2\u075d\u0129\3\2\2\2")
        buf.write(u"\u075e\u075f\7!\2\2\u075f\u012b\3\2\2\2\u0760\u0761\7")
        buf.write(u"\"\2\2\u0761\u012d\3\2\2\2\u0762\u0763\t\6\2\2\u0763")
        buf.write(u"\u012f\3\2\2\2\u0764\u0765\3\2\2\2\u0765\u0131\3\2\2")
        buf.write(u"\2\u0766\u0767\3\2\2\2\u0767\u0133\3\2\2\2\u0768\u0769")
        buf.write(u"\7\u0085\2\2\u0769\u076a\5\u0136\u009c\2\u076a\u076b")
        buf.write(u"\7\16\2\2\u076b\u0770\3\2\2\2\u076c\u076d\5\u0136\u009c")
        buf.write(u"\2\u076d\u076e\7\16\2\2\u076e\u0770\3\2\2\2\u076f\u0768")
        buf.write(u"\3\2\2\2\u076f\u076c\3\2\2\2\u0770\u0135\3\2\2\2\u0771")
        buf.write(u"\u0772\b\u009c\1\2\u0772\u0773\5\u0138\u009d\2\u0773")
        buf.write(u"\u0778\3\2\2\2\u0774\u0775\f\3\2\2\u0775\u0777\5\u013e")
        buf.write(u"\u00a0\2\u0776\u0774\3\2\2\2\u0777\u077a\3\2\2\2\u0778")
        buf.write(u"\u0776\3\2\2\2\u0778\u0779\3\2\2\2\u0779\u0137\3\2\2")
        buf.write(u"\2\u077a\u0778\3\2\2\2\u077b\u0783\5\u013a\u009e\2\u077c")
        buf.write(u"\u0783\5\u013c\u009f\2\u077d\u0783\5\u0146\u00a4\2\u077e")
        buf.write(u"\u0783\5\u0148\u00a5\2\u077f\u0783\5\u014a\u00a6\2\u0780")
        buf.write(u"\u0783\5\u0140\u00a1\2\u0781\u0783\5\u0144\u00a3\2\u0782")
        buf.write(u"\u077b\3\2\2\2\u0782\u077c\3\2\2\2\u0782\u077d\3\2\2")
        buf.write(u"\2\u0782\u077e\3\2\2\2\u0782\u077f\3\2\2\2\u0782\u0780")
        buf.write(u"\3\2\2\2\u0782\u0781\3\2\2\2\u0783\u0139\3\2\2\2\u0784")
        buf.write(u"\u0785\5\u00fc\177\2\u0785\u013b\3\2\2\2\u0786\u0787")
        buf.write(u"\5\u011c\u008f\2\u0787\u0788\5\u0140\u00a1\2\u0788\u013d")
        buf.write(u"\3\2\2\2\u0789\u078a\7\21\2\2\u078a\u078f\5\u0140\u00a1")
        buf.write(u"\2\u078b\u078c\7\21\2\2\u078c\u078f\5\u014c\u00a7\2\u078d")
        buf.write(u"\u078f\5\u0144\u00a3\2\u078e\u0789\3\2\2\2\u078e\u078b")
        buf.write(u"\3\2\2\2\u078e\u078d\3\2\2\2\u078f\u013f\3\2\2\2\u0790")
        buf.write(u"\u0791\5\u014c\u00a7\2\u0791\u0793\7\22\2\2\u0792\u0794")
        buf.write(u"\5\u0142\u00a2\2\u0793\u0792\3\2\2\2\u0793\u0794\3\2")
        buf.write(u"\2\2\u0794\u0795\3\2\2\2\u0795\u0796\7\23\2\2\u0796\u0141")
        buf.write(u"\3\2\2\2\u0797\u0798\b\u00a2\1\2\u0798\u0799\5\u0136")
        buf.write(u"\u009c\2\u0799\u079f\3\2\2\2\u079a\u079b\f\3\2\2\u079b")
        buf.write(u"\u079c\7\17\2\2\u079c\u079e\5\u0136\u009c\2\u079d\u079a")
        buf.write(u"\3\2\2\2\u079e\u07a1\3\2\2\2\u079f\u079d\3\2\2\2\u079f")
        buf.write(u"\u07a0\3\2\2\2\u07a0\u0143\3\2\2\2\u07a1\u079f\3\2\2")
        buf.write(u"\2\u07a2\u07a3\7\24\2\2\u07a3\u07a4\5\u0136\u009c\2\u07a4")
        buf.write(u"\u07a5\7\25\2\2\u07a5\u0145\3\2\2\2\u07a6\u07a7\7\22")
        buf.write(u"\2\2\u07a7\u07a8\5\u0136\u009c\2\u07a8\u07a9\7\23\2\2")
        buf.write(u"\u07a9\u0147\3\2\2\2\u07aa\u07ab\5\u014c\u00a7\2\u07ab")
        buf.write(u"\u0149\3\2\2\2\u07ac\u07b2\7\u00a5\2\2\u07ad\u07b2\7")
        buf.write(u"\u00a7\2\2\u07ae\u07b2\7\u00a3\2\2\u07af\u07b2\7\u009a")
        buf.write(u"\2\2\u07b0\u07b2\7\u009b\2\2\u07b1\u07ac\3\2\2\2\u07b1")
        buf.write(u"\u07ad\3\2\2\2\u07b1\u07ae\3\2\2\2\u07b1\u07af\3\2\2")
        buf.write(u"\2\u07b1\u07b0\3\2\2\2\u07b2\u014b\3\2\2\2\u07b3\u07b4")
        buf.write(u"\t\7\2\2\u07b4\u014d\3\2\2\2\u07b5\u07b6\7\u0085\2\2")
        buf.write(u"\u07b6\u07b9\5\u0150\u00a9\2\u07b7\u07b9\5\u0150\u00a9")
        buf.write(u"\2\u07b8\u07b5\3\2\2\2\u07b8\u07b7\3\2\2\2\u07b9\u014f")
        buf.write(u"\3\2\2\2\u07ba\u07bb\b\u00a9\1\2\u07bb\u07bc\5\u0152")
        buf.write(u"\u00aa\2\u07bc\u07c1\3\2\2\2\u07bd\u07be\f\3\2\2\u07be")
        buf.write(u"\u07c0\5\u0154\u00ab\2\u07bf\u07bd\3\2\2\2\u07c0\u07c3")
        buf.write(u"\3\2\2\2\u07c1\u07bf\3\2\2\2\u07c1\u07c2\3\2\2\2\u07c2")
        buf.write(u"\u0151\3\2\2\2\u07c3\u07c1\3\2\2\2\u07c4\u07c9\5\u015e")
        buf.write(u"\u00b0\2\u07c5\u07c9\5\u0160\u00b1\2\u07c6\u07c9\5\u0162")
        buf.write(u"\u00b2\2\u07c7\u07c9\5\u0156\u00ac\2\u07c8\u07c4\3\2")
        buf.write(u"\2\2\u07c8\u07c5\3\2\2\2\u07c8\u07c6\3\2\2\2\u07c8\u07c7")
        buf.write(u"\3\2\2\2\u07c9\u0153\3\2\2\2\u07ca\u07cb\7\21\2\2\u07cb")
        buf.write(u"\u07d1\5\u0156\u00ac\2\u07cc\u07cd\7\24\2\2\u07cd\u07ce")
        buf.write(u"\5\u0150\u00a9\2\u07ce\u07cf\7\25\2\2\u07cf\u07d1\3\2")
        buf.write(u"\2\2\u07d0\u07ca\3\2\2\2\u07d0\u07cc\3\2\2\2\u07d1\u0155")
        buf.write(u"\3\2\2\2\u07d2\u07d3\5\u0164\u00b3\2\u07d3\u07d5\7\22")
        buf.write(u"\2\2\u07d4\u07d6\5\u0158\u00ad\2\u07d5\u07d4\3\2\2\2")
        buf.write(u"\u07d5\u07d6\3\2\2\2\u07d6\u07d7\3\2\2\2\u07d7\u07d8")
        buf.write(u"\7\23\2\2\u07d8\u0157\3\2\2\2\u07d9\u07e0\5\u015a\u00ae")
        buf.write(u"\2\u07da\u07e0\5\u015c\u00af\2\u07db\u07dc\5\u015a\u00ae")
        buf.write(u"\2\u07dc\u07dd\7\17\2\2\u07dd\u07de\5\u015c\u00af\2\u07de")
        buf.write(u"\u07e0\3\2\2\2\u07df\u07d9\3\2\2\2\u07df\u07da\3\2\2")
        buf.write(u"\2\u07df\u07db\3\2\2\2\u07e0\u0159\3\2\2\2\u07e1\u07e2")
        buf.write(u"\b\u00ae\1\2\u07e2\u07e3\5\u0150\u00a9\2\u07e3\u07e9")
        buf.write(u"\3\2\2\2\u07e4\u07e5\f\3\2\2\u07e5\u07e6\7\17\2\2\u07e6")
        buf.write(u"\u07e8\5\u0150\u00a9\2\u07e7\u07e4\3\2\2\2\u07e8\u07eb")
        buf.write(u"\3\2\2\2\u07e9\u07e7\3\2\2\2\u07e9\u07ea\3\2\2\2\u07ea")
        buf.write(u"\u015b\3\2\2\2\u07eb\u07e9\3\2\2\2\u07ec\u07ed\b\u00af")
        buf.write(u"\1\2\u07ed\u07ee\5\u0164\u00b3\2\u07ee\u07ef\7)\2\2\u07ef")
        buf.write(u"\u07f0\5\u0150\u00a9\2\u07f0\u07f9\3\2\2\2\u07f1\u07f2")
        buf.write(u"\f\3\2\2\u07f2\u07f3\7\17\2\2\u07f3\u07f4\5\u0164\u00b3")
        buf.write(u"\2\u07f4\u07f5\7)\2\2\u07f5\u07f6\5\u0150\u00a9\2\u07f6")
        buf.write(u"\u07f8\3\2\2\2\u07f7\u07f1\3\2\2\2\u07f8\u07fb\3\2\2")
        buf.write(u"\2\u07f9\u07f7\3\2\2\2\u07f9\u07fa\3\2\2\2\u07fa\u015d")
        buf.write(u"\3\2\2\2\u07fb\u07f9\3\2\2\2\u07fc\u07fd\7\22\2\2\u07fd")
        buf.write(u"\u07fe\5\u0150\u00a9\2\u07fe\u07ff\7\23\2\2\u07ff\u015f")
        buf.write(u"\3\2\2\2\u0800\u0801\b\u00b1\1\2\u0801\u0804\7\u00a2")
        buf.write(u"\2\2\u0802\u0804\5\u0164\u00b3\2\u0803\u0800\3\2\2\2")
        buf.write(u"\u0803\u0802\3\2\2\2\u0804\u080a\3\2\2\2\u0805\u0806")
        buf.write(u"\f\3\2\2\u0806\u0807\7\21\2\2\u0807\u0809\5\u0164\u00b3")
        buf.write(u"\2\u0808\u0805\3\2\2\2\u0809\u080c\3\2\2\2\u080a\u0808")
        buf.write(u"\3\2\2\2\u080a\u080b\3\2\2\2\u080b\u0161\3\2\2\2\u080c")
        buf.write(u"\u080a\3\2\2\2\u080d\u0813\7\u00a5\2\2\u080e\u0813\7")
        buf.write(u"\u00a7\2\2\u080f\u0813\7\u00a3\2\2\u0810\u0813\7\u009a")
        buf.write(u"\2\2\u0811\u0813\7\u009b\2\2\u0812\u080d\3\2\2\2\u0812")
        buf.write(u"\u080e\3\2\2\2\u0812\u080f\3\2\2\2\u0812\u0810\3\2\2")
        buf.write(u"\2\u0812\u0811\3\2\2\2\u0813\u0163\3\2\2\2\u0814\u0815")
        buf.write(u"\t\b\2\2\u0815\u0165\3\2\2\2\u0816\u0817\7\u0085\2\2")
        buf.write(u"\u0817\u0818\5\u0168\u00b5\2\u0818\u0819\7\16\2\2\u0819")
        buf.write(u"\u081e\3\2\2\2\u081a\u081b\5\u0168\u00b5\2\u081b\u081c")
        buf.write(u"\7\16\2\2\u081c\u081e\3\2\2\2\u081d\u0816\3\2\2\2\u081d")
        buf.write(u"\u081a\3\2\2\2\u081e\u0167\3\2\2\2\u081f\u0820\b\u00b5")
        buf.write(u"\1\2\u0820\u0821\5\u016a\u00b6\2\u0821\u0826\3\2\2\2")
        buf.write(u"\u0822\u0823\f\3\2\2\u0823\u0825\5\u0170\u00b9\2\u0824")
        buf.write(u"\u0822\3\2\2\2\u0825\u0828\3\2\2\2\u0826\u0824\3\2\2")
        buf.write(u"\2\u0826\u0827\3\2\2\2\u0827\u0169\3\2\2\2\u0828\u0826")
        buf.write(u"\3\2\2\2\u0829\u082f\5\u016c\u00b7\2\u082a\u082f\5\u016e")
        buf.write(u"\u00b8\2\u082b\u082f\5\u0178\u00bd\2\u082c\u082f\5\u017a")
        buf.write(u"\u00be\2\u082d\u082f\5\u017e\u00c0\2\u082e\u0829\3\2")
        buf.write(u"\2\2\u082e\u082a\3\2\2\2\u082e\u082b\3\2\2\2\u082e\u082c")
        buf.write(u"\3\2\2\2\u082e\u082d\3\2\2\2\u082f\u016b\3\2\2\2\u0830")
        buf.write(u"\u0831\5\u00fc\177\2\u0831\u016d\3\2\2\2\u0832\u0833")
        buf.write(u"\5\u011c\u008f\2\u0833\u0834\5\u0172\u00ba\2\u0834\u016f")
        buf.write(u"\3\2\2\2\u0835\u0836\7\21\2\2\u0836\u0839\5\u0172\u00ba")
        buf.write(u"\2\u0837\u0839\5\u0176\u00bc\2\u0838\u0835\3\2\2\2\u0838")
        buf.write(u"\u0837\3\2\2\2\u0839\u0171\3\2\2\2\u083a\u083b\5\u0180")
        buf.write(u"\u00c1\2\u083b\u083d\7\22\2\2\u083c\u083e\5\u0174\u00bb")
        buf.write(u"\2\u083d\u083c\3\2\2\2\u083d\u083e\3\2\2\2\u083e\u083f")
        buf.write(u"\3\2\2\2\u083f\u0840\7\23\2\2\u0840\u0173\3\2\2\2\u0841")
        buf.write(u"\u0842\b\u00bb\1\2\u0842\u0843\5\u0168\u00b5\2\u0843")
        buf.write(u"\u0849\3\2\2\2\u0844\u0845\f\3\2\2\u0845\u0846\7\17\2")
        buf.write(u"\2\u0846\u0848\5\u0168\u00b5\2\u0847\u0844\3\2\2\2\u0848")
        buf.write(u"\u084b\3\2\2\2\u0849\u0847\3\2\2\2\u0849\u084a\3\2\2")
        buf.write(u"\2\u084a\u0175\3\2\2\2\u084b\u0849\3\2\2\2\u084c\u084d")
        buf.write(u"\7\24\2\2\u084d\u084e\5\u0168\u00b5\2\u084e\u084f\7\25")
        buf.write(u"\2\2\u084f\u0177\3\2\2\2\u0850\u0851\7\22\2\2\u0851\u0852")
        buf.write(u"\5\u0168\u00b5\2\u0852\u0853\7\23\2\2\u0853\u0179\3\2")
        buf.write(u"\2\2\u0854\u0855\b\u00be\1\2\u0855\u0856\5\u0180\u00c1")
        buf.write(u"\2\u0856\u085c\3\2\2\2\u0857\u0858\f\3\2\2\u0858\u0859")
        buf.write(u"\7\21\2\2\u0859\u085b\5\u0180\u00c1\2\u085a\u0857\3\2")
        buf.write(u"\2\2\u085b\u085e\3\2\2\2\u085c\u085a\3\2\2\2\u085c\u085d")
        buf.write(u"\3\2\2\2\u085d\u017b\3\2\2\2\u085e\u085c\3\2\2\2\u085f")
        buf.write(u"\u0860\b\u00bf\1\2\u0860\u0861\5\u017a\u00be\2\u0861")
        buf.write(u"\u0866\3\2\2\2\u0862\u0863\f\3\2\2\u0863\u0865\7\u00a2")
        buf.write(u"\2\2\u0864\u0862\3\2\2\2\u0865\u0868\3\2\2\2\u0866\u0864")
        buf.write(u"\3\2\2\2\u0866\u0867\3\2\2\2\u0867\u017d\3\2\2\2\u0868")
        buf.write(u"\u0866\3\2\2\2\u0869\u086f\7\u00a5\2\2\u086a\u086f\7")
        buf.write(u"\u00a7\2\2\u086b\u086f\7\u00a3\2\2\u086c\u086f\7\u009a")
        buf.write(u"\2\2\u086d\u086f\7\u009b\2\2\u086e\u0869\3\2\2\2\u086e")
        buf.write(u"\u086a\3\2\2\2\u086e\u086b\3\2\2\2\u086e\u086c\3\2\2")
        buf.write(u"\2\u086e\u086d\3\2\2\2\u086f\u017f\3\2\2\2\u0870\u0871")
        buf.write(u"\t\t\2\2\u0871\u0181\3\2\2\2\u0872\u0873\7\u0085\2\2")
        buf.write(u"\u0873\u0874\5\u0184\u00c3\2\u0874\u0875\7\16\2\2\u0875")
        buf.write(u"\u087a\3\2\2\2\u0876\u0877\5\u0184\u00c3\2\u0877\u0878")
        buf.write(u"\7\16\2\2\u0878\u087a\3\2\2\2\u0879\u0872\3\2\2\2\u0879")
        buf.write(u"\u0876\3\2\2\2\u087a\u0183\3\2\2\2\u087b\u087c\b\u00c3")
        buf.write(u"\1\2\u087c\u087d\5\u0186\u00c4\2\u087d\u0882\3\2\2\2")
        buf.write(u"\u087e\u087f\f\3\2\2\u087f\u0881\5\u018c\u00c7\2\u0880")
        buf.write(u"\u087e\3\2\2\2\u0881\u0884\3\2\2\2\u0882\u0880\3\2\2")
        buf.write(u"\2\u0882\u0883\3\2\2\2\u0883\u0185\3\2\2\2\u0884\u0882")
        buf.write(u"\3\2\2\2\u0885\u088b\5\u0188\u00c5\2\u0886\u088b\5\u018a")
        buf.write(u"\u00c6\2\u0887\u088b\5\u0194\u00cb\2\u0888\u088b\5\u0196")
        buf.write(u"\u00cc\2\u0889\u088b\5\u0198\u00cd\2\u088a\u0885\3\2")
        buf.write(u"\2\2\u088a\u0886\3\2\2\2\u088a\u0887\3\2\2\2\u088a\u0888")
        buf.write(u"\3\2\2\2\u088a\u0889\3\2\2\2\u088b\u0187\3\2\2\2\u088c")
        buf.write(u"\u088d\5\u00fc\177\2\u088d\u0189\3\2\2\2\u088e\u088f")
        buf.write(u"\5\u011c\u008f\2\u088f\u0890\5\u018e\u00c8\2\u0890\u018b")
        buf.write(u"\3\2\2\2\u0891\u0892\7\21\2\2\u0892\u0895\5\u018e\u00c8")
        buf.write(u"\2\u0893\u0895\5\u0192\u00ca\2\u0894\u0891\3\2\2\2\u0894")
        buf.write(u"\u0893\3\2\2\2\u0895\u018d\3\2\2\2\u0896\u0897\5\u019a")
        buf.write(u"\u00ce\2\u0897\u0899\7\22\2\2\u0898\u089a\5\u0190\u00c9")
        buf.write(u"\2\u0899\u0898\3\2\2\2\u0899\u089a\3\2\2\2\u089a\u089b")
        buf.write(u"\3\2\2\2\u089b\u089c\7\23\2\2\u089c\u018f\3\2\2\2\u089d")
        buf.write(u"\u089e\b\u00c9\1\2\u089e\u089f\5\u0184\u00c3\2\u089f")
        buf.write(u"\u08a5\3\2\2\2\u08a0\u08a1\f\3\2\2\u08a1\u08a2\7\17\2")
        buf.write(u"\2\u08a2\u08a4\5\u0184\u00c3\2\u08a3\u08a0\3\2\2\2\u08a4")
        buf.write(u"\u08a7\3\2\2\2\u08a5\u08a3\3\2\2\2\u08a5\u08a6\3\2\2")
        buf.write(u"\2\u08a6\u0191\3\2\2\2\u08a7\u08a5\3\2\2\2\u08a8\u08a9")
        buf.write(u"\7\24\2\2\u08a9\u08aa\5\u0184\u00c3\2\u08aa\u08ab\7\25")
        buf.write(u"\2\2\u08ab\u0193\3\2\2\2\u08ac\u08ad\7\22\2\2\u08ad\u08ae")
        buf.write(u"\5\u0184\u00c3\2\u08ae\u08af\7\23\2\2\u08af\u0195\3\2")
        buf.write(u"\2\2\u08b0\u08b1\b\u00cc\1\2\u08b1\u08b4\7\u00a2\2\2")
        buf.write(u"\u08b2\u08b4\5\u019a\u00ce\2\u08b3\u08b0\3\2\2\2\u08b3")
        buf.write(u"\u08b2\3\2\2\2\u08b4\u08ba\3\2\2\2\u08b5\u08b6\f\3\2")
        buf.write(u"\2\u08b6\u08b7\7\21\2\2\u08b7\u08b9\5\u019a\u00ce\2\u08b8")
        buf.write(u"\u08b5\3\2\2\2\u08b9\u08bc\3\2\2\2\u08ba\u08b8\3\2\2")
        buf.write(u"\2\u08ba\u08bb\3\2\2\2\u08bb\u0197\3\2\2\2\u08bc\u08ba")
        buf.write(u"\3\2\2\2\u08bd\u08c3\7\u00a5\2\2\u08be\u08c3\7\u00a7")
        buf.write(u"\2\2\u08bf\u08c3\7\u00a3\2\2\u08c0\u08c3\7\u009a\2\2")
        buf.write(u"\u08c1\u08c3\7\u009b\2\2\u08c2\u08bd\3\2\2\2\u08c2\u08be")
        buf.write(u"\3\2\2\2\u08c2\u08bf\3\2\2\2\u08c2\u08c0\3\2\2\2\u08c2")
        buf.write(u"\u08c1\3\2\2\2\u08c3\u0199\3\2\2\2\u08c4\u08c5\t\n\2")
        buf.write(u"\2\u08c5\u019b\3\2\2\2\u00c8\u01a3\u01a7\u01c2\u01c9")
        buf.write(u"\u01d1\u01d3\u01d8\u01e0\u01e4\u01ee\u01fa\u0200\u0203")
        buf.write(u"\u0206\u020f\u0217\u021c\u0222\u022a\u022f\u0235\u0240")
        buf.write(u"\u0245\u024a\u0253\u0258\u026c\u0271\u0277\u027d\u0283")
        buf.write(u"\u0288\u028d\u0290\u0296\u02ad\u02b7\u02bc\u02c3\u02c5")
        buf.write(u"\u02dc\u02fa\u0311\u0313\u031b\u0322\u0324\u032c\u0336")
        buf.write(u"\u034b\u034f\u0363\u0370\u0374\u037c\u037f\u0384\u0387")
        buf.write(u"\u038f\u039a\u039e\u03a5\u03ac\u03b5\u03be\u03c7\u03e0")
        buf.write(u"\u044d\u044f\u045f\u046a\u0474\u0497\u04a2\u04a7\u04b1")
        buf.write(u"\u04b8\u04c0\u04c2\u04c6\u04cf\u04dd\u04e2\u04eb\u04f2")
        buf.write(u"\u0504\u050e\u0519\u0521\u0529\u052f\u0537\u0540\u0548")
        buf.write(u"\u0555\u0558\u055c\u0561\u0565\u056e\u0583\u058d\u058f")
        buf.write(u"\u0594\u05a4\u05a9\u05b2\u05b9\u05be\u05c3\u05d2\u05d7")
        buf.write(u"\u05da\u05de\u05e3\u05ea\u05f5\u05f7\u0600\u0608\u0610")
        buf.write(u"\u0616\u0622\u0626\u0630\u0635\u063b\u0642\u0647\u064e")
        buf.write(u"\u0656\u065d\u0667\u0674\u0678\u067b\u067f\u0682\u068a")
        buf.write(u"\u0693\u069c\u06a5\u06b6\u06c6\u06cd\u06d4\u06de\u06e5")
        buf.write(u"\u06e8\u06ec\u06f1\u06f5\u0700\u0703\u070a\u071a\u0727")
        buf.write(u"\u072e\u0735\u073d\u0741\u0749\u076f\u0778\u0782\u078e")
        buf.write(u"\u0793\u079f\u07b1\u07b8\u07c1\u07c8\u07d0\u07d5\u07df")
        buf.write(u"\u07e9\u07f9\u0803\u080a\u0812\u081d\u0826\u082e\u0838")
        buf.write(u"\u083d\u0849\u085c\u0866\u086e\u0879\u0882\u088a\u0894")
        buf.write(u"\u0899\u08a5\u08b3\u08ba\u08c2")
        return buf.getvalue()
		

class OParser ( AbstractParser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"' '", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
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

    symbolicNames = [ u"<INVALID>", u"SPACE", u"WS", u"LF", u"COMMENT", 
                      u"JAVA", u"CSHARP", u"PYTHON2", u"PYTHON3", u"JAVASCRIPT", 
                      u"SWIFT", u"COLON", u"SEMI", u"COMMA", u"RANGE", u"DOT", 
                      u"LPAR", u"RPAR", u"LBRAK", u"RBRAK", u"LCURL", u"RCURL", 
                      u"QMARK", u"XMARK", u"AMP", u"AMP2", u"PIPE", u"PIPE2", 
                      u"PLUS", u"MINUS", u"STAR", u"SLASH", u"BSLASH", u"PERCENT", 
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
    RULE_read_expression = 53
    RULE_write_statement = 54
    RULE_filtered_list_expression = 55
    RULE_fetch_store_expression = 56
    RULE_sorted_expression = 57
    RULE_selector_expression = 58
    RULE_constructor_expression = 59
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
    RULE_order_by_list = 138
    RULE_order_by = 139
    RULE_operator = 140
    RULE_new_token = 141
    RULE_key_token = 142
    RULE_module_token = 143
    RULE_value_token = 144
    RULE_symbols_token = 145
    RULE_assign = 146
    RULE_multiply = 147
    RULE_divide = 148
    RULE_idivide = 149
    RULE_modulo = 150
    RULE_lfs = 151
    RULE_lfp = 152
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
                   u"blob_expression", u"document_expression", u"read_expression", 
                   u"write_statement", u"filtered_list_expression", u"fetch_store_expression", 
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
                   u"is_expression", u"order_by_list", u"order_by", u"operator", 
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
    METHOD_T=55
    CODE=56
    DOCUMENT=57
    BLOB=58
    IMAGE=59
    UUID=60
    ITERATOR=61
    CURSOR=62
    ABSTRACT=63
    ALL=64
    ALWAYS=65
    AND=66
    ANY=67
    AS=68
    ASC=69
    ATTR=70
    ATTRIBUTE=71
    ATTRIBUTES=72
    BINDINGS=73
    BREAK=74
    BY=75
    CASE=76
    CATCH=77
    CATEGORY=78
    CLASS=79
    CLOSE=80
    CONTAINS=81
    DEF=82
    DEFAULT=83
    DEFINE=84
    DELETE=85
    DESC=86
    DO=87
    DOING=88
    EACH=89
    ELSE=90
    ENUM=91
    ENUMERATED=92
    EXCEPT=93
    EXECUTE=94
    EXPECTING=95
    EXTENDS=96
    FETCH=97
    FILTERED=98
    FINALLY=99
    FLUSH=100
    FOR=101
    FROM=102
    GETTER=103
    IF=104
    IN=105
    INDEX=106
    INVOKE=107
    IS=108
    MATCHING=109
    METHOD=110
    METHODS=111
    MODULO=112
    MUTABLE=113
    NATIVE=114
    NONE=115
    NOT=116
    NOTHING=117
    NULL=118
    ON=119
    ONE=120
    OPEN=121
    OPERATOR=122
    OR=123
    ORDER=124
    OTHERWISE=125
    PASS=126
    RAISE=127
    READ=128
    RECEIVING=129
    RESOURCE=130
    RETURN=131
    RETURNING=132
    ROWS=133
    SELF=134
    SETTER=135
    SINGLETON=136
    SORTED=137
    STORABLE=138
    STORE=139
    SWITCH=140
    TEST=141
    THIS=142
    THROW=143
    TO=144
    TRY=145
    VERIFYING=146
    WITH=147
    WHEN=148
    WHERE=149
    WHILE=150
    WRITE=151
    BOOLEAN_LITERAL=152
    CHAR_LITERAL=153
    MIN_INTEGER=154
    MAX_INTEGER=155
    SYMBOL_IDENTIFIER=156
    TYPE_IDENTIFIER=157
    VARIABLE_IDENTIFIER=158
    NATIVE_IDENTIFIER=159
    DOLLAR_IDENTIFIER=160
    TEXT_LITERAL=161
    UUID_LITERAL=162
    INTEGER_LITERAL=163
    HEXA_LITERAL=164
    DECIMAL_LITERAL=165
    DATETIME_LITERAL=166
    TIME_LITERAL=167
    DATE_LITERAL=168
    PERIOD_LITERAL=169

    def __init__(self, input):
        super(OParser, self).__init__(input)
        self.checkVersion("4.5")
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
            if isinstance( listener, OParserListener ):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = OParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(OParser.ENUMERATED)
            self.state = 411
            self.match(OParser.CATEGORY)
            self.state = 412 
            localctx.name = self.type_identifier()
            self.state = 417
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 413
                self.match(OParser.LPAR)
                self.state = 414 
                localctx.attrs = self.attribute_identifier_list()
                self.state = 415
                self.match(OParser.RPAR)


            self.state = 421
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 419
                self.match(OParser.EXTENDS)
                self.state = 420 
                localctx.derived = self.type_identifier()


            self.state = 423
            self.match(OParser.LCURL)
            self.state = 424 
            localctx.symbols = self.category_symbol_list()
            self.state = 425
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
            if isinstance( listener, OParserListener ):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = OParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(OParser.ENUMERATED)
            self.state = 428 
            localctx.name = self.type_identifier()
            self.state = 429
            self.match(OParser.LPAR)
            self.state = 430 
            localctx.typ = self.native_type()
            self.state = 431
            self.match(OParser.RPAR)
            self.state = 432
            self.match(OParser.LCURL)
            self.state = 433 
            localctx.symbols = self.native_symbol_list()
            self.state = 434
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
            if isinstance( listener, OParserListener ):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = OParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_category_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436 
            localctx.name = self.symbol_identifier()
            self.state = 437
            self.match(OParser.LPAR)
            self.state = 438 
            localctx.args = self.argument_assignment_list(0)
            self.state = 439
            self.match(OParser.RPAR)
            self.state = 440
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = OParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442 
            localctx.name = self.symbol_identifier()
            self.state = 443
            self.match(OParser.EQ)
            self.state = 444 
            localctx.exp = self.expression(0)
            self.state = 445
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
            if isinstance( listener, OParserListener ):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = OParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 447
                self.match(OParser.STORABLE)


            self.state = 450
            self.match(OParser.ATTRIBUTE)
            self.state = 451 
            localctx.name = self.attribute_identifier()
            self.state = 452
            self.match(OParser.COLON)
            self.state = 453 
            localctx.typ = self.typedef(0)
            self.state = 455
            _la = self._input.LA(1)
            if _la==OParser.IN or _la==OParser.MATCHING:
                self.state = 454 
                localctx.match = self.attribute_constraint()


            self.state = 465
            _la = self._input.LA(1)
            if _la==OParser.WITH:
                self.state = 457
                self.match(OParser.WITH)
                self.state = 458
                self.match(OParser.INDEX)
                self.state = 463
                _la = self._input.LA(1)
                if _la==OParser.LPAR:
                    self.state = 459
                    self.match(OParser.LPAR)
                    self.state = 460 
                    localctx.indices = self.variable_identifier_list()
                    self.state = 461
                    self.match(OParser.RPAR)




            self.state = 467
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
            if isinstance( listener, OParserListener ):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = OParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 469
                self.match(OParser.STORABLE)


            self.state = 472
            self.match(OParser.CATEGORY)
            self.state = 473 
            localctx.name = self.type_identifier()
            self.state = 478
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 474
                self.match(OParser.LPAR)
                self.state = 475 
                localctx.attrs = self.attribute_identifier_list()
                self.state = 476
                self.match(OParser.RPAR)


            self.state = 482
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 480
                self.match(OParser.EXTENDS)
                self.state = 481 
                localctx.derived = self.derived_list(0)


            self.state = 484 
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
            if isinstance( listener, OParserListener ):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = OParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_singleton_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(OParser.SINGLETON)
            self.state = 487 
            localctx.name = self.type_identifier()
            self.state = 492
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 488
                self.match(OParser.LPAR)
                self.state = 489 
                localctx.attrs = self.attribute_identifier_list()
                self.state = 490
                self.match(OParser.RPAR)


            self.state = 494 
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
            if isinstance( listener, OParserListener ):
                listener.enterDerivedListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDerivedListItem(self)


    class DerivedListContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Derived_listContext)
            super(OParser.DerivedListContext, self).__init__(parser)
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDerivedList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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

            self.state = 497 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 504
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
                    self.state = 499
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 500
                    self.match(OParser.COMMA)
                    self.state = 501 
                    localctx.item = self.type_identifier() 
                self.state = 506
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
            if isinstance( listener, OParserListener ):
                listener.enterEmptyCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCurlyCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCurlyCategoryMethodList(self)



    def category_method_list(self):

        localctx = OParser.Category_method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_category_method_list)
        self._la = 0 # Token type
        try:
            self.state = 513
            token = self._input.LA(1)
            if token in [OParser.SEMI]:
                localctx = OParser.EmptyCategoryMethodListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.match(OParser.SEMI)

            elif token in [OParser.LCURL]:
                localctx = OParser.CurlyCategoryMethodListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.match(OParser.LCURL)
                self.state = 510
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR) | (1 << OParser.ABSTRACT))) != 0) or ((((_la - 103)) & ~0x3f) == 0 and ((1 << (_la - 103)) & ((1 << (OParser.GETTER - 103)) | (1 << (OParser.METHOD - 103)) | (1 << (OParser.OPERATOR - 103)) | (1 << (OParser.SETTER - 103)) | (1 << (OParser.TYPE_IDENTIFIER - 103)))) != 0):
                    self.state = 509 
                    localctx.items = self.member_method_declaration_list()


                self.state = 512
                self.match(OParser.RCURL)

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
            if isinstance( listener, OParserListener ):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = OParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 515 
                localctx.typ = self.typedef(0)


            self.state = 518
            self.match(OParser.OPERATOR)
            self.state = 519 
            localctx.op = self.operator()
            self.state = 520
            self.match(OParser.LPAR)
            self.state = 521 
            localctx.arg = self.operator_argument()
            self.state = 522
            self.match(OParser.RPAR)
            self.state = 523
            self.match(OParser.LCURL)
            self.state = 525
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                self.state = 524 
                localctx.stmts = self.statement_list()


            self.state = 527
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
            if isinstance( listener, OParserListener ):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = OParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_setter_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(OParser.SETTER)
            self.state = 530 
            localctx.name = self.variable_identifier()
            self.state = 531
            self.match(OParser.LCURL)
            self.state = 533
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                self.state = 532 
                localctx.stmts = self.statement_list()


            self.state = 535
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = OParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 537
                self.match(OParser.NATIVE)


            self.state = 540
            self.match(OParser.SETTER)
            self.state = 541 
            localctx.name = self.variable_identifier()
            self.state = 542
            self.match(OParser.LCURL)
            self.state = 544
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 543 
                localctx.stmts = self.native_statement_list()


            self.state = 546
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
            if isinstance( listener, OParserListener ):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = OParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_getter_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(OParser.GETTER)
            self.state = 549 
            localctx.name = self.variable_identifier()
            self.state = 550
            self.match(OParser.LCURL)
            self.state = 552
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                self.state = 551 
                localctx.stmts = self.statement_list()


            self.state = 554
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = OParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 556
                self.match(OParser.NATIVE)


            self.state = 559
            self.match(OParser.GETTER)
            self.state = 560 
            localctx.name = self.variable_identifier()
            self.state = 561
            self.match(OParser.LCURL)
            self.state = 563
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 562 
                localctx.stmts = self.native_statement_list()


            self.state = 565
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = OParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.match(OParser.NATIVE)
            self.state = 568
            self.match(OParser.RESOURCE)
            self.state = 569 
            localctx.name = self.type_identifier()
            self.state = 574
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 570
                self.match(OParser.LPAR)
                self.state = 571 
                localctx.attrs = self.attribute_identifier_list()
                self.state = 572
                self.match(OParser.RPAR)


            self.state = 576
            self.match(OParser.LCURL)
            self.state = 577 
            localctx.bindings = self.native_category_bindings()
            self.state = 579
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 110)) & ~0x3f) == 0 and ((1 << (_la - 110)) & ((1 << (OParser.METHOD - 110)) | (1 << (OParser.NATIVE - 110)) | (1 << (OParser.SETTER - 110)) | (1 << (OParser.TYPE_IDENTIFIER - 110)))) != 0):
                self.state = 578 
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 581
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = OParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 583
                self.match(OParser.STORABLE)


            self.state = 586
            self.match(OParser.NATIVE)
            self.state = 587
            self.match(OParser.CATEGORY)
            self.state = 588 
            localctx.name = self.type_identifier()
            self.state = 593
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 589
                self.match(OParser.LPAR)
                self.state = 590 
                localctx.attrs = self.attribute_identifier_list()
                self.state = 591
                self.match(OParser.RPAR)


            self.state = 595
            self.match(OParser.LCURL)
            self.state = 596 
            localctx.bindings = self.native_category_bindings()
            self.state = 598
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 110)) & ~0x3f) == 0 and ((1 << (_la - 110)) & ((1 << (OParser.METHOD - 110)) | (1 << (OParser.NATIVE - 110)) | (1 << (OParser.SETTER - 110)) | (1 << (OParser.TYPE_IDENTIFIER - 110)))) != 0):
                self.state = 597 
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 600
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = OParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_native_category_bindings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(OParser.CATEGORY)
            self.state = 603
            self.match(OParser.BINDINGS)
            self.state = 604
            self.match(OParser.LCURL)
            self.state = 605 
            localctx.items = self.native_category_binding_list(0)
            self.state = 606
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
            if isinstance( listener, OParserListener ):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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

            self.state = 609 
            localctx.item = self.native_category_binding()
            self.state = 610
            self.match(OParser.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 618
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
                    self.state = 612
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 613 
                    localctx.item = self.native_category_binding()
                    self.state = 614
                    self.match(OParser.SEMI) 
                self.state = 620
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
            if isinstance( listener, OParserListener ):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = OParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.match(OParser.ABSTRACT)
            self.state = 623
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 622 
                localctx.typ = self.typedef(0)


            self.state = 625
            self.match(OParser.METHOD)
            self.state = 626 
            localctx.name = self.method_identifier()
            self.state = 627
            self.match(OParser.LPAR)
            self.state = 629
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.MUTABLE - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)))) != 0):
                self.state = 628 
                localctx.args = self.argument_list()


            self.state = 631
            self.match(OParser.RPAR)
            self.state = 632
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
            if isinstance( listener, OParserListener ):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = OParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 634 
                localctx.typ = self.typedef(0)


            self.state = 637
            self.match(OParser.METHOD)
            self.state = 638 
            localctx.name = self.method_identifier()
            self.state = 639
            self.match(OParser.LPAR)
            self.state = 641
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.MUTABLE - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)))) != 0):
                self.state = 640 
                localctx.args = self.argument_list()


            self.state = 643
            self.match(OParser.RPAR)
            self.state = 644
            self.match(OParser.LCURL)
            self.state = 646
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                self.state = 645 
                localctx.stmts = self.statement_list()


            self.state = 648
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = OParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 650 
                localctx.typ = self.category_or_any_type()


            self.state = 654
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 653
                self.match(OParser.NATIVE)


            self.state = 656
            self.match(OParser.METHOD)
            self.state = 657 
            localctx.name = self.method_identifier()
            self.state = 658
            self.match(OParser.LPAR)
            self.state = 660
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.MUTABLE - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)))) != 0):
                self.state = 659 
                localctx.args = self.argument_list()


            self.state = 662
            self.match(OParser.RPAR)
            self.state = 663
            self.match(OParser.LCURL)
            self.state = 664 
            localctx.stmts = self.native_statement_list()
            self.state = 665
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
            if isinstance( listener, OParserListener ):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = OParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.match(OParser.TEST)
            self.state = 668
            self.match(OParser.METHOD)
            self.state = 669
            localctx.name = self.match(OParser.TEXT_LITERAL)
            self.state = 670
            self.match(OParser.LPAR)
            self.state = 671
            self.match(OParser.RPAR)
            self.state = 672
            self.match(OParser.LCURL)
            self.state = 673 
            localctx.stmts = self.statement_list()
            self.state = 674
            self.match(OParser.RCURL)
            self.state = 675
            self.match(OParser.VERIFYING)
            self.state = 683
            token = self._input.LA(1)
            if token in [OParser.LCURL]:
                self.state = 676
                self.match(OParser.LCURL)
                self.state = 677 
                localctx.exps = self.assertion_list()
                self.state = 678
                self.match(OParser.RCURL)

            elif token in [OParser.SYMBOL_IDENTIFIER]:
                self.state = 680 
                localctx.error = self.symbol_identifier()
                self.state = 681
                self.match(OParser.SEMI)

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
            if isinstance( listener, OParserListener ):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = OParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685 
            localctx.exp = self.expression(0)
            self.state = 686
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
            if isinstance( listener, OParserListener ):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = OParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688 
            localctx.typ = self.category_or_any_type()
            self.state = 693
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 689
                self.match(OParser.LPAR)
                self.state = 690 
                localctx.attrs = self.attribute_identifier_list()
                self.state = 691
                self.match(OParser.RPAR)


            self.state = 695 
            localctx.name = self.variable_identifier()
            self.state = 698
            _la = self._input.LA(1)
            if _la==OParser.EQ:
                self.state = 696
                self.match(OParser.EQ)
                self.state = 697 
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
            if isinstance( listener, OParserListener ):
                listener.enterCurlyStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCurlyStatementList(self)


    class SingleStatementContext(Statement_or_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Statement_or_listContext)
            super(OParser.SingleStatementContext, self).__init__(parser)
            self.stmt = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(OParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSingleStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSingleStatement(self)



    def statement_or_list(self):

        localctx = OParser.Statement_or_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement_or_list)
        try:
            self.state = 707
            token = self._input.LA(1)
            if token in [OParser.COMMENT, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.BREAK, OParser.DELETE, OParser.DO, OParser.FLUSH, OParser.FOR, OParser.IF, OParser.METHOD, OParser.RETURN, OParser.STORE, OParser.SWITCH, OParser.THROW, OParser.TRY, OParser.WITH, OParser.WHILE, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.SingleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 700 
                localctx.stmt = self.statement()

            elif token in [OParser.LCURL]:
                localctx = OParser.CurlyStatementListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 701
                self.match(OParser.LCURL)
                self.state = 705
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 702 
                    localctx.items = self.statement_list()
                    self.state = 703
                    self.match(OParser.RCURL)



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
            if isinstance( listener, OParserListener ):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(OParser.Store_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(OParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(OParser.Write_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(OParser.While_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(OParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(OParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitRaiseStatement(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.BreakStatementContext, self).__init__(parser)
            self.stmt = None # Break_statementContext
            self.copyFrom(ctx)

        def break_statement(self):
            return self.getTypedRuleContext(OParser.Break_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitBreakStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(OParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(OParser.If_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(OParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(OParser.Try_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(OParser.Return_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(OParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitClosureStatement(self)


    class FlushStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.FlushStatementContext, self).__init__(parser)
            self.stmt = None # Flush_statementContext
            self.copyFrom(ctx)

        def flush_statement(self):
            return self.getTypedRuleContext(OParser.Flush_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterFlushStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitFlushStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(OParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(OParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = OParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 730
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                localctx = OParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 709 
                localctx.stmt = self.method_call()
                self.state = 710
                self.match(OParser.SEMI)
                pass

            elif la_ == 2:
                localctx = OParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 712 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = OParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 713 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = OParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 714 
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = OParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 715 
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = OParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 716 
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = OParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 717 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = OParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 718 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = OParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 719 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = OParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 720 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = OParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 721 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = OParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 722 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = OParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 723 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 14:
                localctx = OParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 724 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 15:
                localctx = OParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 725 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = OParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 726 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = OParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 727 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = OParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 728 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = OParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 729 
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
            if isinstance( listener, OParserListener ):
                listener.enterFlush_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitFlush_statement(self)




    def flush_statement(self):

        localctx = OParser.Flush_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_flush_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
            self.match(OParser.FLUSH)
            self.state = 733
            self.match(OParser.LPAR)
            self.state = 734
            self.match(OParser.RPAR)
            self.state = 735
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
            if isinstance( listener, OParserListener ):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = OParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_store_statement)
        try:
            self.state = 760
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 737
                self.match(OParser.DELETE)
                self.state = 738
                self.match(OParser.LPAR)
                self.state = 739 
                localctx.to_del = self.expression_list()
                self.state = 740
                self.match(OParser.RPAR)
                self.state = 741
                self.match(OParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 743
                self.match(OParser.STORE)
                self.state = 744
                self.match(OParser.LPAR)
                self.state = 745 
                localctx.to_add = self.expression_list()
                self.state = 746
                self.match(OParser.RPAR)
                self.state = 747
                self.match(OParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 749
                self.match(OParser.DELETE)
                self.state = 750
                self.match(OParser.LPAR)
                self.state = 751 
                localctx.to_del = self.expression_list()
                self.state = 752
                self.match(OParser.RPAR)
                self.state = 753
                self.match(OParser.AND)
                self.state = 754
                self.match(OParser.STORE)
                self.state = 755
                self.match(OParser.LPAR)
                self.state = 756 
                localctx.to_add = self.expression_list()
                self.state = 757
                self.match(OParser.RPAR)
                self.state = 758
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
            if isinstance( listener, OParserListener ):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = OParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 762
            self.match(OParser.WITH)
            self.state = 763
            self.match(OParser.LPAR)
            self.state = 764 
            localctx.stmt = self.assign_variable_statement()
            self.state = 765
            self.match(OParser.RPAR)
            self.state = 766 
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
            if isinstance( listener, OParserListener ):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = OParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 768
            self.match(OParser.WITH)
            self.state = 769
            self.match(OParser.LPAR)
            self.state = 770 
            localctx.typ = self.type_identifier()
            self.state = 771
            self.match(OParser.RPAR)
            self.state = 772 
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
            if isinstance( listener, OParserListener ):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = OParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_switch_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 774
            self.match(OParser.SWITCH)
            self.state = 775
            self.match(OParser.LPAR)
            self.state = 776 
            localctx.exp = self.expression(0)
            self.state = 777
            self.match(OParser.RPAR)
            self.state = 778
            self.match(OParser.LCURL)
            self.state = 779 
            localctx.cases = self.switch_case_statement_list()
            self.state = 785
            _la = self._input.LA(1)
            if _la==OParser.DEFAULT:
                self.state = 780
                self.match(OParser.DEFAULT)
                self.state = 781
                self.match(OParser.COLON)
                self.state = 783
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                    self.state = 782 
                    localctx.stmts = self.statement_list()




            self.state = 787
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
            if isinstance( listener, OParserListener ):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = OParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switch_case_statement)
        self._la = 0 # Token type
        try:
            self.state = 802
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = OParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 789
                self.match(OParser.CASE)
                self.state = 790 
                localctx.exp = self.atomic_literal()
                self.state = 791
                self.match(OParser.COLON)
                self.state = 793
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                    self.state = 792 
                    localctx.stmts = self.statement_list()


                pass

            elif la_ == 2:
                localctx = OParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 795
                self.match(OParser.CASE)
                self.state = 796
                self.match(OParser.IN)
                self.state = 797 
                localctx.exp = self.literal_collection()
                self.state = 798
                self.match(OParser.COLON)
                self.state = 800
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                    self.state = 799 
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
            if isinstance( listener, OParserListener ):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = OParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 804
            self.match(OParser.FOR)
            self.state = 805
            self.match(OParser.EACH)
            self.state = 806
            self.match(OParser.LPAR)
            self.state = 807 
            localctx.name1 = self.variable_identifier()
            self.state = 810
            _la = self._input.LA(1)
            if _la==OParser.COMMA:
                self.state = 808
                self.match(OParser.COMMA)
                self.state = 809 
                localctx.name2 = self.variable_identifier()


            self.state = 812
            self.match(OParser.IN)
            self.state = 813 
            localctx.source = self.expression(0)
            self.state = 814
            self.match(OParser.RPAR)
            self.state = 815 
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
            if isinstance( listener, OParserListener ):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = OParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_do_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 817
            self.match(OParser.DO)
            self.state = 818
            self.match(OParser.LCURL)
            self.state = 820
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                self.state = 819 
                localctx.stmts = self.statement_list()


            self.state = 822
            self.match(OParser.RCURL)
            self.state = 823
            self.match(OParser.WHILE)
            self.state = 824
            self.match(OParser.LPAR)
            self.state = 825 
            localctx.exp = self.expression(0)
            self.state = 826
            self.match(OParser.RPAR)
            self.state = 827
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
            if isinstance( listener, OParserListener ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = OParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 829
            self.match(OParser.WHILE)
            self.state = 830
            self.match(OParser.LPAR)
            self.state = 831 
            localctx.exp = self.expression(0)
            self.state = 832
            self.match(OParser.RPAR)
            self.state = 833 
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
            if isinstance( listener, OParserListener ):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = OParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 835
            self.match(OParser.IF)
            self.state = 836
            self.match(OParser.LPAR)
            self.state = 837 
            localctx.exp = self.expression(0)
            self.state = 838
            self.match(OParser.RPAR)
            self.state = 839 
            localctx.stmts = self.statement_or_list()
            self.state = 841
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 840 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 845
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 843
                self.match(OParser.ELSE)
                self.state = 844 
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
            if isinstance( listener, OParserListener ):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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

            self.state = 848
            self.match(OParser.ELSE)
            self.state = 849
            self.match(OParser.IF)
            self.state = 850
            self.match(OParser.LPAR)
            self.state = 851 
            localctx.exp = self.expression(0)
            self.state = 852
            self.match(OParser.RPAR)
            self.state = 853 
            localctx.stmts = self.statement_or_list()
            self._ctx.stop = self._input.LT(-1)
            self.state = 865
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
                    self.state = 855
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 856
                    self.match(OParser.ELSE)
                    self.state = 857
                    self.match(OParser.IF)
                    self.state = 858
                    self.match(OParser.LPAR)
                    self.state = 859 
                    localctx.exp = self.expression(0)
                    self.state = 860
                    self.match(OParser.RPAR)
                    self.state = 861 
                    localctx.stmts = self.statement_or_list() 
                self.state = 867
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
            if isinstance( listener, OParserListener ):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = OParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 868
            self.match(OParser.THROW)
            self.state = 869 
            localctx.exp = self.expression(0)
            self.state = 870
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
            if isinstance( listener, OParserListener ):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = OParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 872
            self.match(OParser.TRY)
            self.state = 873
            self.match(OParser.LPAR)
            self.state = 874 
            localctx.name = self.variable_identifier()
            self.state = 875
            self.match(OParser.RPAR)
            self.state = 876
            self.match(OParser.LCURL)
            self.state = 878
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                self.state = 877 
                localctx.stmts = self.statement_list()


            self.state = 880
            self.match(OParser.RCURL)
            self.state = 882
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 881 
                localctx.handlers = self.catch_statement_list()


            self.state = 893
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 884
                self.match(OParser.CATCH)
                self.state = 885
                self.match(OParser.LPAR)
                self.state = 886
                self.match(OParser.ANY)
                self.state = 887
                self.match(OParser.RPAR)
                self.state = 888
                self.match(OParser.LCURL)
                self.state = 890
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                    self.state = 889 
                    localctx.anyStmts = self.statement_list()


                self.state = 892
                self.match(OParser.RCURL)


            self.state = 901
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 895
                self.match(OParser.FINALLY)
                self.state = 896
                self.match(OParser.LCURL)
                self.state = 898
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                    self.state = 897 
                    localctx.finalStmts = self.statement_list()


                self.state = 900
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
            if isinstance( listener, OParserListener ):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = OParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_catch_statement)
        self._la = 0 # Token type
        try:
            self.state = 924
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                localctx = OParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 903
                self.match(OParser.CATCH)
                self.state = 904
                self.match(OParser.LPAR)
                self.state = 905 
                localctx.name = self.symbol_identifier()
                self.state = 906
                self.match(OParser.RPAR)
                self.state = 907
                self.match(OParser.LCURL)
                self.state = 909
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                    self.state = 908 
                    localctx.stmts = self.statement_list()


                self.state = 911
                self.match(OParser.RCURL)
                pass

            elif la_ == 2:
                localctx = OParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 913
                self.match(OParser.CATCH)
                self.state = 914
                self.match(OParser.IN)
                self.state = 915
                self.match(OParser.LPAR)
                self.state = 916 
                localctx.exp = self.symbol_list()
                self.state = 917
                self.match(OParser.RPAR)
                self.state = 918
                self.match(OParser.LCURL)
                self.state = 920
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                    self.state = 919 
                    localctx.stmts = self.statement_list()


                self.state = 922
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
            if isinstance( listener, OParserListener ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = OParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 926
            self.match(OParser.BREAK)
            self.state = 927
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
            if isinstance( listener, OParserListener ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = OParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 929
            self.match(OParser.RETURN)
            self.state = 931
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (OParser.EXECUTE - 94)) | (1 << (OParser.FETCH - 94)) | (1 << (OParser.FILTERED - 94)) | (1 << (OParser.MUTABLE - 94)) | (1 << (OParser.NULL - 94)) | (1 << (OParser.READ - 94)) | (1 << (OParser.SELF - 94)) | (1 << (OParser.SORTED - 94)) | (1 << (OParser.THIS - 94)) | (1 << (OParser.BOOLEAN_LITERAL - 94)) | (1 << (OParser.CHAR_LITERAL - 94)) | (1 << (OParser.MIN_INTEGER - 94)) | (1 << (OParser.MAX_INTEGER - 94)) | (1 << (OParser.SYMBOL_IDENTIFIER - 94)) | (1 << (OParser.TYPE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (OParser.VARIABLE_IDENTIFIER - 158)) | (1 << (OParser.TEXT_LITERAL - 158)) | (1 << (OParser.UUID_LITERAL - 158)) | (1 << (OParser.INTEGER_LITERAL - 158)) | (1 << (OParser.HEXA_LITERAL - 158)) | (1 << (OParser.DECIMAL_LITERAL - 158)) | (1 << (OParser.DATETIME_LITERAL - 158)) | (1 << (OParser.TIME_LITERAL - 158)) | (1 << (OParser.DATE_LITERAL - 158)) | (1 << (OParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 930 
                localctx.exp = self.expression(0)


            self.state = 933
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
            if isinstance( listener, OParserListener ):
                listener.enterMethod_call(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = OParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 935 
            localctx.method = self.method_selector()
            self.state = 936
            self.match(OParser.LPAR)
            self.state = 938
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (OParser.EXECUTE - 94)) | (1 << (OParser.FETCH - 94)) | (1 << (OParser.FILTERED - 94)) | (1 << (OParser.MUTABLE - 94)) | (1 << (OParser.NULL - 94)) | (1 << (OParser.READ - 94)) | (1 << (OParser.SELF - 94)) | (1 << (OParser.SORTED - 94)) | (1 << (OParser.THIS - 94)) | (1 << (OParser.BOOLEAN_LITERAL - 94)) | (1 << (OParser.CHAR_LITERAL - 94)) | (1 << (OParser.MIN_INTEGER - 94)) | (1 << (OParser.MAX_INTEGER - 94)) | (1 << (OParser.SYMBOL_IDENTIFIER - 94)) | (1 << (OParser.TYPE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (OParser.VARIABLE_IDENTIFIER - 158)) | (1 << (OParser.TEXT_LITERAL - 158)) | (1 << (OParser.UUID_LITERAL - 158)) | (1 << (OParser.INTEGER_LITERAL - 158)) | (1 << (OParser.HEXA_LITERAL - 158)) | (1 << (OParser.DECIMAL_LITERAL - 158)) | (1 << (OParser.DATETIME_LITERAL - 158)) | (1 << (OParser.TIME_LITERAL - 158)) | (1 << (OParser.DATE_LITERAL - 158)) | (1 << (OParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 937 
                localctx.args = self.argument_assignment_list(0)


            self.state = 940
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
            if isinstance( listener, OParserListener ):
                listener.enterMethodParent(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethodParent(self)


    class MethodNameContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_selectorContext)
            super(OParser.MethodNameContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterMethodName(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethodName(self)



    def method_selector(self):

        localctx = OParser.Method_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_method_selector)
        try:
            self.state = 947
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = OParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 942 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = OParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 943 
                localctx.parent = self.callable_parent(0)
                self.state = 944
                self.match(OParser.DOT)
                self.state = 945 
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
            if isinstance( listener, OParserListener ):
                listener.enterCallableSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCallableSelector(self)


    class CallableRootContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a OParser.Callable_parentContext)
            super(OParser.CallableRootContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCallableRoot(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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

            self.state = 950 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 956
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
                    self.state = 952
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 953 
                    localctx.select = self.callable_selector() 
                self.state = 958
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
            if isinstance( listener, OParserListener ):
                listener.enterCallableItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCallableMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCallableMemberSelector(self)



    def callable_selector(self):

        localctx = OParser.Callable_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_callable_selector)
        try:
            self.state = 965
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 959
                self.match(OParser.DOT)
                self.state = 960 
                localctx.name = self.variable_identifier()

            elif token in [OParser.LBRAK]:
                localctx = OParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 961
                self.match(OParser.LBRAK)
                self.state = 962 
                localctx.exp = self.expression(0)
                self.state = 963
                self.match(OParser.RBRAK)

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
            if isinstance( listener, OParserListener ):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitIntDivideExpression(self)


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
            if isinstance( listener, OParserListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTernaryExpression(self)


    class ContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(OParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(OParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitContainsAllExpression(self)


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
            if isinstance( listener, OParserListener ):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterIsAnExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitLessThanOrEqualExpression(self)


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
            if isinstance( listener, OParserListener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAndExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ClosureExpressionContext, self).__init__(parser)
            self.exp = None # Closure_expressionContext
            self.copyFrom(ctx)

        def closure_expression(self):
            return self.getTypedRuleContext(OParser.Closure_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitClosureExpression(self)


    class NotContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(OParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(OParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNotContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNotContainsAnyExpression(self)


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
            if isinstance( listener, OParserListener ):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterIsNotAnExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitExecuteExpression(self)


    class MethodExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.MethodExpressionContext, self).__init__(parser)
            self.exp = None # Method_expressionContext
            self.copyFrom(ctx)

        def method_expression(self):
            return self.getTypedRuleContext(OParser.Method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAddExpression(self)


    class NotContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(OParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(OParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNotContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNotContainsAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(OParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCastExpression(self)


    class ContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(OParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(OParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitContainsAnyExpression(self)


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
            if isinstance( listener, OParserListener ):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            self.state = 990
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                localctx = OParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 968
                self.match(OParser.MINUS)
                self.state = 969 
                localctx.exp = self.expression(34)
                pass

            elif la_ == 2:
                localctx = OParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 970
                self.match(OParser.XMARK)
                self.state = 971 
                localctx.exp = self.expression(33)
                pass

            elif la_ == 3:
                localctx = OParser.CastExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 972
                self.match(OParser.LPAR)
                self.state = 973 
                localctx.right = self.category_or_any_type()
                self.state = 974
                self.match(OParser.RPAR)
                self.state = 975 
                localctx.left = self.expression(13)
                pass

            elif la_ == 4:
                localctx = OParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 977 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 5:
                localctx = OParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 978 
                localctx.exp = self.method_expression()
                pass

            elif la_ == 6:
                localctx = OParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 979
                self.match(OParser.CODE)
                self.state = 980
                self.match(OParser.LPAR)
                self.state = 981 
                localctx.exp = self.expression(0)
                self.state = 982
                self.match(OParser.RPAR)
                pass

            elif la_ == 7:
                localctx = OParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 984
                self.match(OParser.EXECUTE)
                self.state = 985
                self.match(OParser.LPAR)
                self.state = 986 
                localctx.name = self.variable_identifier()
                self.state = 987
                self.match(OParser.RPAR)
                pass

            elif la_ == 8:
                localctx = OParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 989 
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1099
                    la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                    if la_ == 1:
                        localctx = OParser.MultiplyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 992
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 993 
                        self.multiply()
                        self.state = 994 
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 2:
                        localctx = OParser.DivideExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 996
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 997 
                        self.divide()
                        self.state = 998 
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 3:
                        localctx = OParser.ModuloExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1000
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1001 
                        self.modulo()
                        self.state = 1002 
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 4:
                        localctx = OParser.IntDivideExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1004
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 1005 
                        self.idivide()
                        self.state = 1006 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 5:
                        localctx = OParser.AddExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1008
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1009
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==OParser.PLUS or _la==OParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 1010 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 6:
                        localctx = OParser.LessThanExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1011
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1012
                        self.match(OParser.LT)
                        self.state = 1013 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 7:
                        localctx = OParser.LessThanOrEqualExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1014
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1015
                        self.match(OParser.LTE)
                        self.state = 1016 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 8:
                        localctx = OParser.GreaterThanExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1017
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1018
                        self.match(OParser.GT)
                        self.state = 1019 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 9:
                        localctx = OParser.GreaterThanOrEqualExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1020
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1021
                        self.match(OParser.GTE)
                        self.state = 1022 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 10:
                        localctx = OParser.IsNotExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1023
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1024
                        self.match(OParser.IS)
                        self.state = 1025
                        self.match(OParser.NOT)
                        self.state = 1026 
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 11:
                        localctx = OParser.IsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1027
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1028
                        self.match(OParser.IS)
                        self.state = 1029 
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 12:
                        localctx = OParser.EqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1030
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1031
                        self.match(OParser.EQ2)
                        self.state = 1032 
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 13:
                        localctx = OParser.NotEqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1033
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1034
                        self.match(OParser.XEQ)
                        self.state = 1035 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 14:
                        localctx = OParser.RoughlyEqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1036
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1037
                        self.match(OParser.TEQ)
                        self.state = 1038 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 15:
                        localctx = OParser.OrExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1039
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1040
                        self.match(OParser.PIPE2)
                        self.state = 1041 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 16:
                        localctx = OParser.AndExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1042
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1043
                        self.match(OParser.AMP2)
                        self.state = 1044 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 17:
                        localctx = OParser.TernaryExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.test = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1045
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1046
                        self.match(OParser.QMARK)
                        self.state = 1047 
                        localctx.ifTrue = self.expression(0)
                        self.state = 1048
                        self.match(OParser.COLON)
                        self.state = 1049 
                        localctx.ifFalse = self.expression(15)
                        pass

                    elif la_ == 18:
                        localctx = OParser.InExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1051
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1052
                        self.match(OParser.IN)
                        self.state = 1053 
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 19:
                        localctx = OParser.ContainsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1054
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1055
                        self.match(OParser.CONTAINS)
                        self.state = 1056 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 20:
                        localctx = OParser.ContainsAllExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1057
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 1058
                        self.match(OParser.CONTAINS)
                        self.state = 1059
                        self.match(OParser.ALL)
                        self.state = 1060 
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 21:
                        localctx = OParser.ContainsAnyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1061
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 1062
                        self.match(OParser.CONTAINS)
                        self.state = 1063
                        self.match(OParser.ANY)
                        self.state = 1064 
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 22:
                        localctx = OParser.NotInExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1065
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1066
                        self.match(OParser.NOT)
                        self.state = 1067
                        self.match(OParser.IN)
                        self.state = 1068 
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 23:
                        localctx = OParser.NotContainsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1069
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1070
                        self.match(OParser.NOT)
                        self.state = 1071
                        self.match(OParser.CONTAINS)
                        self.state = 1072 
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 24:
                        localctx = OParser.NotContainsAllExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1073
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1074
                        self.match(OParser.NOT)
                        self.state = 1075
                        self.match(OParser.CONTAINS)
                        self.state = 1076
                        self.match(OParser.ALL)
                        self.state = 1077 
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 25:
                        localctx = OParser.NotContainsAnyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1078
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1079
                        self.match(OParser.NOT)
                        self.state = 1080
                        self.match(OParser.CONTAINS)
                        self.state = 1081
                        self.match(OParser.ANY)
                        self.state = 1082 
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 26:
                        localctx = OParser.IsNotAnExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1083
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1084
                        self.match(OParser.IS)
                        self.state = 1085
                        self.match(OParser.NOT)
                        self.state = 1086 
                        localctx.right = self.an_expression()
                        pass

                    elif la_ == 27:
                        localctx = OParser.IsAnExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1087
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1088
                        self.match(OParser.IS)
                        self.state = 1089 
                        localctx.right = self.an_expression()
                        pass

                    elif la_ == 28:
                        localctx = OParser.IteratorExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1090
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1091
                        self.match(OParser.FOR)
                        self.state = 1092
                        self.match(OParser.EACH)
                        self.state = 1093
                        self.match(OParser.LPAR)
                        self.state = 1094 
                        localctx.name = self.variable_identifier()
                        self.state = 1095
                        self.match(OParser.IN)
                        self.state = 1096 
                        localctx.source = self.expression(0)
                        self.state = 1097
                        self.match(OParser.RPAR)
                        pass

             
                self.state = 1103
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
            if isinstance( listener, OParserListener ):
                listener.enterAn_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAn_expression(self)




    def an_expression(self):

        localctx = OParser.An_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_an_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1104
            if not self.willBeAOrAn():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willBeAOrAn()")
            self.state = 1105
            self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1106 
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
            if isinstance( listener, OParserListener ):
                listener.enterClosure_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitClosure_expression(self)




    def closure_expression(self):

        localctx = OParser.Closure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_closure_expression)
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
            if isinstance( listener, OParserListener ):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Instance_expressionContext)
            super(OParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(OParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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

            self.state = 1111 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1117
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
                    self.state = 1113
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1114 
                    localctx.selector = self.selector_expression() 
                self.state = 1119
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


        def read_expression(self):
            return self.getTypedRuleContext(OParser.Read_expressionContext,0)


        def sorted_expression(self):
            return self.getTypedRuleContext(OParser.Sorted_expressionContext,0)


        def method_call(self):
            return self.getTypedRuleContext(OParser.Method_callContext,0)


        def constructor_expression(self):
            return self.getTypedRuleContext(OParser.Constructor_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_method_expression

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterMethod_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethod_expression(self)




    def method_expression(self):

        localctx = OParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_method_expression)
        try:
            self.state = 1128
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
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
                self.filtered_list_expression()
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
            if isinstance( listener, OParserListener ):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = OParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_blob_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1130
            self.match(OParser.BLOB)
            self.state = 1131
            self.match(OParser.LPAR)
            self.state = 1132 
            self.expression(0)
            self.state = 1133
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
            if isinstance( listener, OParserListener ):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = OParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_document_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1135
            self.match(OParser.DOCUMENT)
            self.state = 1136
            self.match(OParser.LPAR)
            self.state = 1138
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (OParser.EXECUTE - 94)) | (1 << (OParser.FETCH - 94)) | (1 << (OParser.FILTERED - 94)) | (1 << (OParser.MUTABLE - 94)) | (1 << (OParser.NULL - 94)) | (1 << (OParser.READ - 94)) | (1 << (OParser.SELF - 94)) | (1 << (OParser.SORTED - 94)) | (1 << (OParser.THIS - 94)) | (1 << (OParser.BOOLEAN_LITERAL - 94)) | (1 << (OParser.CHAR_LITERAL - 94)) | (1 << (OParser.MIN_INTEGER - 94)) | (1 << (OParser.MAX_INTEGER - 94)) | (1 << (OParser.SYMBOL_IDENTIFIER - 94)) | (1 << (OParser.TYPE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (OParser.VARIABLE_IDENTIFIER - 158)) | (1 << (OParser.TEXT_LITERAL - 158)) | (1 << (OParser.UUID_LITERAL - 158)) | (1 << (OParser.INTEGER_LITERAL - 158)) | (1 << (OParser.HEXA_LITERAL - 158)) | (1 << (OParser.DECIMAL_LITERAL - 158)) | (1 << (OParser.DATETIME_LITERAL - 158)) | (1 << (OParser.TIME_LITERAL - 158)) | (1 << (OParser.DATE_LITERAL - 158)) | (1 << (OParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1137 
                self.expression(0)


            self.state = 1140
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Read_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_read_expression

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterRead_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitRead_expression(self)




    def read_expression(self):

        localctx = OParser.Read_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1142
            self.match(OParser.READ)
            self.state = 1143
            self.match(OParser.FROM)
            self.state = 1144 
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
            if isinstance( listener, OParserListener ):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = OParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1146
            self.match(OParser.WRITE)
            self.state = 1147
            self.match(OParser.LPAR)
            self.state = 1148 
            localctx.what = self.expression(0)
            self.state = 1149
            self.match(OParser.RPAR)
            self.state = 1150
            self.match(OParser.TO)
            self.state = 1151 
            localctx.target = self.expression(0)
            self.state = 1152
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
            if isinstance( listener, OParserListener ):
                listener.enterFiltered_list_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitFiltered_list_expression(self)




    def filtered_list_expression(self):

        localctx = OParser.Filtered_list_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_filtered_list_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1154
            self.match(OParser.FILTERED)
            self.state = 1155
            self.match(OParser.LPAR)
            self.state = 1156 
            localctx.source = self.expression(0)
            self.state = 1157
            self.match(OParser.RPAR)
            self.state = 1158
            self.match(OParser.WITH)
            self.state = 1159
            self.match(OParser.LPAR)
            self.state = 1160 
            localctx.name = self.variable_identifier()
            self.state = 1161
            self.match(OParser.RPAR)
            self.state = 1162
            self.match(OParser.WHERE)
            self.state = 1163
            self.match(OParser.LPAR)
            self.state = 1164 
            localctx.predicate = self.expression(0)
            self.state = 1165
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
            if isinstance( listener, OParserListener ):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterFetchMany(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitFetchMany(self)



    def fetch_store_expression(self):

        localctx = OParser.Fetch_store_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_fetch_store_expression)
        self._la = 0 # Token type
        try:
            self.state = 1216
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                localctx = OParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1167
                self.match(OParser.FETCH)
                self.state = 1168
                self.match(OParser.ONE)
                self.state = 1173
                _la = self._input.LA(1)
                if _la==OParser.LPAR:
                    self.state = 1169
                    self.match(OParser.LPAR)
                    self.state = 1170 
                    localctx.typ = self.mutable_category_type()
                    self.state = 1171
                    self.match(OParser.RPAR)


                self.state = 1175
                self.match(OParser.WHERE)
                self.state = 1176
                self.match(OParser.LPAR)
                self.state = 1177 
                localctx.predicate = self.expression(0)
                self.state = 1178
                self.match(OParser.RPAR)
                pass

            elif la_ == 2:
                localctx = OParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1180
                self.match(OParser.FETCH)
                self.state = 1199
                token = self._input.LA(1)
                if token in [OParser.ALL]:
                    self.state = 1181
                    self.match(OParser.ALL)
                    self.state = 1182
                    self.match(OParser.LPAR)
                    self.state = 1184
                    _la = self._input.LA(1)
                    if _la==OParser.MUTABLE or _la==OParser.TYPE_IDENTIFIER:
                        self.state = 1183 
                        localctx.typ = self.mutable_category_type()


                    self.state = 1186
                    self.match(OParser.RPAR)

                elif token in [OParser.LPAR]:
                    self.state = 1187
                    self.match(OParser.LPAR)
                    self.state = 1189
                    _la = self._input.LA(1)
                    if _la==OParser.MUTABLE or _la==OParser.TYPE_IDENTIFIER:
                        self.state = 1188 
                        localctx.typ = self.mutable_category_type()


                    self.state = 1191
                    self.match(OParser.RPAR)
                    self.state = 1192
                    self.match(OParser.ROWS)
                    self.state = 1193
                    self.match(OParser.LPAR)
                    self.state = 1194 
                    localctx.xstart = self.expression(0)
                    self.state = 1195
                    self.match(OParser.TO)
                    self.state = 1196 
                    localctx.xstop = self.expression(0)
                    self.state = 1197
                    self.match(OParser.RPAR)

                else:
                    raise NoViableAltException(self)

                self.state = 1206
                la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                if la_ == 1:
                    self.state = 1201
                    self.match(OParser.WHERE)
                    self.state = 1202
                    self.match(OParser.LPAR)
                    self.state = 1203 
                    localctx.predicate = self.expression(0)
                    self.state = 1204
                    self.match(OParser.RPAR)


                self.state = 1214
                la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
                if la_ == 1:
                    self.state = 1208
                    self.match(OParser.ORDER)
                    self.state = 1209
                    self.match(OParser.BY)
                    self.state = 1210
                    self.match(OParser.LPAR)
                    self.state = 1211 
                    localctx.orderby = self.order_by_list()
                    self.state = 1212
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
            if isinstance( listener, OParserListener ):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = OParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1218
            self.match(OParser.SORTED)
            self.state = 1220
            _la = self._input.LA(1)
            if _la==OParser.DESC:
                self.state = 1219
                self.match(OParser.DESC)


            self.state = 1222
            self.match(OParser.LPAR)
            self.state = 1223 
            localctx.source = self.instance_expression(0)
            self.state = 1229
            _la = self._input.LA(1)
            if _la==OParser.COMMA:
                self.state = 1224
                self.match(OParser.COMMA)
                self.state = 1225 
                self.key_token()
                self.state = 1226
                self.match(OParser.EQ)
                self.state = 1227 
                localctx.key = self.instance_expression(0)


            self.state = 1231
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
            if isinstance( listener, OParserListener ):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitItemSelector(self)



    def selector_expression(self):

        localctx = OParser.Selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_selector_expression)
        try:
            self.state = 1243
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                localctx = OParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1233
                self.match(OParser.DOT)
                self.state = 1234 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = OParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1235
                self.match(OParser.LBRAK)
                self.state = 1236 
                localctx.exp = self.expression(0)
                self.state = 1237
                self.match(OParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = OParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1239
                self.match(OParser.LBRAK)
                self.state = 1240 
                localctx.xslice = self.slice_arguments()
                self.state = 1241
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
            if isinstance( listener, OParserListener ):
                listener.enterConstructor_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitConstructor_expression(self)




    def constructor_expression(self):

        localctx = OParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1245 
            localctx.typ = self.mutable_category_type()
            self.state = 1246
            self.match(OParser.LPAR)
            self.state = 1248
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (OParser.EXECUTE - 94)) | (1 << (OParser.FETCH - 94)) | (1 << (OParser.FILTERED - 94)) | (1 << (OParser.MUTABLE - 94)) | (1 << (OParser.NULL - 94)) | (1 << (OParser.READ - 94)) | (1 << (OParser.SELF - 94)) | (1 << (OParser.SORTED - 94)) | (1 << (OParser.THIS - 94)) | (1 << (OParser.BOOLEAN_LITERAL - 94)) | (1 << (OParser.CHAR_LITERAL - 94)) | (1 << (OParser.MIN_INTEGER - 94)) | (1 << (OParser.MAX_INTEGER - 94)) | (1 << (OParser.SYMBOL_IDENTIFIER - 94)) | (1 << (OParser.TYPE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (OParser.VARIABLE_IDENTIFIER - 158)) | (1 << (OParser.TEXT_LITERAL - 158)) | (1 << (OParser.UUID_LITERAL - 158)) | (1 << (OParser.INTEGER_LITERAL - 158)) | (1 << (OParser.HEXA_LITERAL - 158)) | (1 << (OParser.DECIMAL_LITERAL - 158)) | (1 << (OParser.DATETIME_LITERAL - 158)) | (1 << (OParser.TIME_LITERAL - 158)) | (1 << (OParser.DATE_LITERAL - 158)) | (1 << (OParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1247 
                localctx.args = self.argument_assignment_list(0)


            self.state = 1250
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
            if isinstance( listener, OParserListener ):
                listener.enterExpressionAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitExpressionAssignmentList(self)


    class ArgumentAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Argument_assignment_listContext)
            super(OParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def argument_assignment(self):
            return self.getTypedRuleContext(OParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            self.state = 1257
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                localctx = OParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1253 
                localctx.exp = self.expression(0)
                self.state = 1254
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = OParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1256 
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1264
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
                    self.state = 1259
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1260
                    self.match(OParser.COMMA)
                    self.state = 1261 
                    localctx.item = self.argument_assignment() 
                self.state = 1266
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
            if isinstance( listener, OParserListener ):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = OParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1267 
            localctx.name = self.variable_identifier()
            self.state = 1268 
            self.assign()
            self.state = 1269 
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
            if isinstance( listener, OParserListener ):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = OParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1271 
            localctx.inst = self.assignable_instance(0)
            self.state = 1272 
            self.assign()
            self.state = 1273 
            localctx.exp = self.expression(0)
            self.state = 1274
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
            if isinstance( listener, OParserListener ):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = OParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_child_instance)
        try:
            self.state = 1282
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1276
                self.match(OParser.DOT)
                self.state = 1277 
                localctx.name = self.variable_identifier()

            elif token in [OParser.LBRAK]:
                localctx = OParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1278
                self.match(OParser.LBRAK)
                self.state = 1279 
                localctx.exp = self.expression(0)
                self.state = 1280
                self.match(OParser.RBRAK)

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
            if isinstance( listener, OParserListener ):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = OParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1284 
            localctx.items = self.variable_identifier_list()
            self.state = 1285 
            self.assign()
            self.state = 1286 
            localctx.exp = self.expression(0)
            self.state = 1287
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
            if isinstance( listener, OParserListener ):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = OParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1289
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
            if isinstance( listener, OParserListener ):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = OParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = OParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1292
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR) | (1 << OParser.ABSTRACT))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (OParser.ANY - 67)) | (1 << (OParser.ATTRIBUTE - 67)) | (1 << (OParser.CATEGORY - 67)) | (1 << (OParser.ENUMERATED - 67)) | (1 << (OParser.METHOD - 67)) | (1 << (OParser.NATIVE - 67)))) != 0) or ((((_la - 136)) & ~0x3f) == 0 and ((1 << (_la - 136)) & ((1 << (OParser.SINGLETON - 136)) | (1 << (OParser.STORABLE - 136)) | (1 << (OParser.TEST - 136)) | (1 << (OParser.TYPE_IDENTIFIER - 136)))) != 0):
                self.state = 1291 
                self.declarations()


            self.state = 1294 
            self.lfs()
            self.state = 1295
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
            if isinstance( listener, OParserListener ):
                listener.enterDeclarations(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = OParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1297 
            self.declaration()
            self.state = 1303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR) | (1 << OParser.ABSTRACT))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (OParser.ANY - 67)) | (1 << (OParser.ATTRIBUTE - 67)) | (1 << (OParser.CATEGORY - 67)) | (1 << (OParser.ENUMERATED - 67)) | (1 << (OParser.METHOD - 67)) | (1 << (OParser.NATIVE - 67)))) != 0) or ((((_la - 136)) & ~0x3f) == 0 and ((1 << (_la - 136)) & ((1 << (OParser.SINGLETON - 136)) | (1 << (OParser.STORABLE - 136)) | (1 << (OParser.TEST - 136)) | (1 << (OParser.TYPE_IDENTIFIER - 136)))) != 0):
                self.state = 1298 
                self.lfp()
                self.state = 1299 
                self.declaration()
                self.state = 1305
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
            if isinstance( listener, OParserListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = OParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMENT:
                self.state = 1306 
                self.comment_statement()
                self.state = 1307 
                self.lfp()
                self.state = 1313
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1319
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
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
            super(OParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_resource_declaration(self):
            return self.getTypedRuleContext(OParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = OParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_resource_declaration)
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
            super(OParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enum_category_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_category_declarationContext,0)


        def enum_native_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_native_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_enum_declaration

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitEnum_declaration(self)




    def enum_declaration(self):

        localctx = OParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_enum_declaration)
        try:
            self.state = 1325
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_symbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_symbol_list(self)




    def native_symbol_list(self):

        localctx = OParser.Native_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_native_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1327 
            self.native_symbol()
            self.state = 1333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SYMBOL_IDENTIFIER:
                self.state = 1328 
                self.lfp()
                self.state = 1329 
                self.native_symbol()
                self.state = 1335
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
            if isinstance( listener, OParserListener ):
                listener.enterCategory_symbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategory_symbol_list(self)




    def category_symbol_list(self):

        localctx = OParser.Category_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_category_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1336 
            self.category_symbol()
            self.state = 1342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SYMBOL_IDENTIFIER:
                self.state = 1337 
                self.lfp()
                self.state = 1338 
                self.category_symbol()
                self.state = 1344
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
            if isinstance( listener, OParserListener ):
                listener.enterSymbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSymbol_list(self)




    def symbol_list(self):

        localctx = OParser.Symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1345 
            self.symbol_identifier()
            self.state = 1350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1346
                self.match(OParser.COMMA)
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
            if isinstance( listener, OParserListener ):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = OParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_attribute_constraint)
        try:
            self.state = 1363
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                localctx = OParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1353
                self.match(OParser.IN)
                self.state = 1354 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = OParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1355
                self.match(OParser.IN)
                self.state = 1356 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = OParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1357
                self.match(OParser.IN)
                self.state = 1358 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = OParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1359
                self.match(OParser.MATCHING)
                self.state = 1360
                localctx.text = self.match(OParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = OParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1361
                self.match(OParser.MATCHING)
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
            if isinstance( listener, OParserListener ):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = OParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1366
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1365
                self.match(OParser.MUTABLE)


            self.state = 1368
            self.match(OParser.LBRAK)
            self.state = 1370
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (OParser.EXECUTE - 94)) | (1 << (OParser.FETCH - 94)) | (1 << (OParser.FILTERED - 94)) | (1 << (OParser.MUTABLE - 94)) | (1 << (OParser.NULL - 94)) | (1 << (OParser.READ - 94)) | (1 << (OParser.SELF - 94)) | (1 << (OParser.SORTED - 94)) | (1 << (OParser.THIS - 94)) | (1 << (OParser.BOOLEAN_LITERAL - 94)) | (1 << (OParser.CHAR_LITERAL - 94)) | (1 << (OParser.MIN_INTEGER - 94)) | (1 << (OParser.MAX_INTEGER - 94)) | (1 << (OParser.SYMBOL_IDENTIFIER - 94)) | (1 << (OParser.TYPE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (OParser.VARIABLE_IDENTIFIER - 158)) | (1 << (OParser.TEXT_LITERAL - 158)) | (1 << (OParser.UUID_LITERAL - 158)) | (1 << (OParser.INTEGER_LITERAL - 158)) | (1 << (OParser.HEXA_LITERAL - 158)) | (1 << (OParser.DECIMAL_LITERAL - 158)) | (1 << (OParser.DATETIME_LITERAL - 158)) | (1 << (OParser.TIME_LITERAL - 158)) | (1 << (OParser.DATE_LITERAL - 158)) | (1 << (OParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1369 
                self.expression_list()


            self.state = 1372
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
            if isinstance( listener, OParserListener ):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = OParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1375
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1374
                self.match(OParser.MUTABLE)


            self.state = 1377
            self.match(OParser.LT)
            self.state = 1379
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (OParser.EXECUTE - 94)) | (1 << (OParser.FETCH - 94)) | (1 << (OParser.FILTERED - 94)) | (1 << (OParser.MUTABLE - 94)) | (1 << (OParser.NULL - 94)) | (1 << (OParser.READ - 94)) | (1 << (OParser.SELF - 94)) | (1 << (OParser.SORTED - 94)) | (1 << (OParser.THIS - 94)) | (1 << (OParser.BOOLEAN_LITERAL - 94)) | (1 << (OParser.CHAR_LITERAL - 94)) | (1 << (OParser.MIN_INTEGER - 94)) | (1 << (OParser.MAX_INTEGER - 94)) | (1 << (OParser.SYMBOL_IDENTIFIER - 94)) | (1 << (OParser.TYPE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (OParser.VARIABLE_IDENTIFIER - 158)) | (1 << (OParser.TEXT_LITERAL - 158)) | (1 << (OParser.UUID_LITERAL - 158)) | (1 << (OParser.INTEGER_LITERAL - 158)) | (1 << (OParser.HEXA_LITERAL - 158)) | (1 << (OParser.DECIMAL_LITERAL - 158)) | (1 << (OParser.DATETIME_LITERAL - 158)) | (1 << (OParser.TIME_LITERAL - 158)) | (1 << (OParser.DATE_LITERAL - 158)) | (1 << (OParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1378 
                self.expression_list()


            self.state = 1381
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
            if isinstance( listener, OParserListener ):
                listener.enterExpression_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = OParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1383 
            self.expression(0)
            self.state = 1388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1384
                self.match(OParser.COMMA)
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
            if isinstance( listener, OParserListener ):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = OParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1391
            self.match(OParser.LBRAK)
            self.state = 1392 
            localctx.low = self.expression(0)
            self.state = 1393
            self.match(OParser.RANGE)
            self.state = 1394 
            localctx.high = self.expression(0)
            self.state = 1395
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
            if isinstance( listener, OParserListener ):
                listener.enterIteratorType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterListType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCursorType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCursorType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(OParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            self.state = 1409
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.TYPE_IDENTIFIER]:
                localctx = OParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1398 
                localctx.p = self.primary_type()

            elif token in [OParser.CURSOR]:
                localctx = OParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1399
                self.match(OParser.CURSOR)
                self.state = 1400
                self.match(OParser.LT)
                self.state = 1401 
                localctx.c = self.typedef(0)
                self.state = 1402
                self.match(OParser.GT)

            elif token in [OParser.ITERATOR]:
                localctx = OParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1404
                self.match(OParser.ITERATOR)
                self.state = 1405
                self.match(OParser.LT)
                self.state = 1406 
                localctx.i = self.typedef(0)
                self.state = 1407
                self.match(OParser.GT)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,102,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1419
                    la_ = self._interp.adaptivePredict(self._input,101,self._ctx)
                    if la_ == 1:
                        localctx = OParser.SetTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1411
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1412
                        self.match(OParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = OParser.ListTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1413
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1414
                        self.match(OParser.LBRAK)
                        self.state = 1415
                        self.match(OParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = OParser.DictTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1416
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1417
                        self.match(OParser.LCURL)
                        self.state = 1418
                        self.match(OParser.RCURL)
                        pass

             
                self.state = 1423
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
            if isinstance( listener, OParserListener ):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Primary_typeContext)
            super(OParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(OParser.Category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = OParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_primary_type)
        try:
            self.state = 1426
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID]:
                localctx = OParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1424 
                localctx.n = self.native_type()

            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.CategoryTypeContext(self, localctx)
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
            if isinstance( listener, OParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPeriodType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(OParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCharacterType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(OParser.IMAGE, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(OParser.BLOB, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(OParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDateType(self)



    def native_type(self):

        localctx = OParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_native_type)
        try:
            self.state = 1442
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN]:
                localctx = OParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1428
                self.match(OParser.BOOLEAN)

            elif token in [OParser.CHARACTER]:
                localctx = OParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1429
                self.match(OParser.CHARACTER)

            elif token in [OParser.TEXT]:
                localctx = OParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1430
                self.match(OParser.TEXT)

            elif token in [OParser.IMAGE]:
                localctx = OParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1431
                self.match(OParser.IMAGE)

            elif token in [OParser.INTEGER]:
                localctx = OParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1432
                self.match(OParser.INTEGER)

            elif token in [OParser.DECIMAL]:
                localctx = OParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1433
                self.match(OParser.DECIMAL)

            elif token in [OParser.DOCUMENT]:
                localctx = OParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1434
                self.match(OParser.DOCUMENT)

            elif token in [OParser.DATE]:
                localctx = OParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1435
                self.match(OParser.DATE)

            elif token in [OParser.DATETIME]:
                localctx = OParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1436
                self.match(OParser.DATETIME)

            elif token in [OParser.TIME]:
                localctx = OParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1437
                self.match(OParser.TIME)

            elif token in [OParser.PERIOD]:
                localctx = OParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1438
                self.match(OParser.PERIOD)

            elif token in [OParser.CODE]:
                localctx = OParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1439
                self.match(OParser.CODE)

            elif token in [OParser.BLOB]:
                localctx = OParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1440
                self.match(OParser.BLOB)

            elif token in [OParser.UUID]:
                localctx = OParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1441
                self.match(OParser.UUID)

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
            if isinstance( listener, OParserListener ):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = OParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1444
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
            if isinstance( listener, OParserListener ):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = OParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1447
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1446
                self.match(OParser.MUTABLE)


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
            super(OParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(OParser.CODE, 0)

        def getRuleIndex(self):
            return OParser.RULE_code_type

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = OParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1451
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
            if isinstance( listener, OParserListener ):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_declarationContext)
            super(OParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(OParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_declarationContext)
            super(OParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(OParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = OParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_category_declaration)
        try:
            self.state = 1456
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                localctx = OParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1453 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = OParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1454 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = OParser.SingletonCategoryDeclarationContext(self, localctx)
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
            if isinstance( listener, OParserListener ):
                listener.enterType_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitType_identifier_list(self)




    def type_identifier_list(self):

        localctx = OParser.Type_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_type_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1458 
            self.type_identifier()
            self.state = 1463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1459
                self.match(OParser.COMMA)
                self.state = 1460 
                self.type_identifier()
                self.state = 1465
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
            if isinstance( listener, OParserListener ):
                listener.enterMethod_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethod_identifier(self)




    def method_identifier(self):

        localctx = OParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_method_identifier)
        try:
            self.state = 1468
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1466 
                self.variable_identifier()

            elif token in [OParser.TYPE_IDENTIFIER]:
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
            if isinstance( listener, OParserListener ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a OParser.IdentifierContext)
            super(OParser.SymbolIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a OParser.IdentifierContext)
            super(OParser.VariableIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = OParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_identifier)
        try:
            self.state = 1473
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1470 
                self.variable_identifier()

            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1471 
                self.type_identifier()

            elif token in [OParser.SYMBOL_IDENTIFIER]:
                localctx = OParser.SymbolIdentifierContext(self, localctx)
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
            super(OParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_variable_identifier

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = OParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1475
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
            if isinstance( listener, OParserListener ):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = OParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1477
            _la = self._input.LA(1)
            if not(_la==OParser.STORABLE or _la==OParser.VARIABLE_IDENTIFIER):
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
            super(OParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_type_identifier

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = OParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1479
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
            if isinstance( listener, OParserListener ):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = OParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1481
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
            if isinstance( listener, OParserListener ):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = OParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1483 
            self.argument()
            self.state = 1488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1484
                self.match(OParser.COMMA)
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
            if isinstance( listener, OParserListener ):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a OParser.ArgumentContext)
            super(OParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(OParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = OParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1496
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                localctx = OParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1491 
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = OParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1493
                _la = self._input.LA(1)
                if _la==OParser.MUTABLE:
                    self.state = 1492
                    self.match(OParser.MUTABLE)


                self.state = 1495 
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
            if isinstance( listener, OParserListener ):
                listener.enterOperator_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOperator_argument(self)




    def operator_argument(self):

        localctx = OParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_operator_argument)
        try:
            self.state = 1500
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1498 
                self.named_argument()

            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.ANY, OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1499 
                self.typed_argument()

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
            if isinstance( listener, OParserListener ):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = OParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1502 
            self.variable_identifier()
            self.state = 1505
            _la = self._input.LA(1)
            if _la==OParser.EQ:
                self.state = 1503
                self.match(OParser.EQ)
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
            if isinstance( listener, OParserListener ):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = OParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_code_argument)
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
            super(OParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def any_type(self):
            return self.getTypedRuleContext(OParser.Any_typeContext,0)


        def getRuleIndex(self):
            return OParser.RULE_category_or_any_type

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCategory_or_any_type(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategory_or_any_type(self)




    def category_or_any_type(self):

        localctx = OParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_category_or_any_type)
        try:
            self.state = 1512
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1510 
                self.typedef(0)

            elif token in [OParser.ANY]:
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
            if isinstance( listener, OParserListener ):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Any_typeContext)
            super(OParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(OParser.ANY, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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

            self.state = 1515
            self.match(OParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1525
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1523
                    la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
                    if la_ == 1:
                        localctx = OParser.AnyListTypeContext(self, OParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1517
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1518
                        self.match(OParser.LBRAK)
                        self.state = 1519
                        self.match(OParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = OParser.AnyDictTypeContext(self, OParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1520
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1521
                        self.match(OParser.LCURL)
                        self.state = 1522
                        self.match(OParser.RCURL)
                        pass

             
                self.state = 1527
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
            if isinstance( listener, OParserListener ):
                listener.enterMember_method_declaration_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMember_method_declaration_list(self)




    def member_method_declaration_list(self):

        localctx = OParser.Member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_member_method_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1528 
            self.member_method_declaration()
            self.state = 1534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR) | (1 << OParser.ABSTRACT))) != 0) or ((((_la - 103)) & ~0x3f) == 0 and ((1 << (_la - 103)) & ((1 << (OParser.GETTER - 103)) | (1 << (OParser.METHOD - 103)) | (1 << (OParser.OPERATOR - 103)) | (1 << (OParser.SETTER - 103)) | (1 << (OParser.TYPE_IDENTIFIER - 103)))) != 0):
                self.state = 1529 
                self.lfp()
                self.state = 1530 
                self.member_method_declaration()
                self.state = 1536
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
            if isinstance( listener, OParserListener ):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = OParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_member_method_declaration)
        try:
            self.state = 1542
            la_ = self._interp.adaptivePredict(self._input,119,self._ctx)
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_member_method_declaration_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_member_method_declaration_list(self)




    def native_member_method_declaration_list(self):

        localctx = OParser.Native_member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_native_member_method_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1544 
            self.native_member_method_declaration()
            self.state = 1550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 110)) & ~0x3f) == 0 and ((1 << (_la - 110)) & ((1 << (OParser.METHOD - 110)) | (1 << (OParser.NATIVE - 110)) | (1 << (OParser.SETTER - 110)) | (1 << (OParser.TYPE_IDENTIFIER - 110)))) != 0):
                self.state = 1545 
                self.lfp()
                self.state = 1546 
                self.native_member_method_declaration()
                self.state = 1552
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = OParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_native_member_method_declaration)
        try:
            self.state = 1556
            la_ = self._interp.adaptivePredict(self._input,121,self._ctx)
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
            if isinstance( listener, OParserListener ):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = OParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_native_category_binding)
        try:
            self.state = 1568
            token = self._input.LA(1)
            if token in [OParser.JAVA]:
                localctx = OParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1558
                self.match(OParser.JAVA)
                self.state = 1559 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [OParser.CSHARP]:
                localctx = OParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1560
                self.match(OParser.CSHARP)
                self.state = 1561 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [OParser.PYTHON2]:
                localctx = OParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1562
                self.match(OParser.PYTHON2)
                self.state = 1563 
                localctx.binding = self.python_category_binding()

            elif token in [OParser.PYTHON3]:
                localctx = OParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1564
                self.match(OParser.PYTHON3)
                self.state = 1565 
                localctx.binding = self.python_category_binding()

            elif token in [OParser.JAVASCRIPT]:
                localctx = OParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1566
                self.match(OParser.JAVASCRIPT)
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
            super(OParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(OParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_category_binding

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = OParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_python_category_binding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1570 
            self.identifier()
            self.state = 1572
            _la = self._input.LA(1)
            if _la==OParser.FROM:
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
            if isinstance( listener, OParserListener ):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = OParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_python_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1574
            self.match(OParser.FROM)
            self.state = 1575 
            self.module_token()
            self.state = 1576
            self.match(OParser.COLON)
            self.state = 1577 
            self.identifier()
            self.state = 1582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.DOT:
                self.state = 1578
                self.match(OParser.DOT)
                self.state = 1579 
                self.identifier()
                self.state = 1584
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = OParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_javascript_category_binding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1585 
            self.identifier()
            self.state = 1587
            _la = self._input.LA(1)
            if _la==OParser.FROM:
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = OParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1589
            self.match(OParser.FROM)
            self.state = 1590 
            self.module_token()
            self.state = 1591
            self.match(OParser.COLON)
            self.state = 1593
            _la = self._input.LA(1)
            if _la==OParser.SLASH:
                self.state = 1592
                self.match(OParser.SLASH)


            self.state = 1595 
            self.javascript_identifier()
            self.state = 1600
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SLASH:
                self.state = 1596
                self.match(OParser.SLASH)
                self.state = 1597 
                self.javascript_identifier()
                self.state = 1602
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1605
            _la = self._input.LA(1)
            if _la==OParser.DOT:
                self.state = 1603
                self.match(OParser.DOT)
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
            if isinstance( listener, OParserListener ):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = OParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1607 
            self.variable_identifier()
            self.state = 1612
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1608
                self.match(OParser.COMMA)
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
            if isinstance( listener, OParserListener ):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = OParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_attribute_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1615 
            self.attribute_identifier()
            self.state = 1620
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1616
                self.match(OParser.COMMA)
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
            if isinstance( listener, OParserListener ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = OParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_method_declaration)
        try:
            self.state = 1627
            la_ = self._interp.adaptivePredict(self._input,131,self._ctx)
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
            super(OParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(OParser.COMMENT, 0)

        def getRuleIndex(self):
            return OParser.RULE_comment_statement

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = OParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1629
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
            if isinstance( listener, OParserListener ):
                listener.enterNative_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNative_statement_list(self)




    def native_statement_list(self):

        localctx = OParser.Native_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_native_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1631 
            self.native_statement()
            self.state = 1637
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 1632 
                self.lfp()
                self.state = 1633 
                self.native_statement()
                self.state = 1639
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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = OParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_native_statement)
        try:
            self.state = 1650
            token = self._input.LA(1)
            if token in [OParser.JAVA]:
                localctx = OParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1640
                self.match(OParser.JAVA)
                self.state = 1641 
                self.java_statement()

            elif token in [OParser.CSHARP]:
                localctx = OParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1642
                self.match(OParser.CSHARP)
                self.state = 1643 
                self.csharp_statement()

            elif token in [OParser.PYTHON2]:
                localctx = OParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1644
                self.match(OParser.PYTHON2)
                self.state = 1645 
                self.python_native_statement()

            elif token in [OParser.PYTHON3]:
                localctx = OParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1646
                self.match(OParser.PYTHON3)
                self.state = 1647 
                self.python_native_statement()

            elif token in [OParser.JAVASCRIPT]:
                localctx = OParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1648
                self.match(OParser.JAVASCRIPT)
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
            if isinstance( listener, OParserListener ):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = OParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1652 
            self.python_statement()
            self.state = 1654
            _la = self._input.LA(1)
            if _la==OParser.SEMI:
                self.state = 1653
                self.match(OParser.SEMI)


            self.state = 1657
            _la = self._input.LA(1)
            if _la==OParser.FROM:
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = OParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1659 
            self.javascript_statement()
            self.state = 1661
            _la = self._input.LA(1)
            if _la==OParser.SEMI:
                self.state = 1660
                self.match(OParser.SEMI)


            self.state = 1664
            _la = self._input.LA(1)
            if _la==OParser.FROM:
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
            if isinstance( listener, OParserListener ):
                listener.enterStatement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = OParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1666 
            self.statement()
            self.state = 1672
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (OParser.BREAK - 74)) | (1 << (OParser.DELETE - 74)) | (1 << (OParser.DO - 74)) | (1 << (OParser.FLUSH - 74)) | (1 << (OParser.FOR - 74)) | (1 << (OParser.IF - 74)) | (1 << (OParser.METHOD - 74)) | (1 << (OParser.RETURN - 74)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.STORE - 139)) | (1 << (OParser.SWITCH - 139)) | (1 << (OParser.THROW - 139)) | (1 << (OParser.TRY - 139)) | (1 << (OParser.WITH - 139)) | (1 << (OParser.WHILE - 139)) | (1 << (OParser.WRITE - 139)) | (1 << (OParser.SYMBOL_IDENTIFIER - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)) | (1 << (OParser.VARIABLE_IDENTIFIER - 139)))) != 0):
                self.state = 1667 
                self.lfp()
                self.state = 1668 
                self.statement()
                self.state = 1674
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
            if isinstance( listener, OParserListener ):
                listener.enterAssertion_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAssertion_list(self)




    def assertion_list(self):

        localctx = OParser.Assertion_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_assertion_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1675 
            self.assertion()
            self.state = 1681
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (OParser.EXECUTE - 94)) | (1 << (OParser.FETCH - 94)) | (1 << (OParser.FILTERED - 94)) | (1 << (OParser.MUTABLE - 94)) | (1 << (OParser.NULL - 94)) | (1 << (OParser.READ - 94)) | (1 << (OParser.SELF - 94)) | (1 << (OParser.SORTED - 94)) | (1 << (OParser.THIS - 94)) | (1 << (OParser.BOOLEAN_LITERAL - 94)) | (1 << (OParser.CHAR_LITERAL - 94)) | (1 << (OParser.MIN_INTEGER - 94)) | (1 << (OParser.MAX_INTEGER - 94)) | (1 << (OParser.SYMBOL_IDENTIFIER - 94)) | (1 << (OParser.TYPE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (OParser.VARIABLE_IDENTIFIER - 158)) | (1 << (OParser.TEXT_LITERAL - 158)) | (1 << (OParser.UUID_LITERAL - 158)) | (1 << (OParser.INTEGER_LITERAL - 158)) | (1 << (OParser.HEXA_LITERAL - 158)) | (1 << (OParser.DECIMAL_LITERAL - 158)) | (1 << (OParser.DATETIME_LITERAL - 158)) | (1 << (OParser.TIME_LITERAL - 158)) | (1 << (OParser.DATE_LITERAL - 158)) | (1 << (OParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1676 
                self.lfp()
                self.state = 1677 
                self.assertion()
                self.state = 1683
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
            if isinstance( listener, OParserListener ):
                listener.enterSwitch_case_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSwitch_case_statement_list(self)




    def switch_case_statement_list(self):

        localctx = OParser.Switch_case_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_switch_case_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1684 
            self.switch_case_statement()
            self.state = 1690
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.CASE:
                self.state = 1685 
                self.lfp()
                self.state = 1686 
                self.switch_case_statement()
                self.state = 1692
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
            if isinstance( listener, OParserListener ):
                listener.enterCatch_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCatch_statement_list(self)




    def catch_statement_list(self):

        localctx = OParser.Catch_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1693 
            self.catch_statement()
            self.state = 1699
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,141,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1694 
                    self.lfp()
                    self.state = 1695 
                    self.catch_statement() 
                self.state = 1701
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
            if isinstance( listener, OParserListener ):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = OParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_literal_collection)
        try:
            self.state = 1716
            la_ = self._interp.adaptivePredict(self._input,142,self._ctx)
            if la_ == 1:
                localctx = OParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1702
                self.match(OParser.LBRAK)
                self.state = 1703 
                localctx.low = self.atomic_literal()
                self.state = 1704
                self.match(OParser.RANGE)
                self.state = 1705 
                localctx.high = self.atomic_literal()
                self.state = 1706
                self.match(OParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = OParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1708
                self.match(OParser.LBRAK)
                self.state = 1709 
                self.literal_list_literal()
                self.state = 1710
                self.match(OParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = OParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1712
                self.match(OParser.LT)
                self.state = 1713 
                self.literal_list_literal()
                self.state = 1714
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
            if isinstance( listener, OParserListener ):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(OParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitBooleanLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(OParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitHexadecimalLiteral(self)


    class UUIDLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.UUIDLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def UUID_LITERAL(self):
            return self.getToken(OParser.UUID_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterUUIDLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitUUIDLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(OParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(OParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(OParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(OParser.Null_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(OParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = OParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_atomic_literal)
        try:
            self.state = 1732
            token = self._input.LA(1)
            if token in [OParser.MIN_INTEGER]:
                localctx = OParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1718
                localctx.t = self.match(OParser.MIN_INTEGER)

            elif token in [OParser.MAX_INTEGER]:
                localctx = OParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1719
                localctx.t = self.match(OParser.MAX_INTEGER)

            elif token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1720
                localctx.t = self.match(OParser.INTEGER_LITERAL)

            elif token in [OParser.HEXA_LITERAL]:
                localctx = OParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1721
                localctx.t = self.match(OParser.HEXA_LITERAL)

            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1722
                localctx.t = self.match(OParser.CHAR_LITERAL)

            elif token in [OParser.DATE_LITERAL]:
                localctx = OParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1723
                localctx.t = self.match(OParser.DATE_LITERAL)

            elif token in [OParser.TIME_LITERAL]:
                localctx = OParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1724
                localctx.t = self.match(OParser.TIME_LITERAL)

            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1725
                localctx.t = self.match(OParser.TEXT_LITERAL)

            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1726
                localctx.t = self.match(OParser.DECIMAL_LITERAL)

            elif token in [OParser.DATETIME_LITERAL]:
                localctx = OParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1727
                localctx.t = self.match(OParser.DATETIME_LITERAL)

            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1728
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)

            elif token in [OParser.PERIOD_LITERAL]:
                localctx = OParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1729
                localctx.t = self.match(OParser.PERIOD_LITERAL)

            elif token in [OParser.UUID_LITERAL]:
                localctx = OParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1730
                localctx.t = self.match(OParser.UUID_LITERAL)

            elif token in [OParser.NULL]:
                localctx = OParser.NullLiteralContext(self, localctx)
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
            if isinstance( listener, OParserListener ):
                listener.enterLiteral_list_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitLiteral_list_literal(self)




    def literal_list_literal(self):

        localctx = OParser.Literal_list_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1734 
            self.atomic_literal()
            self.state = 1739
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1735
                self.match(OParser.COMMA)
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
            if isinstance( listener, OParserListener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(OParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = OParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_selectable_expression)
        try:
            self.state = 1746
            la_ = self._interp.adaptivePredict(self._input,145,self._ctx)
            if la_ == 1:
                localctx = OParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1742 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = OParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1743 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = OParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1744 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = OParser.ThisExpressionContext(self, localctx)
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
            super(OParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def THIS(self):
            return self.getToken(OParser.THIS, 0)

        def getRuleIndex(self):
            return OParser.RULE_this_expression

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = OParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1748
            _la = self._input.LA(1)
            if not(_la==OParser.SELF or _la==OParser.THIS):
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
            if isinstance( listener, OParserListener ):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = OParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1750
            self.match(OParser.LPAR)
            self.state = 1751 
            self.expression(0)
            self.state = 1752
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
            if isinstance( listener, OParserListener ):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = OParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_literal_expression)
        try:
            self.state = 1756
            token = self._input.LA(1)
            if token in [OParser.NULL, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.MIN_INTEGER, OParser.MAX_INTEGER, OParser.TEXT_LITERAL, OParser.UUID_LITERAL, OParser.INTEGER_LITERAL, OParser.HEXA_LITERAL, OParser.DECIMAL_LITERAL, OParser.DATETIME_LITERAL, OParser.TIME_LITERAL, OParser.DATE_LITERAL, OParser.PERIOD_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1754 
                self.atomic_literal()

            elif token in [OParser.LPAR, OParser.LBRAK, OParser.LCURL, OParser.LT, OParser.MUTABLE]:
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
            if isinstance( listener, OParserListener ):
                listener.enterCollection_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCollection_literal(self)




    def collection_literal(self):

        localctx = OParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_collection_literal)
        try:
            self.state = 1763
            la_ = self._interp.adaptivePredict(self._input,147,self._ctx)
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
            if isinstance( listener, OParserListener ):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = OParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1766
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1765
                self.match(OParser.MUTABLE)


            self.state = 1768
            self.match(OParser.LPAR)
            self.state = 1770
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (OParser.EXECUTE - 94)) | (1 << (OParser.FETCH - 94)) | (1 << (OParser.FILTERED - 94)) | (1 << (OParser.MUTABLE - 94)) | (1 << (OParser.NULL - 94)) | (1 << (OParser.READ - 94)) | (1 << (OParser.SELF - 94)) | (1 << (OParser.SORTED - 94)) | (1 << (OParser.THIS - 94)) | (1 << (OParser.BOOLEAN_LITERAL - 94)) | (1 << (OParser.CHAR_LITERAL - 94)) | (1 << (OParser.MIN_INTEGER - 94)) | (1 << (OParser.MAX_INTEGER - 94)) | (1 << (OParser.SYMBOL_IDENTIFIER - 94)) | (1 << (OParser.TYPE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (OParser.VARIABLE_IDENTIFIER - 158)) | (1 << (OParser.TEXT_LITERAL - 158)) | (1 << (OParser.UUID_LITERAL - 158)) | (1 << (OParser.INTEGER_LITERAL - 158)) | (1 << (OParser.HEXA_LITERAL - 158)) | (1 << (OParser.DECIMAL_LITERAL - 158)) | (1 << (OParser.DATETIME_LITERAL - 158)) | (1 << (OParser.TIME_LITERAL - 158)) | (1 << (OParser.DATE_LITERAL - 158)) | (1 << (OParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1769 
                self.expression_tuple()


            self.state = 1772
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
            if isinstance( listener, OParserListener ):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = OParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1775
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1774
                self.match(OParser.MUTABLE)


            self.state = 1777
            self.match(OParser.LCURL)
            self.state = 1779
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (OParser.EXECUTE - 94)) | (1 << (OParser.FETCH - 94)) | (1 << (OParser.FILTERED - 94)) | (1 << (OParser.MUTABLE - 94)) | (1 << (OParser.NULL - 94)) | (1 << (OParser.READ - 94)) | (1 << (OParser.SELF - 94)) | (1 << (OParser.SORTED - 94)) | (1 << (OParser.THIS - 94)) | (1 << (OParser.BOOLEAN_LITERAL - 94)) | (1 << (OParser.CHAR_LITERAL - 94)) | (1 << (OParser.MIN_INTEGER - 94)) | (1 << (OParser.MAX_INTEGER - 94)) | (1 << (OParser.SYMBOL_IDENTIFIER - 94)) | (1 << (OParser.TYPE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (OParser.VARIABLE_IDENTIFIER - 158)) | (1 << (OParser.TEXT_LITERAL - 158)) | (1 << (OParser.UUID_LITERAL - 158)) | (1 << (OParser.INTEGER_LITERAL - 158)) | (1 << (OParser.HEXA_LITERAL - 158)) | (1 << (OParser.DECIMAL_LITERAL - 158)) | (1 << (OParser.DATETIME_LITERAL - 158)) | (1 << (OParser.TIME_LITERAL - 158)) | (1 << (OParser.DATE_LITERAL - 158)) | (1 << (OParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1778 
                self.dict_entry_list()


            self.state = 1781
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
            if isinstance( listener, OParserListener ):
                listener.enterExpression_tuple(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitExpression_tuple(self)




    def expression_tuple(self):

        localctx = OParser.Expression_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1783 
            self.expression(0)
            self.state = 1784
            self.match(OParser.COMMA)
            self.state = 1793
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (OParser.EXECUTE - 94)) | (1 << (OParser.FETCH - 94)) | (1 << (OParser.FILTERED - 94)) | (1 << (OParser.MUTABLE - 94)) | (1 << (OParser.NULL - 94)) | (1 << (OParser.READ - 94)) | (1 << (OParser.SELF - 94)) | (1 << (OParser.SORTED - 94)) | (1 << (OParser.THIS - 94)) | (1 << (OParser.BOOLEAN_LITERAL - 94)) | (1 << (OParser.CHAR_LITERAL - 94)) | (1 << (OParser.MIN_INTEGER - 94)) | (1 << (OParser.MAX_INTEGER - 94)) | (1 << (OParser.SYMBOL_IDENTIFIER - 94)) | (1 << (OParser.TYPE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (OParser.VARIABLE_IDENTIFIER - 158)) | (1 << (OParser.TEXT_LITERAL - 158)) | (1 << (OParser.UUID_LITERAL - 158)) | (1 << (OParser.INTEGER_LITERAL - 158)) | (1 << (OParser.HEXA_LITERAL - 158)) | (1 << (OParser.DECIMAL_LITERAL - 158)) | (1 << (OParser.DATETIME_LITERAL - 158)) | (1 << (OParser.TIME_LITERAL - 158)) | (1 << (OParser.DATE_LITERAL - 158)) | (1 << (OParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1785 
                self.expression(0)
                self.state = 1790
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==OParser.COMMA:
                    self.state = 1786
                    self.match(OParser.COMMA)
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
            if isinstance( listener, OParserListener ):
                listener.enterDict_entry_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDict_entry_list(self)




    def dict_entry_list(self):

        localctx = OParser.Dict_entry_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1795 
            self.dict_entry()
            self.state = 1800
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1796
                self.match(OParser.COMMA)
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
            if isinstance( listener, OParserListener ):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = OParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1803 
            localctx.key = self.expression(0)
            self.state = 1804
            self.match(OParser.COLON)
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
            if isinstance( listener, OParserListener ):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = OParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_slice_arguments)
        try:
            self.state = 1816
            la_ = self._interp.adaptivePredict(self._input,155,self._ctx)
            if la_ == 1:
                localctx = OParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1807 
                localctx.first = self.expression(0)
                self.state = 1808
                self.match(OParser.COLON)
                self.state = 1809 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = OParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1811 
                localctx.first = self.expression(0)
                self.state = 1812
                self.match(OParser.COLON)
                pass

            elif la_ == 3:
                localctx = OParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1814
                self.match(OParser.COLON)
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
            if isinstance( listener, OParserListener ):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = OParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_assign_variable_statement)
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
            if isinstance( listener, OParserListener ):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a OParser.Assignable_instanceContext)
            super(OParser.RootInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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

            self.state = 1823 
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1829
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,156,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ChildInstanceContext(self, OParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1825
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1826 
                    self.child_instance() 
                self.state = 1831
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
            if isinstance( listener, OParserListener ):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Is_expressionContext)
            super(OParser.IsOtherExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = OParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_is_expression)
        try:
            self.state = 1836
            la_ = self._interp.adaptivePredict(self._input,157,self._ctx)
            if la_ == 1:
                localctx = OParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1832
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1833
                self.match(OParser.VARIABLE_IDENTIFIER)
                self.state = 1834 
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = OParser.IsOtherExpressionContext(self, localctx)
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
            if isinstance( listener, OParserListener ):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = OParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_order_by_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1838 
            self.order_by()
            self.state = 1843
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1839
                self.match(OParser.COMMA)
                self.state = 1840 
                self.order_by()
                self.state = 1845
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
            if isinstance( listener, OParserListener ):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = OParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1846 
            self.variable_identifier()
            self.state = 1851
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.DOT:
                self.state = 1847
                self.match(OParser.DOT)
                self.state = 1848 
                self.variable_identifier()
                self.state = 1853
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1855
            _la = self._input.LA(1)
            if _la==OParser.ASC or _la==OParser.DESC:
                self.state = 1854
                _la = self._input.LA(1)
                if not(_la==OParser.ASC or _la==OParser.DESC):
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
            if isinstance( listener, OParserListener ):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(OParser.DivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(OParser.IdivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(OParser.MultiplyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(OParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(OParser.ModuloContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = OParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_operator)
        try:
            self.state = 1863
            token = self._input.LA(1)
            if token in [OParser.PLUS]:
                localctx = OParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1857
                self.match(OParser.PLUS)

            elif token in [OParser.MINUS]:
                localctx = OParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1858
                self.match(OParser.MINUS)

            elif token in [OParser.STAR]:
                localctx = OParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1859 
                self.multiply()

            elif token in [OParser.SLASH]:
                localctx = OParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1860 
                self.divide()

            elif token in [OParser.BSLASH]:
                localctx = OParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1861 
                self.idivide()

            elif token in [OParser.PERCENT, OParser.MODULO]:
                localctx = OParser.OperatorModuloContext(self, localctx)
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
            super(OParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_new_token

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = OParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1865
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
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
            super(OParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_key_token

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = OParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1868
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
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
            super(OParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_module_token

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = OParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1871
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
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
            super(OParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_value_token

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = OParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1874
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
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
            super(OParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_symbols_token

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = OParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1877
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
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
            super(OParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def getRuleIndex(self):
            return OParser.RULE_assign

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAssign(self)




    def assign(self):

        localctx = OParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1880
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
            if isinstance( listener, OParserListener ):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = OParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1882
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
            if isinstance( listener, OParserListener ):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDivide(self)




    def divide(self):

        localctx = OParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1884
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
            if isinstance( listener, OParserListener ):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = OParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1886
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
            if isinstance( listener, OParserListener ):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitModulo(self)




    def modulo(self):

        localctx = OParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1888
            _la = self._input.LA(1)
            if not(_la==OParser.PERCENT or _la==OParser.MODULO):
                self._errHandler.recoverInline(self)
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
            if isinstance( listener, OParserListener ):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitLfs(self)




    def lfs(self):

        localctx = OParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_lfs)
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
            if isinstance( listener, OParserListener ):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitLfp(self)




    def lfp(self):

        localctx = OParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_lfp)
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = OParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_javascript_statement)
        try:
            self.state = 1901
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1894
                self.match(OParser.RETURN)
                self.state = 1895 
                localctx.exp = self.javascript_expression(0)
                self.state = 1896
                self.match(OParser.SEMI)

            elif token in [OParser.LPAR, OParser.LBRAK, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1898 
                localctx.exp = self.javascript_expression(0)
                self.state = 1899
                self.match(OParser.SEMI)

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
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_expressionContext)
            super(OParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 308
        self.enterRecursionRule(localctx, 308, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1904 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1910
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
                    self.state = 1906
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1907 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1912
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = OParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_javascript_primary_expression)
        try:
            self.state = 1920
            la_ = self._interp.adaptivePredict(self._input,164,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1913 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1914 
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1915 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1916 
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1917 
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1918 
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1919 
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = OParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1922 
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = OParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1924 
            self.new_token()
            self.state = 1925 
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_selector_expressionContext)
            super(OParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = OParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_javascript_selector_expression)
        try:
            self.state = 1932
            la_ = self._interp.adaptivePredict(self._input,165,self._ctx)
            if la_ == 1:
                localctx = OParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1927
                self.match(OParser.DOT)
                self.state = 1928 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = OParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1929
                self.match(OParser.DOT)
                self.state = 1930 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = OParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1931 
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = OParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1934 
            localctx.name = self.javascript_identifier()
            self.state = 1935
            self.match(OParser.LPAR)
            self.state = 1937
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.READ - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.BOOLEAN_LITERAL - 128)) | (1 << (OParser.CHAR_LITERAL - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)) | (1 << (OParser.DOLLAR_IDENTIFIER - 128)) | (1 << (OParser.TEXT_LITERAL - 128)) | (1 << (OParser.INTEGER_LITERAL - 128)) | (1 << (OParser.DECIMAL_LITERAL - 128)))) != 0):
                self.state = 1936 
                localctx.args = self.javascript_arguments(0)


            self.state = 1939
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 320
        self.enterRecursionRule(localctx, 320, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1942 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1949
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
                    self.state = 1944
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1945
                    self.match(OParser.COMMA)
                    self.state = 1946 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1951
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = OParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1952
            self.match(OParser.LBRAK)
            self.state = 1953 
            localctx.exp = self.javascript_expression(0)
            self.state = 1954
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = OParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1956
            self.match(OParser.LPAR)
            self.state = 1957 
            localctx.exp = self.javascript_expression(0)
            self.state = 1958
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = OParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1960 
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
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = OParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_javascript_literal_expression)
        try:
            self.state = 1967
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1962
                localctx.t = self.match(OParser.INTEGER_LITERAL)

            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1963
                localctx.t = self.match(OParser.DECIMAL_LITERAL)

            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1964
                localctx.t = self.match(OParser.TEXT_LITERAL)

            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1965
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)

            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1966
                localctx.t = self.match(OParser.CHAR_LITERAL)

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

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def getRuleIndex(self):
            return OParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = OParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1969
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.READ - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)) | (1 << (OParser.DOLLAR_IDENTIFIER - 128)))) != 0)):
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = OParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_python_statement)
        try:
            self.state = 1974
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1971
                self.match(OParser.RETURN)
                self.state = 1972 
                localctx.exp = self.python_expression(0)

            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1973 
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_expressionContext)
            super(OParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(OParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 334
        self.enterRecursionRule(localctx, 334, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1977 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1983
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
                    self.state = 1979
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1980 
                    localctx.child = self.python_selector_expression() 
                self.state = 1985
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonIdentifierExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(OParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(OParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = OParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_python_primary_expression)
        try:
            self.state = 1990
            la_ = self._interp.adaptivePredict(self._input,171,self._ctx)
            if la_ == 1:
                localctx = OParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1986 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = OParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1987 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = OParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1988 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = OParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1989 
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = OParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_python_selector_expression)
        try:
            self.state = 1998
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1992
                self.match(OParser.DOT)
                self.state = 1993 
                localctx.exp = self.python_method_expression()

            elif token in [OParser.LBRAK]:
                localctx = OParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1994
                self.match(OParser.LBRAK)
                self.state = 1995 
                localctx.exp = self.python_expression(0)
                self.state = 1996
                self.match(OParser.RBRAK)

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
            if isinstance( listener, OParserListener ):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = OParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2000 
            localctx.name = self.python_identifier()
            self.state = 2001
            self.match(OParser.LPAR)
            self.state = 2003
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.READ - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.BOOLEAN_LITERAL - 128)) | (1 << (OParser.CHAR_LITERAL - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)) | (1 << (OParser.DOLLAR_IDENTIFIER - 128)) | (1 << (OParser.TEXT_LITERAL - 128)) | (1 << (OParser.INTEGER_LITERAL - 128)) | (1 << (OParser.DECIMAL_LITERAL - 128)))) != 0):
                self.state = 2002 
                localctx.args = self.python_argument_list()


            self.state = 2005
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_argument_listContext)
            super(OParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = OParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_python_argument_list)
        try:
            self.state = 2013
            la_ = self._interp.adaptivePredict(self._input,174,self._ctx)
            if la_ == 1:
                localctx = OParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2007 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = OParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2008 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = OParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2009 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2010
                self.match(OParser.COMMA)
                self.state = 2011 
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 344
        self.enterRecursionRule(localctx, 344, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2016 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2023
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
                    self.state = 2018
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2019
                    self.match(OParser.COMMA)
                    self.state = 2020 
                    localctx.item = self.python_expression(0) 
                self.state = 2025
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 346
        self.enterRecursionRule(localctx, 346, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2027 
            localctx.name = self.python_identifier()
            self.state = 2028
            self.match(OParser.EQ)
            self.state = 2029 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2039
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
                    self.state = 2031
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2032
                    self.match(OParser.COMMA)
                    self.state = 2033 
                    localctx.name = self.python_identifier()
                    self.state = 2034
                    self.match(OParser.EQ)
                    self.state = 2035 
                    localctx.exp = self.python_expression(0) 
                self.state = 2041
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
            if isinstance( listener, OParserListener ):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = OParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2042
            self.match(OParser.LPAR)
            self.state = 2043 
            localctx.exp = self.python_expression(0)
            self.state = 2044
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_identifier_expressionContext)
            super(OParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_identifier_expressionContext)
            super(OParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2049
            token = self._input.LA(1)
            if token in [OParser.DOLLAR_IDENTIFIER]:
                localctx = OParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2047
                self.match(OParser.DOLLAR_IDENTIFIER)

            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2048 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2056
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
                    self.state = 2051
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2052
                    self.match(OParser.DOT)
                    self.state = 2053 
                    localctx.name = self.python_identifier() 
                self.state = 2058
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
            if isinstance( listener, OParserListener ):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = OParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_python_literal_expression)
        try:
            self.state = 2064
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2059
                localctx.t = self.match(OParser.INTEGER_LITERAL)

            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2060
                localctx.t = self.match(OParser.DECIMAL_LITERAL)

            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2061
                localctx.t = self.match(OParser.TEXT_LITERAL)

            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2062
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)

            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2063
                localctx.t = self.match(OParser.CHAR_LITERAL)

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

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def THIS(self):
            return self.getToken(OParser.THIS, 0)

        def getRuleIndex(self):
            return OParser.RULE_python_identifier

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = OParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2066
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.READ - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)))) != 0)):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = OParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_java_statement)
        try:
            self.state = 2075
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2068
                self.match(OParser.RETURN)
                self.state = 2069 
                localctx.exp = self.java_expression(0)
                self.state = 2070
                self.match(OParser.SEMI)

            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.NATIVE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2072 
                localctx.exp = self.java_expression(0)
                self.state = 2073
                self.match(OParser.SEMI)

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
            if isinstance( listener, OParserListener ):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_expressionContext)
            super(OParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(OParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 358
        self.enterRecursionRule(localctx, 358, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2078 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2084
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
                    self.state = 2080
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2081 
                    localctx.child = self.java_selector_expression() 
                self.state = 2086
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
            if isinstance( listener, OParserListener ):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = OParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_java_primary_expression)
        try:
            self.state = 2092
            la_ = self._interp.adaptivePredict(self._input,182,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2087 
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2088 
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2089 
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2090 
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2091 
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
            if isinstance( listener, OParserListener ):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = OParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2094 
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
            if isinstance( listener, OParserListener ):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = OParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2096 
            self.new_token()
            self.state = 2097 
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = OParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_java_selector_expression)
        try:
            self.state = 2102
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2099
                self.match(OParser.DOT)
                self.state = 2100 
                localctx.exp = self.java_method_expression()

            elif token in [OParser.LBRAK]:
                localctx = OParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2101 
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
            if isinstance( listener, OParserListener ):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = OParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2104 
            localctx.name = self.java_identifier()
            self.state = 2105
            self.match(OParser.LPAR)
            self.state = 2107
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.READ - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.BOOLEAN_LITERAL - 128)) | (1 << (OParser.CHAR_LITERAL - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)) | (1 << (OParser.NATIVE_IDENTIFIER - 128)) | (1 << (OParser.DOLLAR_IDENTIFIER - 128)) | (1 << (OParser.TEXT_LITERAL - 128)) | (1 << (OParser.INTEGER_LITERAL - 128)) | (1 << (OParser.DECIMAL_LITERAL - 128)))) != 0):
                self.state = 2106 
                localctx.args = self.java_arguments(0)


            self.state = 2109
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_argumentsContext)
            super(OParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 370
        self.enterRecursionRule(localctx, 370, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2112 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2119
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
                    self.state = 2114
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2115
                    self.match(OParser.COMMA)
                    self.state = 2116 
                    localctx.item = self.java_expression(0) 
                self.state = 2121
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
            if isinstance( listener, OParserListener ):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = OParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2122
            self.match(OParser.LBRAK)
            self.state = 2123 
            localctx.exp = self.java_expression(0)
            self.state = 2124
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
            if isinstance( listener, OParserListener ):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = OParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2126
            self.match(OParser.LPAR)
            self.state = 2127 
            localctx.exp = self.java_expression(0)
            self.state = 2128
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 376
        self.enterRecursionRule(localctx, 376, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2131 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2138
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
                    self.state = 2133
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2134
                    self.match(OParser.DOT)
                    self.state = 2135 
                    localctx.name = self.java_identifier() 
                self.state = 2140
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 378
        self.enterRecursionRule(localctx, 378, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2142 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2148
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
                    self.state = 2144
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2145
                    localctx.name = self.match(OParser.DOLLAR_IDENTIFIER) 
                self.state = 2150
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
            if isinstance( listener, OParserListener ):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = OParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_java_literal_expression)
        try:
            self.state = 2156
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2151
                localctx.t = self.match(OParser.INTEGER_LITERAL)

            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2152
                localctx.t = self.match(OParser.DECIMAL_LITERAL)

            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2153
                localctx.t = self.match(OParser.TEXT_LITERAL)

            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2154
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)

            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2155
                localctx.t = self.match(OParser.CHAR_LITERAL)

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

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def getRuleIndex(self):
            return OParser.RULE_java_identifier

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = OParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2158
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.READ - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)) | (1 << (OParser.NATIVE_IDENTIFIER - 128)) | (1 << (OParser.DOLLAR_IDENTIFIER - 128)))) != 0)):
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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = OParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_csharp_statement)
        try:
            self.state = 2167
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2160
                self.match(OParser.RETURN)
                self.state = 2161 
                localctx.exp = self.csharp_expression(0)
                self.state = 2162
                self.match(OParser.SEMI)

            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2164 
                localctx.exp = self.csharp_expression(0)
                self.state = 2165
                self.match(OParser.SEMI)

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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_expressionContext)
            super(OParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 386
        self.enterRecursionRule(localctx, 386, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2170 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2176
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
                    self.state = 2172
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2173 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2178
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
            if isinstance( listener, OParserListener ):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = OParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_csharp_primary_expression)
        try:
            self.state = 2184
            la_ = self._interp.adaptivePredict(self._input,191,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2179 
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2180 
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2181 
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2182 
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2183 
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
            if isinstance( listener, OParserListener ):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = OParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2186 
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
            if isinstance( listener, OParserListener ):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = OParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2188 
            self.new_token()
            self.state = 2189 
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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_selector_expressionContext)
            super(OParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = OParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_csharp_selector_expression)
        try:
            self.state = 2194
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2191
                self.match(OParser.DOT)
                self.state = 2192 
                localctx.exp = self.csharp_method_expression()

            elif token in [OParser.LBRAK]:
                localctx = OParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2193 
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
            if isinstance( listener, OParserListener ):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = OParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2196 
            localctx.name = self.csharp_identifier()
            self.state = 2197
            self.match(OParser.LPAR)
            self.state = 2199
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.READ - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.BOOLEAN_LITERAL - 128)) | (1 << (OParser.CHAR_LITERAL - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)) | (1 << (OParser.DOLLAR_IDENTIFIER - 128)) | (1 << (OParser.TEXT_LITERAL - 128)) | (1 << (OParser.INTEGER_LITERAL - 128)) | (1 << (OParser.DECIMAL_LITERAL - 128)))) != 0):
                self.state = 2198 
                localctx.args = self.csharp_arguments(0)


            self.state = 2201
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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 398
        self.enterRecursionRule(localctx, 398, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2204 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2211
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
                    self.state = 2206
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2207
                    self.match(OParser.COMMA)
                    self.state = 2208 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2213
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
            if isinstance( listener, OParserListener ):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = OParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2214
            self.match(OParser.LBRAK)
            self.state = 2215 
            localctx.exp = self.csharp_expression(0)
            self.state = 2216
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
            if isinstance( listener, OParserListener ):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = OParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2218
            self.match(OParser.LPAR)
            self.state = 2219 
            localctx.exp = self.csharp_expression(0)
            self.state = 2220
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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_identifier_expressionContext)
            super(OParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 404
        self.enterRecursionRule(localctx, 404, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2225
            token = self._input.LA(1)
            if token in [OParser.DOLLAR_IDENTIFIER]:
                localctx = OParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2223
                self.match(OParser.DOLLAR_IDENTIFIER)

            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.TEST, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2224 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2232
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
                    self.state = 2227
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2228
                    self.match(OParser.DOT)
                    self.state = 2229 
                    localctx.name = self.csharp_identifier() 
                self.state = 2234
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
            if isinstance( listener, OParserListener ):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = OParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_csharp_literal_expression)
        try:
            self.state = 2240
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2235
                self.match(OParser.INTEGER_LITERAL)

            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2236
                self.match(OParser.DECIMAL_LITERAL)

            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2237
                self.match(OParser.TEXT_LITERAL)

            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2238
                self.match(OParser.BOOLEAN_LITERAL)

            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2239
                self.match(OParser.CHAR_LITERAL)

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

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def getRuleIndex(self):
            return OParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = OParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.READ - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)))) != 0)):
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
        self._predicates[7] = self.derived_list_sempred
        self._predicates[17] = self.native_category_binding_list_sempred
        self._predicates[36] = self.else_if_statement_list_sempred
        self._predicates[44] = self.callable_parent_sempred
        self._predicates[46] = self.expression_sempred
        self._predicates[47] = self.an_expression_sempred
        self._predicates[49] = self.instance_expression_sempred
        self._predicates[60] = self.argument_assignment_list_sempred
        self._predicates[79] = self.typedef_sempred
        self._predicates[99] = self.any_type_sempred
        self._predicates[136] = self.assignable_instance_sempred
        self._predicates[137] = self.is_expression_sempred
        self._predicates[141] = self.new_token_sempred
        self._predicates[142] = self.key_token_sempred
        self._predicates[143] = self.module_token_sempred
        self._predicates[144] = self.value_token_sempred
        self._predicates[145] = self.symbols_token_sempred
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
                return self.precpred(self._ctx, 32)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 1)
         

    def an_expression_sempred(self, localctx, predIndex):
            if predIndex == 32:
                return self.willBeAOrAn()
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 33:
                return self.precpred(self._ctx, 1)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 34:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 35:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 37:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 38:
                return self.precpred(self._ctx, 3)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 40:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 43:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 44:
                return self.isText(localctx.i1,"key")
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 45:
                return self.isText(localctx.i1,"module")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         



