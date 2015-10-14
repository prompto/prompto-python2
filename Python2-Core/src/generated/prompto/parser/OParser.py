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
        buf.write(u"\u009b\u0827\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0188\n\2\3\2\3\2\5")
        buf.write(u"\2\u018c\n\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\6\5\6\u01a7\n\6\3\6\3\6\3\6\3\6\3\6\5\6\u01ae")
        buf.write(u"\n\6\3\6\3\6\3\7\5\7\u01b3\n\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write(u"\7\5\7\u01bb\n\7\3\7\3\7\5\7\u01bf\n\7\3\7\3\7\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\5\b\u01c9\n\b\3\b\3\b\3\t\3\t\3\t")
        buf.write(u"\3\t\3\t\3\t\7\t\u01d3\n\t\f\t\16\t\u01d6\13\t\3\n\3")
        buf.write(u"\n\3\n\5\n\u01db\n\n\3\n\5\n\u01de\n\n\3\13\5\13\u01e1")
        buf.write(u"\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u01ea\n")
        buf.write(u"\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u01f2\n\f\3\f\3\f\3")
        buf.write(u"\r\3\r\3\r\3\r\5\r\u01fa\n\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write(u"\16\3\16\3\16\3\16\5\16\u0205\n\16\3\16\3\16\3\16\5\16")
        buf.write(u"\u020a\n\16\3\16\3\16\3\17\5\17\u020f\n\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\5\17\u0218\n\17\3\17\3\17\3")
        buf.write(u"\17\5\17\u021d\n\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u022f")
        buf.write(u"\n\21\f\21\16\21\u0232\13\21\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\7\22\u023a\n\22\f\22\16\22\u023d\13\22\3\23\3\23")
        buf.write(u"\5\23\u0241\n\23\3\23\3\23\3\23\3\23\5\23\u0247\n\23")
        buf.write(u"\3\23\3\23\3\23\3\24\5\24\u024d\n\24\3\24\3\24\3\24\3")
        buf.write(u"\24\5\24\u0253\n\24\3\24\3\24\3\24\5\24\u0258\n\24\3")
        buf.write(u"\24\3\24\3\25\5\25\u025d\n\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\5\25\u0264\n\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\5\26\u027b\n\26\3\27\3\27\3\27\3\30\3")
        buf.write(u"\30\3\30\3\30\3\30\5\30\u0285\n\30\3\30\3\30\3\30\5\30")
        buf.write(u"\u028a\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u0291\n\31")
        buf.write(u"\5\31\u0293\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write(u"\5\32\u02a7\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u02c4")
        buf.write(u"\n\36\5\36\u02c6\n\36\3\36\3\36\3\37\3\37\3\37\3\37\5")
        buf.write(u"\37\u02ce\n\37\3\37\3\37\3\37\3\37\3\37\5\37\u02d5\n")
        buf.write(u"\37\5\37\u02d7\n\37\3 \3 \3 \3 \3 \3 \5 \u02df\n \3 ")
        buf.write(u"\3 \3 \3 \3 \3!\3!\3!\5!\u02e9\n!\3!\3!\3!\3!\3!\3!\3")
        buf.write(u"!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\5#\u02fe")
        buf.write(u"\n#\3#\3#\5#\u0302\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write(u"$\3$\3$\3$\3$\3$\7$\u0314\n$\f$\16$\u0317\13$\3%\3%\3")
        buf.write(u"%\3%\3&\3&\3&\3&\3&\3&\5&\u0323\n&\3&\3&\5&\u0327\n&")
        buf.write(u"\3&\3&\3&\3&\3&\3&\5&\u032f\n&\3&\5&\u0332\n&\3&\3&\3")
        buf.write(u"&\5&\u0337\n&\3&\5&\u033a\n&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\5\'\u0342\n\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5")
        buf.write(u"\'\u034d\n\'\3\'\3\'\5\'\u0351\n\'\3(\3(\5(\u0355\n(")
        buf.write(u"\3(\3(\3)\3)\3)\5)\u035c\n)\3)\3)\3*\3*\3*\3*\3*\5*\u0365")
        buf.write(u"\n*\3+\3+\3+\3+\3+\7+\u036c\n+\f+\16+\u036f\13+\3,\3")
        buf.write(u",\3,\3,\3,\3,\5,\u0377\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0390\n")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\7-\u03f4\n-\f-\16-")
        buf.write(u"\u03f7\13-\3.\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\7\60\u0404\n\60\f\60\16\60\u0407\13\60\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\5\61\u040f\n\61\3\62\3\62\3\62\3\62\3")
        buf.write(u"\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write(u"\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write(u"\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write(u"\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u043b\n\65\3\65\3")
        buf.write(u"\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0445\n\65\5\65")
        buf.write(u"\u0447\n\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5")
        buf.write(u"\66\u0451\n\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\5\67\u045f\n\67\38\58\u0462\n8\3")
        buf.write(u"8\38\38\58\u0467\n8\38\38\39\39\39\39\39\59\u0470\n9")
        buf.write(u"\39\39\39\79\u0475\n9\f9\169\u0478\139\3:\3:\3:\3:\3")
        buf.write(u";\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\5<\u0489\n<\3=\3=\3=")
        buf.write(u"\3=\3=\3>\3>\3?\5?\u0493\n?\3?\3?\3?\3@\3@\3@\3@\3@\3")
        buf.write(u"@\3@\7@\u049f\n@\f@\16@\u04a2\13@\3A\3A\3A\3A\3A\5A\u04a9")
        buf.write(u"\nA\3B\3B\3C\3C\5C\u04af\nC\3D\3D\3D\3D\3D\3D\3D\7D\u04b8")
        buf.write(u"\nD\fD\16D\u04bb\13D\3E\3E\3E\3E\3E\3E\3E\7E\u04c4\n")
        buf.write(u"E\fE\16E\u04c7\13E\3F\3F\3F\3F\3F\3F\7F\u04cf\nF\fF\16")
        buf.write(u"F\u04d2\13F\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u04de\n")
        buf.write(u"G\3H\3H\5H\u04e2\nH\3H\3H\3I\3I\5I\u04e8\nI\3I\3I\3J")
        buf.write(u"\3J\3J\3J\3J\3J\7J\u04f2\nJ\fJ\16J\u04f5\13J\3K\3K\3")
        buf.write(u"K\3K\3K\3K\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\7L\u0508")
        buf.write(u"\nL\fL\16L\u050b\13L\3M\3M\5M\u050f\nM\3N\3N\3N\3N\3")
        buf.write(u"N\3N\3N\3N\3N\3N\5N\u051b\nN\3O\3O\3P\3P\3Q\3Q\3R\3R")
        buf.write(u"\3R\5R\u0526\nR\3S\3S\3S\3S\3S\3S\7S\u052e\nS\fS\16S")
        buf.write(u"\u0531\13S\3T\3T\5T\u0535\nT\3U\3U\3U\5U\u053a\nU\3V")
        buf.write(u"\3V\3W\3W\3X\3X\3Y\3Y\3Y\3Y\3Y\3Y\7Y\u0548\nY\fY\16Y")
        buf.write(u"\u054b\13Y\3Z\3Z\5Z\u054f\nZ\3Z\5Z\u0552\nZ\3[\3[\5[")
        buf.write(u"\u0556\n[\3\\\3\\\3\\\5\\\u055b\n\\\3]\3]\3]\3^\3^\5")
        buf.write(u"^\u0562\n^\3_\3_\3_\3_\3_\3_\3_\3_\3_\7_\u056d\n_\f_")
        buf.write(u"\16_\u0570\13_\3`\3`\3`\3`\3`\3`\3`\7`\u0579\n`\f`\16")
        buf.write(u"`\u057c\13`\3a\3a\3a\3a\3a\5a\u0583\na\3b\3b\3b\3b\3")
        buf.write(u"b\3b\3b\7b\u058c\nb\fb\16b\u058f\13b\3c\3c\5c\u0593\n")
        buf.write(u"c\3d\3d\3d\3d\3d\3d\3d\3d\3d\3d\5d\u059f\nd\3e\3e\5e")
        buf.write(u"\u05a3\ne\3f\3f\3f\3f\3f\3f\7f\u05ab\nf\ff\16f\u05ae")
        buf.write(u"\13f\3g\3g\3g\3h\3h\5h\u05b5\nh\3i\3i\3i\3i\5i\u05bb")
        buf.write(u"\ni\3i\3i\3i\7i\u05c0\ni\fi\16i\u05c3\13i\3i\3i\5i\u05c7")
        buf.write(u"\ni\3j\3j\3j\3j\3j\3j\7j\u05cf\nj\fj\16j\u05d2\13j\3")
        buf.write(u"k\3k\3k\3k\5k\u05d8\nk\3l\3l\3l\3l\3l\3l\3l\7l\u05e1")
        buf.write(u"\nl\fl\16l\u05e4\13l\3m\3m\3m\3m\3m\3m\3m\3m\3m\3m\5")
        buf.write(u"m\u05f0\nm\3n\3n\5n\u05f4\nn\3n\5n\u05f7\nn\3o\3o\5o")
        buf.write(u"\u05fb\no\3o\5o\u05fe\no\3p\3p\3p\3p\3p\3p\3p\7p\u0607")
        buf.write(u"\np\fp\16p\u060a\13p\3q\3q\3q\3q\3q\3q\3q\7q\u0613\n")
        buf.write(u"q\fq\16q\u0616\13q\3r\3r\3r\3r\3r\3r\3r\7r\u061f\nr\f")
        buf.write(u"r\16r\u0622\13r\3s\3s\3s\3s\3s\3s\3s\7s\u062b\ns\fs\16")
        buf.write(u"s\u062e\13s\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3")
        buf.write(u"t\5t\u063e\nt\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u")
        buf.write(u"\5u\u064d\nu\3v\3v\3v\3v\3v\3v\7v\u0655\nv\fv\16v\u0658")
        buf.write(u"\13v\3w\3w\3w\3w\5w\u065e\nw\3x\3x\3y\3y\3y\3y\3z\3z")
        buf.write(u"\5z\u0668\nz\3{\3{\3{\3{\3{\5{\u066f\n{\3|\3|\5|\u0673")
        buf.write(u"\n|\3|\3|\3}\3}\5}\u0679\n}\3}\3}\3~\3~\3~\3~\3~\3~\7")
        buf.write(u"~\u0683\n~\f~\16~\u0686\13~\3\177\3\177\3\177\3\177\3")
        buf.write(u"\177\3\177\7\177\u068e\n\177\f\177\16\177\u0691\13\177")
        buf.write(u"\3\u0080\3\u0080\3\u0080\3\u0080\3\u0081\3\u0081\3\u0081")
        buf.write(u"\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\5\u0081")
        buf.write(u"\u06a0\n\u0081\3\u0082\3\u0082\3\u0082\3\u0082\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0083\7\u0083\u06ab\n\u0083")
        buf.write(u"\f\u0083\16\u0083\u06ae\13\u0083\3\u0084\3\u0084\3\u0084")
        buf.write(u"\3\u0084\5\u0084\u06b4\n\u0084\3\u0085\3\u0085\3\u0085")
        buf.write(u"\3\u0085\3\u0085\3\u0085\5\u0085\u06bc\n\u0085\3\u0086")
        buf.write(u"\3\u0086\3\u0086\3\u0087\3\u0087\3\u0087\3\u0088\3\u0088")
        buf.write(u"\3\u0088\3\u0089\3\u0089\3\u008a\3\u008a\3\u008b\3\u008b")
        buf.write(u"\3\u008c\3\u008c\3\u008d\3\u008d\3\u008e\3\u008e\3\u008f")
        buf.write(u"\3\u008f\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090")
        buf.write(u"\3\u0090\5\u0090\u06dc\n\u0090\3\u0091\3\u0091\3\u0091")
        buf.write(u"\3\u0091\3\u0091\7\u0091\u06e3\n\u0091\f\u0091\16\u0091")
        buf.write(u"\u06e6\13\u0091\3\u0092\3\u0092\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0092\5\u0092\u06ee\n\u0092\3\u0093\3\u0093\3\u0094")
        buf.write(u"\3\u0094\3\u0094\3\u0094\3\u0094\5\u0094\u06f7\n\u0094")
        buf.write(u"\3\u0095\3\u0095\3\u0095\5\u0095\u06fc\n\u0095\3\u0095")
        buf.write(u"\3\u0095\3\u0096\3\u0096\3\u0096\3\u0096\3\u0096\3\u0096")
        buf.write(u"\7\u0096\u0706\n\u0096\f\u0096\16\u0096\u0709\13\u0096")
        buf.write(u"\3\u0097\3\u0097\3\u0097\3\u0097\3\u0098\3\u0098\3\u0098")
        buf.write(u"\3\u0098\3\u0099\3\u0099\3\u009a\3\u009a\3\u009a\3\u009a")
        buf.write(u"\3\u009a\5\u009a\u071a\n\u009a\3\u009b\3\u009b\3\u009c")
        buf.write(u"\3\u009c\3\u009c\5\u009c\u0721\n\u009c\3\u009d\3\u009d")
        buf.write(u"\3\u009d\3\u009d\3\u009d\7\u009d\u0728\n\u009d\f\u009d")
        buf.write(u"\16\u009d\u072b\13\u009d\3\u009e\3\u009e\3\u009e\3\u009e")
        buf.write(u"\5\u009e\u0731\n\u009e\3\u009f\3\u009f\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\5\u009f\u0739\n\u009f\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a0\5\u00a0\u073e\n\u00a0\3\u00a0\3\u00a0\3\u00a1")
        buf.write(u"\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\5\u00a1\u0748")
        buf.write(u"\n\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2\3\u00a2\3\u00a2")
        buf.write(u"\7\u00a2\u0750\n\u00a2\f\u00a2\16\u00a2\u0753\13\u00a2")
        buf.write(u"\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\3\u00a3\3\u00a3\3\u00a3\7\u00a3\u0760\n\u00a3")
        buf.write(u"\f\u00a3\16\u00a3\u0763\13\u00a3\3\u00a4\3\u00a4\3\u00a4")
        buf.write(u"\3\u00a4\3\u00a5\3\u00a5\3\u00a5\5\u00a5\u076c\n\u00a5")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\7\u00a5\u0771\n\u00a5\f\u00a5")
        buf.write(u"\16\u00a5\u0774\13\u00a5\3\u00a6\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a6\5\u00a6\u077b\n\u00a6\3\u00a7\3\u00a7\3\u00a8")
        buf.write(u"\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8\5\u00a8")
        buf.write(u"\u0786\n\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\7\u00a9\u078d\n\u00a9\f\u00a9\16\u00a9\u0790\13\u00a9")
        buf.write(u"\3\u00aa\3\u00aa\3\u00aa\3\u00aa\5\u00aa\u0796\n\u00aa")
        buf.write(u"\3\u00ab\3\u00ab\3\u00ac\3\u00ac\3\u00ac\5\u00ac\u079d")
        buf.write(u"\n\u00ac\3\u00ad\3\u00ad\3\u00ad\5\u00ad\u07a2\n\u00ad")
        buf.write(u"\3\u00ad\3\u00ad\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\3\u00ae\7\u00ae\u07ac\n\u00ae\f\u00ae\16\u00ae\u07af")
        buf.write(u"\13\u00ae\3\u00af\3\u00af\3\u00af\3\u00af\3\u00b0\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\7\u00b1\u07bf\n\u00b1\f\u00b1\16\u00b1\u07c2")
        buf.write(u"\13\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\7\u00b2")
        buf.write(u"\u07c9\n\u00b2\f\u00b2\16\u00b2\u07cc\13\u00b2\3\u00b3")
        buf.write(u"\3\u00b3\3\u00b3\3\u00b3\3\u00b3\5\u00b3\u07d3\n\u00b3")
        buf.write(u"\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\3\u00b5\5\u00b5\u07de\n\u00b5\3\u00b6\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\7\u00b6\u07e5\n\u00b6\f\u00b6")
        buf.write(u"\16\u00b6\u07e8\13\u00b6\3\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write(u"\5\u00b7\u07ee\n\u00b7\3\u00b8\3\u00b8\3\u00b9\3\u00b9")
        buf.write(u"\3\u00b9\5\u00b9\u07f5\n\u00b9\3\u00ba\3\u00ba\3\u00ba")
        buf.write(u"\5\u00ba\u07fa\n\u00ba\3\u00ba\3\u00ba\3\u00bb\3\u00bb")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\3\u00bb\7\u00bb\u0804\n\u00bb")
        buf.write(u"\f\u00bb\16\u00bb\u0807\13\u00bb\3\u00bc\3\u00bc\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00be\3\u00be")
        buf.write(u"\3\u00be\5\u00be\u0814\n\u00be\3\u00be\3\u00be\3\u00be")
        buf.write(u"\7\u00be\u0819\n\u00be\f\u00be\16\u00be\u081c\13\u00be")
        buf.write(u"\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf\5\u00bf\u0823")
        buf.write(u"\n\u00bf\3\u00c0\3\u00c0\3\u00c0\2,\20 \"FTX^p~\u0086")
        buf.write(u"\u0088\u008a\u0092\u0096\u00a4\u00b0\u00bc\u00be\u00c2")
        buf.write(u"\u00d2\u00d6\u00de\u00e0\u00e2\u00e4\u00ea\u00fa\u00fc")
        buf.write(u"\u0104\u0120\u012a\u0138\u0142\u0144\u0148\u0150\u015a")
        buf.write(u"\u0160\u0162\u016a\u0174\u017a\u00c1\2\4\6\b\n\f\16\20")
        buf.write(u"\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJ")
        buf.write(u"LNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write(u"\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a")
        buf.write(u"\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac")
        buf.write(u"\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be")
        buf.write(u"\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0")
        buf.write(u"\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2")
        buf.write(u"\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4")
        buf.write(u"\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106")
        buf.write(u"\u0108\u010a\u010c\u010e\u0110\u0112\u0114\u0116\u0118")
        buf.write(u"\u011a\u011c\u011e\u0120\u0122\u0124\u0126\u0128\u012a")
        buf.write(u"\u012c\u012e\u0130\u0132\u0134\u0136\u0138\u013a\u013c")
        buf.write(u"\u013e\u0140\u0142\u0144\u0146\u0148\u014a\u014c\u014e")
        buf.write(u"\u0150\u0152\u0154\u0156\u0158\u015a\u015c\u015e\u0160")
        buf.write(u"\u0162\u0164\u0166\u0168\u016a\u016c\u016e\u0170\u0172")
        buf.write(u"\u0174\u0176\u0178\u017a\u017c\u017e\2\t\3\2\35\36\4")
        buf.write(u"\2yy\u0081\u0081\4\2\"\"dd\b\2/\67ss\u0080\u0080\u0089")
        buf.write(u"\u0089\u008e\u0090\u0092\u0092\b\2/\67ssyy\u0080\u0081")
        buf.write(u"\u0089\u0089\u008e\u0090\7\2/\67ss\u0080\u0080\u0089")
        buf.write(u"\u0089\u008e\u0092\7\2/\67ss\u0080\u0080\u0089\u0089")
        buf.write(u"\u008e\u0090\u0892\2\u0180\3\2\2\2\4\u0191\3\2\2\2\6")
        buf.write(u"\u019a\3\2\2\2\b\u01a0\3\2\2\2\n\u01a6\3\2\2\2\f\u01b2")
        buf.write(u"\3\2\2\2\16\u01c2\3\2\2\2\20\u01cc\3\2\2\2\22\u01dd\3")
        buf.write(u"\2\2\2\24\u01e0\3\2\2\2\26\u01ed\3\2\2\2\30\u01f5\3\2")
        buf.write(u"\2\2\32\u01fd\3\2\2\2\34\u020e\3\2\2\2\36\u0220\3\2\2")
        buf.write(u"\2 \u0226\3\2\2\2\"\u0233\3\2\2\2$\u023e\3\2\2\2&\u024c")
        buf.write(u"\3\2\2\2(\u025c\3\2\2\2*\u026a\3\2\2\2,\u027c\3\2\2\2")
        buf.write(u".\u027f\3\2\2\2\60\u0292\3\2\2\2\62\u02a6\3\2\2\2\64")
        buf.write(u"\u02a8\3\2\2\2\66\u02ae\3\2\2\28\u02b4\3\2\2\2:\u02ba")
        buf.write(u"\3\2\2\2<\u02d6\3\2\2\2>\u02d8\3\2\2\2@\u02e5\3\2\2\2")
        buf.write(u"B\u02f1\3\2\2\2D\u02f7\3\2\2\2F\u0303\3\2\2\2H\u0318")
        buf.write(u"\3\2\2\2J\u031c\3\2\2\2L\u0350\3\2\2\2N\u0352\3\2\2\2")
        buf.write(u"P\u0358\3\2\2\2R\u0364\3\2\2\2T\u0366\3\2\2\2V\u0376")
        buf.write(u"\3\2\2\2X\u038f\3\2\2\2Z\u03f8\3\2\2\2\\\u03fc\3\2\2")
        buf.write(u"\2^\u03fe\3\2\2\2`\u040e\3\2\2\2b\u0410\3\2\2\2d\u0414")
        buf.write(u"\3\2\2\2f\u0418\3\2\2\2h\u0446\3\2\2\2j\u0448\3\2\2\2")
        buf.write(u"l\u045e\3\2\2\2n\u0461\3\2\2\2p\u046f\3\2\2\2r\u0479")
        buf.write(u"\3\2\2\2t\u047d\3\2\2\2v\u0488\3\2\2\2x\u048a\3\2\2\2")
        buf.write(u"z\u048f\3\2\2\2|\u0492\3\2\2\2~\u0497\3\2\2\2\u0080\u04a8")
        buf.write(u"\3\2\2\2\u0082\u04aa\3\2\2\2\u0084\u04ae\3\2\2\2\u0086")
        buf.write(u"\u04b0\3\2\2\2\u0088\u04bc\3\2\2\2\u008a\u04c8\3\2\2")
        buf.write(u"\2\u008c\u04dd\3\2\2\2\u008e\u04df\3\2\2\2\u0090\u04e5")
        buf.write(u"\3\2\2\2\u0092\u04eb\3\2\2\2\u0094\u04f6\3\2\2\2\u0096")
        buf.write(u"\u04fc\3\2\2\2\u0098\u050e\3\2\2\2\u009a\u051a\3\2\2")
        buf.write(u"\2\u009c\u051c\3\2\2\2\u009e\u051e\3\2\2\2\u00a0\u0520")
        buf.write(u"\3\2\2\2\u00a2\u0525\3\2\2\2\u00a4\u0527\3\2\2\2\u00a6")
        buf.write(u"\u0534\3\2\2\2\u00a8\u0539\3\2\2\2\u00aa\u053b\3\2\2")
        buf.write(u"\2\u00ac\u053d\3\2\2\2\u00ae\u053f\3\2\2\2\u00b0\u0541")
        buf.write(u"\3\2\2\2\u00b2\u0551\3\2\2\2\u00b4\u0555\3\2\2\2\u00b6")
        buf.write(u"\u0557\3\2\2\2\u00b8\u055c\3\2\2\2\u00ba\u0561\3\2\2")
        buf.write(u"\2\u00bc\u0563\3\2\2\2\u00be\u0571\3\2\2\2\u00c0\u0582")
        buf.write(u"\3\2\2\2\u00c2\u0584\3\2\2\2\u00c4\u0592\3\2\2\2\u00c6")
        buf.write(u"\u059e\3\2\2\2\u00c8\u05a0\3\2\2\2\u00ca\u05a4\3\2\2")
        buf.write(u"\2\u00cc\u05af\3\2\2\2\u00ce\u05b2\3\2\2\2\u00d0\u05b6")
        buf.write(u"\3\2\2\2\u00d2\u05c8\3\2\2\2\u00d4\u05d7\3\2\2\2\u00d6")
        buf.write(u"\u05d9\3\2\2\2\u00d8\u05ef\3\2\2\2\u00da\u05f1\3\2\2")
        buf.write(u"\2\u00dc\u05f8\3\2\2\2\u00de\u05ff\3\2\2\2\u00e0\u060b")
        buf.write(u"\3\2\2\2\u00e2\u0617\3\2\2\2\u00e4\u0623\3\2\2\2\u00e6")
        buf.write(u"\u063d\3\2\2\2\u00e8\u064c\3\2\2\2\u00ea\u064e\3\2\2")
        buf.write(u"\2\u00ec\u065d\3\2\2\2\u00ee\u065f\3\2\2\2\u00f0\u0661")
        buf.write(u"\3\2\2\2\u00f2\u0667\3\2\2\2\u00f4\u066e\3\2\2\2\u00f6")
        buf.write(u"\u0670\3\2\2\2\u00f8\u0676\3\2\2\2\u00fa\u067c\3\2\2")
        buf.write(u"\2\u00fc\u0687\3\2\2\2\u00fe\u0692\3\2\2\2\u0100\u069f")
        buf.write(u"\3\2\2\2\u0102\u06a1\3\2\2\2\u0104\u06a5\3\2\2\2\u0106")
        buf.write(u"\u06b3\3\2\2\2\u0108\u06bb\3\2\2\2\u010a\u06bd\3\2\2")
        buf.write(u"\2\u010c\u06c0\3\2\2\2\u010e\u06c3\3\2\2\2\u0110\u06c6")
        buf.write(u"\3\2\2\2\u0112\u06c8\3\2\2\2\u0114\u06ca\3\2\2\2\u0116")
        buf.write(u"\u06cc\3\2\2\2\u0118\u06ce\3\2\2\2\u011a\u06d0\3\2\2")
        buf.write(u"\2\u011c\u06d2\3\2\2\2\u011e\u06db\3\2\2\2\u0120\u06dd")
        buf.write(u"\3\2\2\2\u0122\u06ed\3\2\2\2\u0124\u06ef\3\2\2\2\u0126")
        buf.write(u"\u06f6\3\2\2\2\u0128\u06f8\3\2\2\2\u012a\u06ff\3\2\2")
        buf.write(u"\2\u012c\u070a\3\2\2\2\u012e\u070e\3\2\2\2\u0130\u0712")
        buf.write(u"\3\2\2\2\u0132\u0719\3\2\2\2\u0134\u071b\3\2\2\2\u0136")
        buf.write(u"\u0720\3\2\2\2\u0138\u0722\3\2\2\2\u013a\u0730\3\2\2")
        buf.write(u"\2\u013c\u0738\3\2\2\2\u013e\u073a\3\2\2\2\u0140\u0747")
        buf.write(u"\3\2\2\2\u0142\u0749\3\2\2\2\u0144\u0754\3\2\2\2\u0146")
        buf.write(u"\u0764\3\2\2\2\u0148\u076b\3\2\2\2\u014a\u077a\3\2\2")
        buf.write(u"\2\u014c\u077c\3\2\2\2\u014e\u0785\3\2\2\2\u0150\u0787")
        buf.write(u"\3\2\2\2\u0152\u0795\3\2\2\2\u0154\u0797\3\2\2\2\u0156")
        buf.write(u"\u079c\3\2\2\2\u0158\u079e\3\2\2\2\u015a\u07a5\3\2\2")
        buf.write(u"\2\u015c\u07b0\3\2\2\2\u015e\u07b4\3\2\2\2\u0160\u07b8")
        buf.write(u"\3\2\2\2\u0162\u07c3\3\2\2\2\u0164\u07d2\3\2\2\2\u0166")
        buf.write(u"\u07d4\3\2\2\2\u0168\u07dd\3\2\2\2\u016a\u07df\3\2\2")
        buf.write(u"\2\u016c\u07ed\3\2\2\2\u016e\u07ef\3\2\2\2\u0170\u07f4")
        buf.write(u"\3\2\2\2\u0172\u07f6\3\2\2\2\u0174\u07fd\3\2\2\2\u0176")
        buf.write(u"\u0808\3\2\2\2\u0178\u080c\3\2\2\2\u017a\u0813\3\2\2")
        buf.write(u"\2\u017c\u0822\3\2\2\2\u017e\u0824\3\2\2\2\u0180\u0181")
        buf.write(u"\7S\2\2\u0181\u0182\7G\2\2\u0182\u0187\5\u00acW\2\u0183")
        buf.write(u"\u0184\7\21\2\2\u0184\u0185\5\"\22\2\u0185\u0186\7\22")
        buf.write(u"\2\2\u0186\u0188\3\2\2\2\u0187\u0183\3\2\2\2\u0187\u0188")
        buf.write(u"\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u018a\7W\2\2\u018a")
        buf.write(u"\u018c\5\u00acW\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2")
        buf.write(u"\2\2\u018c\u018d\3\2\2\2\u018d\u018e\7\25\2\2\u018e\u018f")
        buf.write(u"\5\u0088E\2\u018f\u0190\7\26\2\2\u0190\3\3\2\2\2\u0191")
        buf.write(u"\u0192\7S\2\2\u0192\u0193\5\u00acW\2\u0193\u0194\7\21")
        buf.write(u"\2\2\u0194\u0195\5\u009aN\2\u0195\u0196\7\22\2\2\u0196")
        buf.write(u"\u0197\7\25\2\2\u0197\u0198\5\u0086D\2\u0198\u0199\7")
        buf.write(u"\26\2\2\u0199\5\3\2\2\2\u019a\u019b\5\u00aeX\2\u019b")
        buf.write(u"\u019c\7\21\2\2\u019c\u019d\5p9\2\u019d\u019e\7\22\2")
        buf.write(u"\2\u019e\u019f\7\r\2\2\u019f\7\3\2\2\2\u01a0\u01a1\5")
        buf.write(u"\u00aeX\2\u01a1\u01a2\7(\2\2\u01a2\u01a3\5X-\2\u01a3")
        buf.write(u"\u01a4\7\r\2\2\u01a4\t\3\2\2\2\u01a5\u01a7\7}\2\2\u01a6")
        buf.write(u"\u01a5\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3\2\2")
        buf.write(u"\2\u01a8\u01a9\7B\2\2\u01a9\u01aa\5\u00aaV\2\u01aa\u01ab")
        buf.write(u"\7\f\2\2\u01ab\u01ad\5\u0096L\2\u01ac\u01ae\5\u008cG")
        buf.write(u"\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af")
        buf.write(u"\3\2\2\2\u01af\u01b0\7\r\2\2\u01b0\13\3\2\2\2\u01b1\u01b3")
        buf.write(u"\7}\2\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write(u"\u01b4\3\2\2\2\u01b4\u01b5\7G\2\2\u01b5\u01ba\5\u00ac")
        buf.write(u"W\2\u01b6\u01b7\7\21\2\2\u01b7\u01b8\5\"\22\2\u01b8\u01b9")
        buf.write(u"\7\22\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b6\3\2\2\2\u01ba")
        buf.write(u"\u01bb\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01bd\7W\2\2")
        buf.write(u"\u01bd\u01bf\5\20\t\2\u01be\u01bc\3\2\2\2\u01be\u01bf")
        buf.write(u"\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\5\22\n\2\u01c1")
        buf.write(u"\r\3\2\2\2\u01c2\u01c3\7{\2\2\u01c3\u01c8\5\u00acW\2")
        buf.write(u"\u01c4\u01c5\7\21\2\2\u01c5\u01c6\5\"\22\2\u01c6\u01c7")
        buf.write(u"\7\22\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01c4\3\2\2\2\u01c8")
        buf.write(u"\u01c9\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\5\22\n")
        buf.write(u"\2\u01cb\17\3\2\2\2\u01cc\u01cd\b\t\1\2\u01cd\u01ce\5")
        buf.write(u"\u00acW\2\u01ce\u01d4\3\2\2\2\u01cf\u01d0\f\3\2\2\u01d0")
        buf.write(u"\u01d1\7\16\2\2\u01d1\u01d3\5\u00acW\2\u01d2\u01cf\3")
        buf.write(u"\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4")
        buf.write(u"\u01d5\3\2\2\2\u01d5\21\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7")
        buf.write(u"\u01de\7\r\2\2\u01d8\u01da\7\25\2\2\u01d9\u01db\5\u00be")
        buf.write(u"`\2\u01da\u01d9\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dc")
        buf.write(u"\3\2\2\2\u01dc\u01de\7\26\2\2\u01dd\u01d7\3\2\2\2\u01dd")
        buf.write(u"\u01d8\3\2\2\2\u01de\23\3\2\2\2\u01df\u01e1\5\u0096L")
        buf.write(u"\2\u01e0\u01df\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2")
        buf.write(u"\3\2\2\2\u01e2\u01e3\7n\2\2\u01e3\u01e4\5\u0108\u0085")
        buf.write(u"\2\u01e4\u01e5\7\21\2\2\u01e5\u01e6\5\u00b4[\2\u01e6")
        buf.write(u"\u01e7\7\22\2\2\u01e7\u01e9\7\25\2\2\u01e8\u01ea\5\u00de")
        buf.write(u"p\2\u01e9\u01e8\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb")
        buf.write(u"\3\2\2\2\u01eb\u01ec\7\26\2\2\u01ec\25\3\2\2\2\u01ed")
        buf.write(u"\u01ee\7z\2\2\u01ee\u01ef\5\u00aaV\2\u01ef\u01f1\7\25")
        buf.write(u"\2\2\u01f0\u01f2\5\u00dep\2\u01f1\u01f0\3\2\2\2\u01f1")
        buf.write(u"\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\7\26\2")
        buf.write(u"\2\u01f4\27\3\2\2\2\u01f5\u01f6\7\\\2\2\u01f6\u01f7\5")
        buf.write(u"\u00aaV\2\u01f7\u01f9\7\25\2\2\u01f8\u01fa\5\u00dep\2")
        buf.write(u"\u01f9\u01f8\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb")
        buf.write(u"\3\2\2\2\u01fb\u01fc\7\26\2\2\u01fc\31\3\2\2\2\u01fd")
        buf.write(u"\u01fe\7f\2\2\u01fe\u01ff\7u\2\2\u01ff\u0204\5\u00ac")
        buf.write(u"W\2\u0200\u0201\7\21\2\2\u0201\u0202\5\"\22\2\u0202\u0203")
        buf.write(u"\7\22\2\2\u0203\u0205\3\2\2\2\u0204\u0200\3\2\2\2\u0204")
        buf.write(u"\u0205\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0207\7\25\2")
        buf.write(u"\2\u0207\u0209\5\36\20\2\u0208\u020a\5\u00c2b\2\u0209")
        buf.write(u"\u0208\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020b\3\2\2")
        buf.write(u"\2\u020b\u020c\7\26\2\2\u020c\33\3\2\2\2\u020d\u020f")
        buf.write(u"\7}\2\2\u020e\u020d\3\2\2\2\u020e\u020f\3\2\2\2\u020f")
        buf.write(u"\u0210\3\2\2\2\u0210\u0211\7f\2\2\u0211\u0212\7G\2\2")
        buf.write(u"\u0212\u0217\5\u00acW\2\u0213\u0214\7\21\2\2\u0214\u0215")
        buf.write(u"\5\"\22\2\u0215\u0216\7\22\2\2\u0216\u0218\3\2\2\2\u0217")
        buf.write(u"\u0213\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0219\3\2\2")
        buf.write(u"\2\u0219\u021a\7\25\2\2\u021a\u021c\5\36\20\2\u021b\u021d")
        buf.write(u"\5\u00c2b\2\u021c\u021b\3\2\2\2\u021c\u021d\3\2\2\2\u021d")
        buf.write(u"\u021e\3\2\2\2\u021e\u021f\7\26\2\2\u021f\35\3\2\2\2")
        buf.write(u"\u0220\u0221\7G\2\2\u0221\u0222\7D\2\2\u0222\u0223\7")
        buf.write(u"\25\2\2\u0223\u0224\5 \21\2\u0224\u0225\7\26\2\2\u0225")
        buf.write(u"\37\3\2\2\2\u0226\u0227\b\21\1\2\u0227\u0228\5\u00c6")
        buf.write(u"d\2\u0228\u0229\7\r\2\2\u0229\u0230\3\2\2\2\u022a\u022b")
        buf.write(u"\f\3\2\2\u022b\u022c\5\u00c6d\2\u022c\u022d\7\r\2\2\u022d")
        buf.write(u"\u022f\3\2\2\2\u022e\u022a\3\2\2\2\u022f\u0232\3\2\2")
        buf.write(u"\2\u0230\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231!\3\2")
        buf.write(u"\2\2\u0232\u0230\3\2\2\2\u0233\u0234\b\22\1\2\u0234\u0235")
        buf.write(u"\5\u00aaV\2\u0235\u023b\3\2\2\2\u0236\u0237\f\3\2\2\u0237")
        buf.write(u"\u0238\7\16\2\2\u0238\u023a\5\u00aaV\2\u0239\u0236\3")
        buf.write(u"\2\2\2\u023a\u023d\3\2\2\2\u023b\u0239\3\2\2\2\u023b")
        buf.write(u"\u023c\3\2\2\2\u023c#\3\2\2\2\u023d\u023b\3\2\2\2\u023e")
        buf.write(u"\u0240\7;\2\2\u023f\u0241\5\u0096L\2\u0240\u023f\3\2")
        buf.write(u"\2\2\u0240\u0241\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243")
        buf.write(u"\7b\2\2\u0243\u0244\5\u00a6T\2\u0244\u0246\7\21\2\2\u0245")
        buf.write(u"\u0247\5\u00b0Y\2\u0246\u0245\3\2\2\2\u0246\u0247\3\2")
        buf.write(u"\2\2\u0247\u0248\3\2\2\2\u0248\u0249\7\22\2\2\u0249\u024a")
        buf.write(u"\7\r\2\2\u024a%\3\2\2\2\u024b\u024d\5\u0096L\2\u024c")
        buf.write(u"\u024b\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024e\3\2\2")
        buf.write(u"\2\u024e\u024f\7b\2\2\u024f\u0250\5\u00a6T\2\u0250\u0252")
        buf.write(u"\7\21\2\2\u0251\u0253\5\u00b0Y\2\u0252\u0251\3\2\2\2")
        buf.write(u"\u0252\u0253\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0255")
        buf.write(u"\7\22\2\2\u0255\u0257\7\25\2\2\u0256\u0258\5\u00dep\2")
        buf.write(u"\u0257\u0256\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0259")
        buf.write(u"\3\2\2\2\u0259\u025a\7\26\2\2\u025a\'\3\2\2\2\u025b\u025d")
        buf.write(u"\5\u00ba^\2\u025c\u025b\3\2\2\2\u025c\u025d\3\2\2\2\u025d")
        buf.write(u"\u025e\3\2\2\2\u025e\u025f\7f\2\2\u025f\u0260\7b\2\2")
        buf.write(u"\u0260\u0261\5\u00a6T\2\u0261\u0263\7\21\2\2\u0262\u0264")
        buf.write(u"\5\u00b0Y\2\u0263\u0262\3\2\2\2\u0263\u0264\3\2\2\2\u0264")
        buf.write(u"\u0265\3\2\2\2\u0265\u0266\7\22\2\2\u0266\u0267\7\25")
        buf.write(u"\2\2\u0267\u0268\5\u00d6l\2\u0268\u0269\7\26\2\2\u0269")
        buf.write(u")\3\2\2\2\u026a\u026b\7\u0080\2\2\u026b\u026c\7b\2\2")
        buf.write(u"\u026c\u026d\7\u0093\2\2\u026d\u026e\7\21\2\2\u026e\u026f")
        buf.write(u"\7\22\2\2\u026f\u0270\7\25\2\2\u0270\u0271\5\u00dep\2")
        buf.write(u"\u0271\u0272\7\26\2\2\u0272\u027a\7V\2\2\u0273\u0274")
        buf.write(u"\7\25\2\2\u0274\u0275\5\u00e0q\2\u0275\u0276\7\26\2\2")
        buf.write(u"\u0276\u027b\3\2\2\2\u0277\u0278\5\u00aeX\2\u0278\u0279")
        buf.write(u"\7\r\2\2\u0279\u027b\3\2\2\2\u027a\u0273\3\2\2\2\u027a")
        buf.write(u"\u0277\3\2\2\2\u027b+\3\2\2\2\u027c\u027d\5X-\2\u027d")
        buf.write(u"\u027e\7\r\2\2\u027e-\3\2\2\2\u027f\u0284\5\u00ba^\2")
        buf.write(u"\u0280\u0281\7\21\2\2\u0281\u0282\5\"\22\2\u0282\u0283")
        buf.write(u"\7\22\2\2\u0283\u0285\3\2\2\2\u0284\u0280\3\2\2\2\u0284")
        buf.write(u"\u0285\3\2\2\2\u0285\u0286\3\2\2\2\u0286\u0289\5\u00aa")
        buf.write(u"V\2\u0287\u0288\7(\2\2\u0288\u028a\5\u00f2z\2\u0289\u0287")
        buf.write(u"\3\2\2\2\u0289\u028a\3\2\2\2\u028a/\3\2\2\2\u028b\u0293")
        buf.write(u"\5\62\32\2\u028c\u0290\7\25\2\2\u028d\u028e\5\u00dep")
        buf.write(u"\2\u028e\u028f\7\26\2\2\u028f\u0291\3\2\2\2\u0290\u028d")
        buf.write(u"\3\2\2\2\u0290\u0291\3\2\2\2\u0291\u0293\3\2\2\2\u0292")
        buf.write(u"\u028b\3\2\2\2\u0292\u028c\3\2\2\2\u0293\61\3\2\2\2\u0294")
        buf.write(u"\u0295\5P)\2\u0295\u0296\7\r\2\2\u0296\u02a7\3\2\2\2")
        buf.write(u"\u0297\u02a7\5t;\2\u0298\u02a7\5x=\2\u0299\u02a7\5\64")
        buf.write(u"\33\2\u029a\u02a7\5N(\2\u029b\u02a7\5D#\2\u029c\u02a7")
        buf.write(u"\5:\36\2\u029d\u02a7\5> \2\u029e\u02a7\5B\"\2\u029f\u02a7")
        buf.write(u"\5@!\2\u02a0\u02a7\5J&\2\u02a1\u02a7\5H%\2\u02a2\u02a7")
        buf.write(u"\5f\64\2\u02a3\u02a7\5\66\34\2\u02a4\u02a7\58\35\2\u02a5")
        buf.write(u"\u02a7\5&\24\2\u02a6\u0294\3\2\2\2\u02a6\u0297\3\2\2")
        buf.write(u"\2\u02a6\u0298\3\2\2\2\u02a6\u0299\3\2\2\2\u02a6\u029a")
        buf.write(u"\3\2\2\2\u02a6\u029b\3\2\2\2\u02a6\u029c\3\2\2\2\u02a6")
        buf.write(u"\u029d\3\2\2\2\u02a6\u029e\3\2\2\2\u02a6\u029f\3\2\2")
        buf.write(u"\2\u02a6\u02a0\3\2\2\2\u02a6\u02a1\3\2\2\2\u02a6\u02a2")
        buf.write(u"\3\2\2\2\u02a6\u02a3\3\2\2\2\u02a6\u02a4\3\2\2\2\u02a6")
        buf.write(u"\u02a5\3\2\2\2\u02a7\63\3\2\2\2\u02a8\u02a9\7~\2\2\u02a9")
        buf.write(u"\u02aa\7\21\2\2\u02aa\u02ab\5\u0092J\2\u02ab\u02ac\7")
        buf.write(u"\22\2\2\u02ac\u02ad\7\r\2\2\u02ad\65\3\2\2\2\u02ae\u02af")
        buf.write(u"\7\u0085\2\2\u02af\u02b0\7\21\2\2\u02b0\u02b1\5\u0102")
        buf.write(u"\u0082\2\u02b1\u02b2\7\22\2\2\u02b2\u02b3\5\60\31\2\u02b3")
        buf.write(u"\67\3\2\2\2\u02b4\u02b5\7\u0085\2\2\u02b5\u02b6\7\21")
        buf.write(u"\2\2\u02b6\u02b7\5\u00acW\2\u02b7\u02b8\7\22\2\2\u02b8")
        buf.write(u"\u02b9\5\60\31\2\u02b99\3\2\2\2\u02ba\u02bb\7\177\2\2")
        buf.write(u"\u02bb\u02bc\7\21\2\2\u02bc\u02bd\5X-\2\u02bd\u02be\7")
        buf.write(u"\22\2\2\u02be\u02bf\7\25\2\2\u02bf\u02c5\5\u00e2r\2\u02c0")
        buf.write(u"\u02c1\7L\2\2\u02c1\u02c3\7\f\2\2\u02c2\u02c4\5\u00de")
        buf.write(u"p\2\u02c3\u02c2\3\2\2\2\u02c3\u02c4\3\2\2\2\u02c4\u02c6")
        buf.write(u"\3\2\2\2\u02c5\u02c0\3\2\2\2\u02c5\u02c6\3\2\2\2\u02c6")
        buf.write(u"\u02c7\3\2\2\2\u02c7\u02c8\7\26\2\2\u02c8;\3\2\2\2\u02c9")
        buf.write(u"\u02ca\7E\2\2\u02ca\u02cb\5\u00e8u\2\u02cb\u02cd\7\f")
        buf.write(u"\2\2\u02cc\u02ce\5\u00dep\2\u02cd\u02cc\3\2\2\2\u02cd")
        buf.write(u"\u02ce\3\2\2\2\u02ce\u02d7\3\2\2\2\u02cf\u02d0\7E\2\2")
        buf.write(u"\u02d0\u02d1\7^\2\2\u02d1\u02d2\5\u00e6t\2\u02d2\u02d4")
        buf.write(u"\7\f\2\2\u02d3\u02d5\5\u00dep\2\u02d4\u02d3\3\2\2\2\u02d4")
        buf.write(u"\u02d5\3\2\2\2\u02d5\u02d7\3\2\2\2\u02d6\u02c9\3\2\2")
        buf.write(u"\2\u02d6\u02cf\3\2\2\2\u02d7=\3\2\2\2\u02d8\u02d9\7Z")
        buf.write(u"\2\2\u02d9\u02da\7P\2\2\u02da\u02db\7\21\2\2\u02db\u02de")
        buf.write(u"\5\u00aaV\2\u02dc\u02dd\7\16\2\2\u02dd\u02df\5\u00aa")
        buf.write(u"V\2\u02de\u02dc\3\2\2\2\u02de\u02df\3\2\2\2\u02df\u02e0")
        buf.write(u"\3\2\2\2\u02e0\u02e1\7^\2\2\u02e1\u02e2\5X-\2\u02e2\u02e3")
        buf.write(u"\7\22\2\2\u02e3\u02e4\5\60\31\2\u02e4?\3\2\2\2\u02e5")
        buf.write(u"\u02e6\7N\2\2\u02e6\u02e8\7\25\2\2\u02e7\u02e9\5\u00de")
        buf.write(u"p\2\u02e8\u02e7\3\2\2\2\u02e8\u02e9\3\2\2\2\u02e9\u02ea")
        buf.write(u"\3\2\2\2\u02ea\u02eb\7\26\2\2\u02eb\u02ec\7\u0088\2\2")
        buf.write(u"\u02ec\u02ed\7\21\2\2\u02ed\u02ee\5X-\2\u02ee\u02ef\7")
        buf.write(u"\22\2\2\u02ef\u02f0\7\r\2\2\u02f0A\3\2\2\2\u02f1\u02f2")
        buf.write(u"\7\u0088\2\2\u02f2\u02f3\7\21\2\2\u02f3\u02f4\5X-\2\u02f4")
        buf.write(u"\u02f5\7\22\2\2\u02f5\u02f6\5\60\31\2\u02f6C\3\2\2\2")
        buf.write(u"\u02f7\u02f8\7]\2\2\u02f8\u02f9\7\21\2\2\u02f9\u02fa")
        buf.write(u"\5X-\2\u02fa\u02fb\7\22\2\2\u02fb\u02fd\5\60\31\2\u02fc")
        buf.write(u"\u02fe\5F$\2\u02fd\u02fc\3\2\2\2\u02fd\u02fe\3\2\2\2")
        buf.write(u"\u02fe\u0301\3\2\2\2\u02ff\u0300\7Q\2\2\u0300\u0302\5")
        buf.write(u"\60\31\2\u0301\u02ff\3\2\2\2\u0301\u0302\3\2\2\2\u0302")
        buf.write(u"E\3\2\2\2\u0303\u0304\b$\1\2\u0304\u0305\7Q\2\2\u0305")
        buf.write(u"\u0306\7]\2\2\u0306\u0307\7\21\2\2\u0307\u0308\5X-\2")
        buf.write(u"\u0308\u0309\7\22\2\2\u0309\u030a\5\60\31\2\u030a\u0315")
        buf.write(u"\3\2\2\2\u030b\u030c\f\3\2\2\u030c\u030d\7Q\2\2\u030d")
        buf.write(u"\u030e\7]\2\2\u030e\u030f\7\21\2\2\u030f\u0310\5X-\2")
        buf.write(u"\u0310\u0311\7\22\2\2\u0311\u0312\5\60\31\2\u0312\u0314")
        buf.write(u"\3\2\2\2\u0313\u030b\3\2\2\2\u0314\u0317\3\2\2\2\u0315")
        buf.write(u"\u0313\3\2\2\2\u0315\u0316\3\2\2\2\u0316G\3\2\2\2\u0317")
        buf.write(u"\u0315\3\2\2\2\u0318\u0319\7\u0082\2\2\u0319\u031a\5")
        buf.write(u"X-\2\u031a\u031b\7\r\2\2\u031bI\3\2\2\2\u031c\u031d\7")
        buf.write(u"\u0084\2\2\u031d\u031e\7\21\2\2\u031e\u031f\5\u00aaV")
        buf.write(u"\2\u031f\u0320\7\22\2\2\u0320\u0322\7\25\2\2\u0321\u0323")
        buf.write(u"\5\u00dep\2\u0322\u0321\3\2\2\2\u0322\u0323\3\2\2\2\u0323")
        buf.write(u"\u0324\3\2\2\2\u0324\u0326\7\26\2\2\u0325\u0327\5\u00e4")
        buf.write(u"s\2\u0326\u0325\3\2\2\2\u0326\u0327\3\2\2\2\u0327\u0331")
        buf.write(u"\3\2\2\2\u0328\u0329\7F\2\2\u0329\u032a\7\21\2\2\u032a")
        buf.write(u"\u032b\7?\2\2\u032b\u032c\7\22\2\2\u032c\u032e\7\25\2")
        buf.write(u"\2\u032d\u032f\5\u00dep\2\u032e\u032d\3\2\2\2\u032e\u032f")
        buf.write(u"\3\2\2\2\u032f\u0330\3\2\2\2\u0330\u0332\7\26\2\2\u0331")
        buf.write(u"\u0328\3\2\2\2\u0331\u0332\3\2\2\2\u0332\u0339\3\2\2")
        buf.write(u"\2\u0333\u0334\7Y\2\2\u0334\u0336\7\25\2\2\u0335\u0337")
        buf.write(u"\5\u00dep\2\u0336\u0335\3\2\2\2\u0336\u0337\3\2\2\2\u0337")
        buf.write(u"\u0338\3\2\2\2\u0338\u033a\7\26\2\2\u0339\u0333\3\2\2")
        buf.write(u"\2\u0339\u033a\3\2\2\2\u033aK\3\2\2\2\u033b\u033c\7F")
        buf.write(u"\2\2\u033c\u033d\7\21\2\2\u033d\u033e\5\u00aeX\2\u033e")
        buf.write(u"\u033f\7\22\2\2\u033f\u0341\7\25\2\2\u0340\u0342\5\u00de")
        buf.write(u"p\2\u0341\u0340\3\2\2\2\u0341\u0342\3\2\2\2\u0342\u0343")
        buf.write(u"\3\2\2\2\u0343\u0344\7\26\2\2\u0344\u0351\3\2\2\2\u0345")
        buf.write(u"\u0346\7F\2\2\u0346\u0347\7^\2\2\u0347\u0348\7\21\2\2")
        buf.write(u"\u0348\u0349\5\u008aF\2\u0349\u034a\7\22\2\2\u034a\u034c")
        buf.write(u"\7\25\2\2\u034b\u034d\5\u00dep\2\u034c\u034b\3\2\2\2")
        buf.write(u"\u034c\u034d\3\2\2\2\u034d\u034e\3\2\2\2\u034e\u034f")
        buf.write(u"\7\26\2\2\u034f\u0351\3\2\2\2\u0350\u033b\3\2\2\2\u0350")
        buf.write(u"\u0345\3\2\2\2\u0351M\3\2\2\2\u0352\u0354\7v\2\2\u0353")
        buf.write(u"\u0355\5X-\2\u0354\u0353\3\2\2\2\u0354\u0355\3\2\2\2")
        buf.write(u"\u0355\u0356\3\2\2\2\u0356\u0357\7\r\2\2\u0357O\3\2\2")
        buf.write(u"\2\u0358\u0359\5R*\2\u0359\u035b\7\21\2\2\u035a\u035c")
        buf.write(u"\5p9\2\u035b\u035a\3\2\2\2\u035b\u035c\3\2\2\2\u035c")
        buf.write(u"\u035d\3\2\2\2\u035d\u035e\7\22\2\2\u035eQ\3\2\2\2\u035f")
        buf.write(u"\u0365\5\u00a6T\2\u0360\u0361\5T+\2\u0361\u0362\7\20")
        buf.write(u"\2\2\u0362\u0363\5\u00a6T\2\u0363\u0365\3\2\2\2\u0364")
        buf.write(u"\u035f\3\2\2\2\u0364\u0360\3\2\2\2\u0365S\3\2\2\2\u0366")
        buf.write(u"\u0367\b+\1\2\u0367\u0368\5\u00a8U\2\u0368\u036d\3\2")
        buf.write(u"\2\2\u0369\u036a\f\3\2\2\u036a\u036c\5V,\2\u036b\u0369")
        buf.write(u"\3\2\2\2\u036c\u036f\3\2\2\2\u036d\u036b\3\2\2\2\u036d")
        buf.write(u"\u036e\3\2\2\2\u036eU\3\2\2\2\u036f\u036d\3\2\2\2\u0370")
        buf.write(u"\u0371\7\20\2\2\u0371\u0377\5\u00aaV\2\u0372\u0373\7")
        buf.write(u"\23\2\2\u0373\u0374\5X-\2\u0374\u0375\7\24\2\2\u0375")
        buf.write(u"\u0377\3\2\2\2\u0376\u0370\3\2\2\2\u0376\u0372\3\2\2")
        buf.write(u"\2\u0377W\3\2\2\2\u0378\u0379\b-\1\2\u0379\u037a\7\36")
        buf.write(u"\2\2\u037a\u0390\5X-#\u037b\u037c\7\30\2\2\u037c\u0390")
        buf.write(u"\5X-\"\u037d\u037e\7\21\2\2\u037e\u037f\5\u00ba^\2\u037f")
        buf.write(u"\u0380\7\22\2\2\u0380\u0381\5X-\16\u0381\u0390\3\2\2")
        buf.write(u"\2\u0382\u0390\5^\60\2\u0383\u0390\5`\61\2\u0384\u0385")
        buf.write(u"\79\2\2\u0385\u0386\7\21\2\2\u0386\u0387\5X-\2\u0387")
        buf.write(u"\u0388\7\22\2\2\u0388\u0390\3\2\2\2\u0389\u038a\7U\2")
        buf.write(u"\2\u038a\u038b\7\21\2\2\u038b\u038c\5\u00aaV\2\u038c")
        buf.write(u"\u038d\7\22\2\2\u038d\u0390\3\2\2\2\u038e\u0390\5\\/")
        buf.write(u"\2\u038f\u0378\3\2\2\2\u038f\u037b\3\2\2\2\u038f\u037d")
        buf.write(u"\3\2\2\2\u038f\u0382\3\2\2\2\u038f\u0383\3\2\2\2\u038f")
        buf.write(u"\u0384\3\2\2\2\u038f\u0389\3\2\2\2\u038f\u038e\3\2\2")
        buf.write(u"\2\u0390\u03f5\3\2\2\2\u0391\u0392\f!\2\2\u0392\u0393")
        buf.write(u"\5\u0112\u008a\2\u0393\u0394\5X-\"\u0394\u03f4\3\2\2")
        buf.write(u"\2\u0395\u0396\f \2\2\u0396\u0397\5\u0114\u008b\2\u0397")
        buf.write(u"\u0398\5X-!\u0398\u03f4\3\2\2\2\u0399\u039a\f\37\2\2")
        buf.write(u"\u039a\u039b\5\u0118\u008d\2\u039b\u039c\5X- \u039c\u03f4")
        buf.write(u"\3\2\2\2\u039d\u039e\f\36\2\2\u039e\u039f\5\u0116\u008c")
        buf.write(u"\2\u039f\u03a0\5X-\37\u03a0\u03f4\3\2\2\2\u03a1\u03a2")
        buf.write(u"\f\35\2\2\u03a2\u03a3\t\2\2\2\u03a3\u03f4\5X-\36\u03a4")
        buf.write(u"\u03a5\f\34\2\2\u03a5\u03a6\7%\2\2\u03a6\u03f4\5X-\35")
        buf.write(u"\u03a7\u03a8\f\33\2\2\u03a8\u03a9\7&\2\2\u03a9\u03f4")
        buf.write(u"\5X-\34\u03aa\u03ab\f\32\2\2\u03ab\u03ac\7#\2\2\u03ac")
        buf.write(u"\u03f4\5X-\33\u03ad\u03ae\f\31\2\2\u03ae\u03af\7$\2\2")
        buf.write(u"\u03af\u03f4\5X-\32\u03b0\u03b1\f\26\2\2\u03b1\u03b2")
        buf.write(u"\7`\2\2\u03b2\u03b3\7h\2\2\u03b3\u03f4\5X-\27\u03b4\u03b5")
        buf.write(u"\f\25\2\2\u03b5\u03b6\7`\2\2\u03b6\u03f4\5X-\26\u03b7")
        buf.write(u"\u03b8\f\24\2\2\u03b8\u03b9\7*\2\2\u03b9\u03f4\5X-\25")
        buf.write(u"\u03ba\u03bb\f\23\2\2\u03bb\u03bc\7)\2\2\u03bc\u03f4")
        buf.write(u"\5X-\24\u03bd\u03be\f\22\2\2\u03be\u03bf\7+\2\2\u03bf")
        buf.write(u"\u03f4\5X-\23\u03c0\u03c1\f\21\2\2\u03c1\u03c2\7\34\2")
        buf.write(u"\2\u03c2\u03f4\5X-\22\u03c3\u03c4\f\20\2\2\u03c4\u03c5")
        buf.write(u"\7\32\2\2\u03c5\u03f4\5X-\21\u03c6\u03c7\f\17\2\2\u03c7")
        buf.write(u"\u03c8\7\27\2\2\u03c8\u03c9\5X-\2\u03c9\u03ca\7\f\2\2")
        buf.write(u"\u03ca\u03cb\5X-\20\u03cb\u03f4\3\2\2\2\u03cc\u03cd\f")
        buf.write(u"\r\2\2\u03cd\u03ce\7^\2\2\u03ce\u03f4\5X-\16\u03cf\u03d0")
        buf.write(u"\f\f\2\2\u03d0\u03d1\7J\2\2\u03d1\u03f4\5X-\r\u03d2\u03d3")
        buf.write(u"\f\13\2\2\u03d3\u03d4\7J\2\2\u03d4\u03d5\7<\2\2\u03d5")
        buf.write(u"\u03f4\5X-\f\u03d6\u03d7\f\n\2\2\u03d7\u03d8\7J\2\2\u03d8")
        buf.write(u"\u03d9\7?\2\2\u03d9\u03f4\5X-\13\u03da\u03db\f\t\2\2")
        buf.write(u"\u03db\u03dc\7h\2\2\u03dc\u03dd\7^\2\2\u03dd\u03f4\5")
        buf.write(u"X-\n\u03de\u03df\f\b\2\2\u03df\u03e0\7h\2\2\u03e0\u03e1")
        buf.write(u"\7J\2\2\u03e1\u03f4\5X-\t\u03e2\u03e3\f\7\2\2\u03e3\u03e4")
        buf.write(u"\7h\2\2\u03e4\u03e5\7J\2\2\u03e5\u03e6\7<\2\2\u03e6\u03f4")
        buf.write(u"\5X-\b\u03e7\u03e8\f\6\2\2\u03e8\u03e9\7h\2\2\u03e9\u03ea")
        buf.write(u"\7J\2\2\u03ea\u03eb\7?\2\2\u03eb\u03f4\5X-\7\u03ec\u03ed")
        buf.write(u"\f\30\2\2\u03ed\u03ee\7`\2\2\u03ee\u03ef\7h\2\2\u03ef")
        buf.write(u"\u03f4\5Z.\2\u03f0\u03f1\f\27\2\2\u03f1\u03f2\7`\2\2")
        buf.write(u"\u03f2\u03f4\5Z.\2\u03f3\u0391\3\2\2\2\u03f3\u0395\3")
        buf.write(u"\2\2\2\u03f3\u0399\3\2\2\2\u03f3\u039d\3\2\2\2\u03f3")
        buf.write(u"\u03a1\3\2\2\2\u03f3\u03a4\3\2\2\2\u03f3\u03a7\3\2\2")
        buf.write(u"\2\u03f3\u03aa\3\2\2\2\u03f3\u03ad\3\2\2\2\u03f3\u03b0")
        buf.write(u"\3\2\2\2\u03f3\u03b4\3\2\2\2\u03f3\u03b7\3\2\2\2\u03f3")
        buf.write(u"\u03ba\3\2\2\2\u03f3\u03bd\3\2\2\2\u03f3\u03c0\3\2\2")
        buf.write(u"\2\u03f3\u03c3\3\2\2\2\u03f3\u03c6\3\2\2\2\u03f3\u03cc")
        buf.write(u"\3\2\2\2\u03f3\u03cf\3\2\2\2\u03f3\u03d2\3\2\2\2\u03f3")
        buf.write(u"\u03d6\3\2\2\2\u03f3\u03da\3\2\2\2\u03f3\u03de\3\2\2")
        buf.write(u"\2\u03f3\u03e2\3\2\2\2\u03f3\u03e7\3\2\2\2\u03f3\u03ec")
        buf.write(u"\3\2\2\2\u03f3\u03f0\3\2\2\2\u03f4\u03f7\3\2\2\2\u03f5")
        buf.write(u"\u03f3\3\2\2\2\u03f5\u03f6\3\2\2\2\u03f6Y\3\2\2\2\u03f7")
        buf.write(u"\u03f5\3\2\2\2\u03f8\u03f9\6.\"\3\u03f9\u03fa\7\u0090")
        buf.write(u"\2\2\u03fa\u03fb\5\u00ba^\2\u03fb[\3\2\2\2\u03fc\u03fd")
        buf.write(u"\5\u00acW\2\u03fd]\3\2\2\2\u03fe\u03ff\b\60\1\2\u03ff")
        buf.write(u"\u0400\5\u00ecw\2\u0400\u0405\3\2\2\2\u0401\u0402\f\3")
        buf.write(u"\2\2\u0402\u0404\5l\67\2\u0403\u0401\3\2\2\2\u0404\u0407")
        buf.write(u"\3\2\2\2\u0405\u0403\3\2\2\2\u0405\u0406\3\2\2\2\u0406")
        buf.write(u"_\3\2\2\2\u0407\u0405\3\2\2\2\u0408\u040f\5b\62\2\u0409")
        buf.write(u"\u040f\5h\65\2\u040a\u040f\5d\63\2\u040b\u040f\5j\66")
        buf.write(u"\2\u040c\u040f\5P)\2\u040d\u040f\5n8\2\u040e\u0408\3")
        buf.write(u"\2\2\2\u040e\u0409\3\2\2\2\u040e\u040a\3\2\2\2\u040e")
        buf.write(u"\u040b\3\2\2\2\u040e\u040c\3\2\2\2\u040e\u040d\3\2\2")
        buf.write(u"\2\u040fa\3\2\2\2\u0410\u0411\5\u00a0Q\2\u0411\u0412")
        buf.write(u"\7\21\2\2\u0412\u0413\7\22\2\2\u0413c\3\2\2\2\u0414\u0415")
        buf.write(u"\7s\2\2\u0415\u0416\7[\2\2\u0416\u0417\5X-\2\u0417e\3")
        buf.write(u"\2\2\2\u0418\u0419\7\u0089\2\2\u0419\u041a\7\21\2\2\u041a")
        buf.write(u"\u041b\5X-\2\u041b\u041c\7\22\2\2\u041c\u041d\7\u0083")
        buf.write(u"\2\2\u041d\u041e\5X-\2\u041e\u041f\7\r\2\2\u041fg\3\2")
        buf.write(u"\2\2\u0420\u0421\7X\2\2\u0421\u0422\7\21\2\2\u0422\u0423")
        buf.write(u"\5\u00aaV\2\u0423\u0424\7\22\2\2\u0424\u0425\7[\2\2\u0425")
        buf.write(u"\u0426\5X-\2\u0426\u0427\7\u0087\2\2\u0427\u0428\5X-")
        buf.write(u"\2\u0428\u0447\3\2\2\2\u0429\u042a\7X\2\2\u042a\u042b")
        buf.write(u"\7l\2\2\u042b\u042c\7\21\2\2\u042c\u042d\5\u009cO\2\u042d")
        buf.write(u"\u042e\7\22\2\2\u042e\u042f\7\u0087\2\2\u042f\u0430\7")
        buf.write(u"\21\2\2\u0430\u0431\5X-\2\u0431\u0432\7\22\2\2\u0432")
        buf.write(u"\u0447\3\2\2\2\u0433\u043a\7X\2\2\u0434\u043b\7<\2\2")
        buf.write(u"\u0435\u0436\7x\2\2\u0436\u0437\5X-\2\u0437\u0438\7\u0083")
        buf.write(u"\2\2\u0438\u0439\5X-\2\u0439\u043b\3\2\2\2\u043a\u0434")
        buf.write(u"\3\2\2\2\u043a\u0435\3\2\2\2\u043b\u043c\3\2\2\2\u043c")
        buf.write(u"\u043d\7\21\2\2\u043d\u043e\5\u009cO\2\u043e\u0444\7")
        buf.write(u"\22\2\2\u043f\u0440\7\u0087\2\2\u0440\u0441\7\21\2\2")
        buf.write(u"\u0441\u0442\5X-\2\u0442\u0443\7\22\2\2\u0443\u0445\3")
        buf.write(u"\2\2\2\u0444\u043f\3\2\2\2\u0444\u0445\3\2\2\2\u0445")
        buf.write(u"\u0447\3\2\2\2\u0446\u0420\3\2\2\2\u0446\u0429\3\2\2")
        buf.write(u"\2\u0446\u0433\3\2\2\2\u0447i\3\2\2\2\u0448\u0449\7|")
        buf.write(u"\2\2\u0449\u044a\7\21\2\2\u044a\u0450\5^\60\2\u044b\u044c")
        buf.write(u"\7\16\2\2\u044c\u044d\5\u010a\u0086\2\u044d\u044e\7(")
        buf.write(u"\2\2\u044e\u044f\5^\60\2\u044f\u0451\3\2\2\2\u0450\u044b")
        buf.write(u"\3\2\2\2\u0450\u0451\3\2\2\2\u0451\u0452\3\2\2\2\u0452")
        buf.write(u"\u0453\7\22\2\2\u0453k\3\2\2\2\u0454\u0455\7\20\2\2\u0455")
        buf.write(u"\u045f\5\u00aaV\2\u0456\u0457\7\23\2\2\u0457\u0458\5")
        buf.write(u"X-\2\u0458\u0459\7\24\2\2\u0459\u045f\3\2\2\2\u045a\u045b")
        buf.write(u"\7\23\2\2\u045b\u045c\5\u0100\u0081\2\u045c\u045d\7\24")
        buf.write(u"\2\2\u045d\u045f\3\2\2\2\u045e\u0454\3\2\2\2\u045e\u0456")
        buf.write(u"\3\2\2\2\u045e\u045a\3\2\2\2\u045fm\3\2\2\2\u0460\u0462")
        buf.write(u"\7e\2\2\u0461\u0460\3\2\2\2\u0461\u0462\3\2\2\2\u0462")
        buf.write(u"\u0463\3\2\2\2\u0463\u0464\5\u009cO\2\u0464\u0466\7\21")
        buf.write(u"\2\2\u0465\u0467\5p9\2\u0466\u0465\3\2\2\2\u0466\u0467")
        buf.write(u"\3\2\2\2\u0467\u0468\3\2\2\2\u0468\u0469\7\22\2\2\u0469")
        buf.write(u"o\3\2\2\2\u046a\u046b\b9\1\2\u046b\u046c\5X-\2\u046c")
        buf.write(u"\u046d\69$\3\u046d\u0470\3\2\2\2\u046e\u0470\5r:\2\u046f")
        buf.write(u"\u046a\3\2\2\2\u046f\u046e\3\2\2\2\u0470\u0476\3\2\2")
        buf.write(u"\2\u0471\u0472\f\3\2\2\u0472\u0473\7\16\2\2\u0473\u0475")
        buf.write(u"\5r:\2\u0474\u0471\3\2\2\2\u0475\u0478\3\2\2\2\u0476")
        buf.write(u"\u0474\3\2\2\2\u0476\u0477\3\2\2\2\u0477q\3\2\2\2\u0478")
        buf.write(u"\u0476\3\2\2\2\u0479\u047a\5\u00aaV\2\u047a\u047b\5\u0110")
        buf.write(u"\u0089\2\u047b\u047c\5X-\2\u047cs\3\2\2\2\u047d\u047e")
        buf.write(u"\5\u0104\u0083\2\u047e\u047f\5\u0110\u0089\2\u047f\u0480")
        buf.write(u"\5X-\2\u0480\u0481\7\r\2\2\u0481u\3\2\2\2\u0482\u0483")
        buf.write(u"\7\20\2\2\u0483\u0489\5\u00aaV\2\u0484\u0485\7\23\2\2")
        buf.write(u"\u0485\u0486\5X-\2\u0486\u0487\7\24\2\2\u0487\u0489\3")
        buf.write(u"\2\2\2\u0488\u0482\3\2\2\2\u0488\u0484\3\2\2\2\u0489")
        buf.write(u"w\3\2\2\2\u048a\u048b\5\u00d2j\2\u048b\u048c\5\u0110")
        buf.write(u"\u0089\2\u048c\u048d\5X-\2\u048d\u048e\7\r\2\2\u048e")
        buf.write(u"y\3\2\2\2\u048f\u0490\7j\2\2\u0490{\3\2\2\2\u0491\u0493")
        buf.write(u"\5~@\2\u0492\u0491\3\2\2\2\u0492\u0493\3\2\2\2\u0493")
        buf.write(u"\u0494\3\2\2\2\u0494\u0495\5\u011a\u008e\2\u0495\u0496")
        buf.write(u"\7\2\2\3\u0496}\3\2\2\2\u0497\u0498\b@\1\2\u0498\u0499")
        buf.write(u"\5\u0080A\2\u0499\u04a0\3\2\2\2\u049a\u049b\f\3\2\2\u049b")
        buf.write(u"\u049c\5\u011c\u008f\2\u049c\u049d\5\u0080A\2\u049d\u049f")
        buf.write(u"\3\2\2\2\u049e\u049a\3\2\2\2\u049f\u04a2\3\2\2\2\u04a0")
        buf.write(u"\u049e\3\2\2\2\u04a0\u04a1\3\2\2\2\u04a1\177\3\2\2\2")
        buf.write(u"\u04a2\u04a0\3\2\2\2\u04a3\u04a9\5\n\6\2\u04a4\u04a9")
        buf.write(u"\5\u00a2R\2\u04a5\u04a9\5\u0082B\2\u04a6\u04a9\5\u0084")
        buf.write(u"C\2\u04a7\u04a9\5\u00d4k\2\u04a8\u04a3\3\2\2\2\u04a8")
        buf.write(u"\u04a4\3\2\2\2\u04a8\u04a5\3\2\2\2\u04a8\u04a6\3\2\2")
        buf.write(u"\2\u04a8\u04a7\3\2\2\2\u04a9\u0081\3\2\2\2\u04aa\u04ab")
        buf.write(u"\5\32\16\2\u04ab\u0083\3\2\2\2\u04ac\u04af\5\2\2\2\u04ad")
        buf.write(u"\u04af\5\4\3\2\u04ae\u04ac\3\2\2\2\u04ae\u04ad\3\2\2")
        buf.write(u"\2\u04af\u0085\3\2\2\2\u04b0\u04b1\bD\1\2\u04b1\u04b2")
        buf.write(u"\5\b\5\2\u04b2\u04b9\3\2\2\2\u04b3\u04b4\f\3\2\2\u04b4")
        buf.write(u"\u04b5\5\u011c\u008f\2\u04b5\u04b6\5\b\5\2\u04b6\u04b8")
        buf.write(u"\3\2\2\2\u04b7\u04b3\3\2\2\2\u04b8\u04bb\3\2\2\2\u04b9")
        buf.write(u"\u04b7\3\2\2\2\u04b9\u04ba\3\2\2\2\u04ba\u0087\3\2\2")
        buf.write(u"\2\u04bb\u04b9\3\2\2\2\u04bc\u04bd\bE\1\2\u04bd\u04be")
        buf.write(u"\5\6\4\2\u04be\u04c5\3\2\2\2\u04bf\u04c0\f\3\2\2\u04c0")
        buf.write(u"\u04c1\5\u011c\u008f\2\u04c1\u04c2\5\6\4\2\u04c2\u04c4")
        buf.write(u"\3\2\2\2\u04c3\u04bf\3\2\2\2\u04c4\u04c7\3\2\2\2\u04c5")
        buf.write(u"\u04c3\3\2\2\2\u04c5\u04c6\3\2\2\2\u04c6\u0089\3\2\2")
        buf.write(u"\2\u04c7\u04c5\3\2\2\2\u04c8\u04c9\bF\1\2\u04c9\u04ca")
        buf.write(u"\5\u00aeX\2\u04ca\u04d0\3\2\2\2\u04cb\u04cc\f\3\2\2\u04cc")
        buf.write(u"\u04cd\7\16\2\2\u04cd\u04cf\5\u00aeX\2\u04ce\u04cb\3")
        buf.write(u"\2\2\2\u04cf\u04d2\3\2\2\2\u04d0\u04ce\3\2\2\2\u04d0")
        buf.write(u"\u04d1\3\2\2\2\u04d1\u008b\3\2\2\2\u04d2\u04d0\3\2\2")
        buf.write(u"\2\u04d3\u04d4\7^\2\2\u04d4\u04de\5\u008eH\2\u04d5\u04d6")
        buf.write(u"\7^\2\2\u04d6\u04de\5\u0090I\2\u04d7\u04d8\7^\2\2\u04d8")
        buf.write(u"\u04de\5\u0094K\2\u04d9\u04da\7a\2\2\u04da\u04de\7\u0093")
        buf.write(u"\2\2\u04db\u04dc\7a\2\2\u04dc\u04de\5X-\2\u04dd\u04d3")
        buf.write(u"\3\2\2\2\u04dd\u04d5\3\2\2\2\u04dd\u04d7\3\2\2\2\u04dd")
        buf.write(u"\u04d9\3\2\2\2\u04dd\u04db\3\2\2\2\u04de\u008d\3\2\2")
        buf.write(u"\2\u04df\u04e1\7\23\2\2\u04e0\u04e2\5\u0092J\2\u04e1")
        buf.write(u"\u04e0\3\2\2\2\u04e1\u04e2\3\2\2\2\u04e2\u04e3\3\2\2")
        buf.write(u"\2\u04e3\u04e4\7\24\2\2\u04e4\u008f\3\2\2\2\u04e5\u04e7")
        buf.write(u"\7%\2\2\u04e6\u04e8\5\u0092J\2\u04e7\u04e6\3\2\2\2\u04e7")
        buf.write(u"\u04e8\3\2\2\2\u04e8\u04e9\3\2\2\2\u04e9\u04ea\7#\2\2")
        buf.write(u"\u04ea\u0091\3\2\2\2\u04eb\u04ec\bJ\1\2\u04ec\u04ed\5")
        buf.write(u"X-\2\u04ed\u04f3\3\2\2\2\u04ee\u04ef\f\3\2\2\u04ef\u04f0")
        buf.write(u"\7\16\2\2\u04f0\u04f2\5X-\2\u04f1\u04ee\3\2\2\2\u04f2")
        buf.write(u"\u04f5\3\2\2\2\u04f3\u04f1\3\2\2\2\u04f3\u04f4\3\2\2")
        buf.write(u"\2\u04f4\u0093\3\2\2\2\u04f5\u04f3\3\2\2\2\u04f6\u04f7")
        buf.write(u"\7\23\2\2\u04f7\u04f8\5X-\2\u04f8\u04f9\7\17\2\2\u04f9")
        buf.write(u"\u04fa\5X-\2\u04fa\u04fb\7\24\2\2\u04fb\u0095\3\2\2\2")
        buf.write(u"\u04fc\u04fd\bL\1\2\u04fd\u04fe\5\u0098M\2\u04fe\u0509")
        buf.write(u"\3\2\2\2\u04ff\u0500\f\5\2\2\u0500\u0508\7\'\2\2\u0501")
        buf.write(u"\u0502\f\4\2\2\u0502\u0503\7\23\2\2\u0503\u0508\7\24")
        buf.write(u"\2\2\u0504\u0505\f\3\2\2\u0505\u0506\7\25\2\2\u0506\u0508")
        buf.write(u"\7\26\2\2\u0507\u04ff\3\2\2\2\u0507\u0501\3\2\2\2\u0507")
        buf.write(u"\u0504\3\2\2\2\u0508\u050b\3\2\2\2\u0509\u0507\3\2\2")
        buf.write(u"\2\u0509\u050a\3\2\2\2\u050a\u0097\3\2\2\2\u050b\u0509")
        buf.write(u"\3\2\2\2\u050c\u050f\5\u009aN\2\u050d\u050f\5\u009cO")
        buf.write(u"\2\u050e\u050c\3\2\2\2\u050e\u050d\3\2\2\2\u050f\u0099")
        buf.write(u"\3\2\2\2\u0510\u051b\7/\2\2\u0511\u051b\7\60\2\2\u0512")
        buf.write(u"\u051b\7\61\2\2\u0513\u051b\7\62\2\2\u0514\u051b\7\63")
        buf.write(u"\2\2\u0515\u051b\7\64\2\2\u0516\u051b\7\66\2\2\u0517")
        buf.write(u"\u051b\7\65\2\2\u0518\u051b\7\67\2\2\u0519\u051b\79\2")
        buf.write(u"\2\u051a\u0510\3\2\2\2\u051a\u0511\3\2\2\2\u051a\u0512")
        buf.write(u"\3\2\2\2\u051a\u0513\3\2\2\2\u051a\u0514\3\2\2\2\u051a")
        buf.write(u"\u0515\3\2\2\2\u051a\u0516\3\2\2\2\u051a\u0517\3\2\2")
        buf.write(u"\2\u051a\u0518\3\2\2\2\u051a\u0519\3\2\2\2\u051b\u009b")
        buf.write(u"\3\2\2\2\u051c\u051d\7\u008f\2\2\u051d\u009d\3\2\2\2")
        buf.write(u"\u051e\u051f\79\2\2\u051f\u009f\3\2\2\2\u0520\u0521\7")
        buf.write(u":\2\2\u0521\u00a1\3\2\2\2\u0522\u0526\5\f\7\2\u0523\u0526")
        buf.write(u"\5\34\17\2\u0524\u0526\5\16\b\2\u0525\u0522\3\2\2\2\u0525")
        buf.write(u"\u0523\3\2\2\2\u0525\u0524\3\2\2\2\u0526\u00a3\3\2\2")
        buf.write(u"\2\u0527\u0528\bS\1\2\u0528\u0529\5\u00acW\2\u0529\u052f")
        buf.write(u"\3\2\2\2\u052a\u052b\f\3\2\2\u052b\u052c\7\16\2\2\u052c")
        buf.write(u"\u052e\5\u00acW\2\u052d\u052a\3\2\2\2\u052e\u0531\3\2")
        buf.write(u"\2\2\u052f\u052d\3\2\2\2\u052f\u0530\3\2\2\2\u0530\u00a5")
        buf.write(u"\3\2\2\2\u0531\u052f\3\2\2\2\u0532\u0535\5\u00aaV\2\u0533")
        buf.write(u"\u0535\5\u00acW\2\u0534\u0532\3\2\2\2\u0534\u0533\3\2")
        buf.write(u"\2\2\u0535\u00a7\3\2\2\2\u0536\u053a\5\u00aaV\2\u0537")
        buf.write(u"\u053a\5\u00acW\2\u0538\u053a\5\u00aeX\2\u0539\u0536")
        buf.write(u"\3\2\2\2\u0539\u0537\3\2\2\2\u0539\u0538\3\2\2\2\u053a")
        buf.write(u"\u00a9\3\2\2\2\u053b\u053c\7\u0090\2\2\u053c\u00ab\3")
        buf.write(u"\2\2\2\u053d\u053e\7\u008f\2\2\u053e\u00ad\3\2\2\2\u053f")
        buf.write(u"\u0540\7\u008e\2\2\u0540\u00af\3\2\2\2\u0541\u0542\b")
        buf.write(u"Y\1\2\u0542\u0543\5\u00b2Z\2\u0543\u0549\3\2\2\2\u0544")
        buf.write(u"\u0545\f\3\2\2\u0545\u0546\7\16\2\2\u0546\u0548\5\u00b2")
        buf.write(u"Z\2\u0547\u0544\3\2\2\2\u0548\u054b\3\2\2\2\u0549\u0547")
        buf.write(u"\3\2\2\2\u0549\u054a\3\2\2\2\u054a\u00b1\3\2\2\2\u054b")
        buf.write(u"\u0549\3\2\2\2\u054c\u0552\5\u00b8]\2\u054d\u054f\7e")
        buf.write(u"\2\2\u054e\u054d\3\2\2\2\u054e\u054f\3\2\2\2\u054f\u0550")
        buf.write(u"\3\2\2\2\u0550\u0552\5\u00b4[\2\u0551\u054c\3\2\2\2\u0551")
        buf.write(u"\u054e\3\2\2\2\u0552\u00b3\3\2\2\2\u0553\u0556\5\u00b6")
        buf.write(u"\\\2\u0554\u0556\5.\30\2\u0555\u0553\3\2\2\2\u0555\u0554")
        buf.write(u"\3\2\2\2\u0556\u00b5\3\2\2\2\u0557\u055a\5\u00aaV\2\u0558")
        buf.write(u"\u0559\7(\2\2\u0559\u055b\5\u00f2z\2\u055a\u0558\3\2")
        buf.write(u"\2\2\u055a\u055b\3\2\2\2\u055b\u00b7\3\2\2\2\u055c\u055d")
        buf.write(u"\5\u009eP\2\u055d\u055e\5\u00aaV\2\u055e\u00b9\3\2\2")
        buf.write(u"\2\u055f\u0562\5\u0096L\2\u0560\u0562\5\u00bc_\2\u0561")
        buf.write(u"\u055f\3\2\2\2\u0561\u0560\3\2\2\2\u0562\u00bb\3\2\2")
        buf.write(u"\2\u0563\u0564\b_\1\2\u0564\u0565\7?\2\2\u0565\u056e")
        buf.write(u"\3\2\2\2\u0566\u0567\f\4\2\2\u0567\u0568\7\23\2\2\u0568")
        buf.write(u"\u056d\7\24\2\2\u0569\u056a\f\3\2\2\u056a\u056b\7\25")
        buf.write(u"\2\2\u056b\u056d\7\26\2\2\u056c\u0566\3\2\2\2\u056c\u0569")
        buf.write(u"\3\2\2\2\u056d\u0570\3\2\2\2\u056e\u056c\3\2\2\2\u056e")
        buf.write(u"\u056f\3\2\2\2\u056f\u00bd\3\2\2\2\u0570\u056e\3\2\2")
        buf.write(u"\2\u0571\u0572\b`\1\2\u0572\u0573\5\u00c0a\2\u0573\u057a")
        buf.write(u"\3\2\2\2\u0574\u0575\f\3\2\2\u0575\u0576\5\u011c\u008f")
        buf.write(u"\2\u0576\u0577\5\u00c0a\2\u0577\u0579\3\2\2\2\u0578\u0574")
        buf.write(u"\3\2\2\2\u0579\u057c\3\2\2\2\u057a\u0578\3\2\2\2\u057a")
        buf.write(u"\u057b\3\2\2\2\u057b\u00bf\3\2\2\2\u057c\u057a\3\2\2")
        buf.write(u"\2\u057d\u0583\5\26\f\2\u057e\u0583\5\30\r\2\u057f\u0583")
        buf.write(u"\5&\24\2\u0580\u0583\5$\23\2\u0581\u0583\5\24\13\2\u0582")
        buf.write(u"\u057d\3\2\2\2\u0582\u057e\3\2\2\2\u0582\u057f\3\2\2")
        buf.write(u"\2\u0582\u0580\3\2\2\2\u0582\u0581\3\2\2\2\u0583\u00c1")
        buf.write(u"\3\2\2\2\u0584\u0585\bb\1\2\u0585\u0586\5\u00c4c\2\u0586")
        buf.write(u"\u058d\3\2\2\2\u0587\u0588\f\3\2\2\u0588\u0589\5\u011c")
        buf.write(u"\u008f\2\u0589\u058a\5\u00c4c\2\u058a\u058c\3\2\2\2\u058b")
        buf.write(u"\u0587\3\2\2\2\u058c\u058f\3\2\2\2\u058d\u058b\3\2\2")
        buf.write(u"\2\u058d\u058e\3\2\2\2\u058e\u00c3\3\2\2\2\u058f\u058d")
        buf.write(u"\3\2\2\2\u0590\u0593\5\u00c0a\2\u0591\u0593\5(\25\2\u0592")
        buf.write(u"\u0590\3\2\2\2\u0592\u0591\3\2\2\2\u0593\u00c5\3\2\2")
        buf.write(u"\2\u0594\u0595\7\6\2\2\u0595\u059f\5\u0162\u00b2\2\u0596")
        buf.write(u"\u0597\7\7\2\2\u0597\u059f\5\u017a\u00be\2\u0598\u0599")
        buf.write(u"\7\b\2\2\u0599\u059f\5\u00c8e\2\u059a\u059b\7\t\2\2\u059b")
        buf.write(u"\u059f\5\u00c8e\2\u059c\u059d\7\n\2\2\u059d\u059f\5\u00ce")
        buf.write(u"h\2\u059e\u0594\3\2\2\2\u059e\u0596\3\2\2\2\u059e\u0598")
        buf.write(u"\3\2\2\2\u059e\u059a\3\2\2\2\u059e\u059c\3\2\2\2\u059f")
        buf.write(u"\u00c7\3\2\2\2\u05a0\u05a2\5\u00a8U\2\u05a1\u05a3\5\u00ca")
        buf.write(u"f\2\u05a2\u05a1\3\2\2\2\u05a2\u05a3\3\2\2\2\u05a3\u00c9")
        buf.write(u"\3\2\2\2\u05a4\u05a5\7[\2\2\u05a5\u05a6\5\u00ccg\2\u05a6")
        buf.write(u"\u05a7\7\f\2\2\u05a7\u05ac\5\u00a8U\2\u05a8\u05a9\7\20")
        buf.write(u"\2\2\u05a9\u05ab\5\u00a8U\2\u05aa\u05a8\3\2\2\2\u05ab")
        buf.write(u"\u05ae\3\2\2\2\u05ac\u05aa\3\2\2\2\u05ac\u05ad\3\2\2")
        buf.write(u"\2\u05ad\u00cb\3\2\2\2\u05ae\u05ac\3\2\2\2\u05af\u05b0")
        buf.write(u"\7\u0090\2\2\u05b0\u05b1\6g\64\3\u05b1\u00cd\3\2\2\2")
        buf.write(u"\u05b2\u05b4\5\u00a8U\2\u05b3\u05b5\5\u00d0i\2\u05b4")
        buf.write(u"\u05b3\3\2\2\2\u05b4\u05b5\3\2\2\2\u05b5\u00cf\3\2\2")
        buf.write(u"\2\u05b6\u05b7\7[\2\2\u05b7\u05b8\5\u00ccg\2\u05b8\u05ba")
        buf.write(u"\7\f\2\2\u05b9\u05bb\7 \2\2\u05ba\u05b9\3\2\2\2\u05ba")
        buf.write(u"\u05bb\3\2\2\2\u05bb\u05bc\3\2\2\2\u05bc\u05c1\5\u0134")
        buf.write(u"\u009b\2\u05bd\u05be\7 \2\2\u05be\u05c0\5\u0134\u009b")
        buf.write(u"\2\u05bf\u05bd\3\2\2\2\u05c0\u05c3\3\2\2\2\u05c1\u05bf")
        buf.write(u"\3\2\2\2\u05c1\u05c2\3\2\2\2\u05c2\u05c6\3\2\2\2\u05c3")
        buf.write(u"\u05c1\3\2\2\2\u05c4\u05c5\7\20\2\2\u05c5\u05c7\5\u0134")
        buf.write(u"\u009b\2\u05c6\u05c4\3\2\2\2\u05c6\u05c7\3\2\2\2\u05c7")
        buf.write(u"\u00d1\3\2\2\2\u05c8\u05c9\bj\1\2\u05c9\u05ca\5\u00aa")
        buf.write(u"V\2\u05ca\u05d0\3\2\2\2\u05cb\u05cc\f\3\2\2\u05cc\u05cd")
        buf.write(u"\7\16\2\2\u05cd\u05cf\5\u00aaV\2\u05ce\u05cb\3\2\2\2")
        buf.write(u"\u05cf\u05d2\3\2\2\2\u05d0\u05ce\3\2\2\2\u05d0\u05d1")
        buf.write(u"\3\2\2\2\u05d1\u00d3\3\2\2\2\u05d2\u05d0\3\2\2\2\u05d3")
        buf.write(u"\u05d8\5$\23\2\u05d4\u05d8\5&\24\2\u05d5\u05d8\5(\25")
        buf.write(u"\2\u05d6\u05d8\5*\26\2\u05d7\u05d3\3\2\2\2\u05d7\u05d4")
        buf.write(u"\3\2\2\2\u05d7\u05d5\3\2\2\2\u05d7\u05d6\3\2\2\2\u05d8")
        buf.write(u"\u00d5\3\2\2\2\u05d9\u05da\bl\1\2\u05da\u05db\5\u00d8")
        buf.write(u"m\2\u05db\u05e2\3\2\2\2\u05dc\u05dd\f\3\2\2\u05dd\u05de")
        buf.write(u"\5\u011c\u008f\2\u05de\u05df\5\u00d8m\2\u05df\u05e1\3")
        buf.write(u"\2\2\2\u05e0\u05dc\3\2\2\2\u05e1\u05e4\3\2\2\2\u05e2")
        buf.write(u"\u05e0\3\2\2\2\u05e2\u05e3\3\2\2\2\u05e3\u00d7\3\2\2")
        buf.write(u"\2\u05e4\u05e2\3\2\2\2\u05e5\u05e6\7\6\2\2\u05e6\u05f0")
        buf.write(u"\5\u014e\u00a8\2\u05e7\u05e8\7\7\2\2\u05e8\u05f0\5\u0168")
        buf.write(u"\u00b5\2\u05e9\u05ea\7\b\2\2\u05ea\u05f0\5\u00dan\2\u05eb")
        buf.write(u"\u05ec\7\t\2\2\u05ec\u05f0\5\u00dan\2\u05ed\u05ee\7\n")
        buf.write(u"\2\2\u05ee\u05f0\5\u00dco\2\u05ef\u05e5\3\2\2\2\u05ef")
        buf.write(u"\u05e7\3\2\2\2\u05ef\u05e9\3\2\2\2\u05ef\u05eb\3\2\2")
        buf.write(u"\2\u05ef\u05ed\3\2\2\2\u05f0\u00d9\3\2\2\2\u05f1\u05f3")
        buf.write(u"\5\u0136\u009c\2\u05f2\u05f4\7\r\2\2\u05f3\u05f2\3\2")
        buf.write(u"\2\2\u05f3\u05f4\3\2\2\2\u05f4\u05f6\3\2\2\2\u05f5\u05f7")
        buf.write(u"\5\u00caf\2\u05f6\u05f5\3\2\2\2\u05f6\u05f7\3\2\2\2\u05f7")
        buf.write(u"\u00db\3\2\2\2\u05f8\u05fa\5\u011e\u0090\2\u05f9\u05fb")
        buf.write(u"\7\r\2\2\u05fa\u05f9\3\2\2\2\u05fa\u05fb\3\2\2\2\u05fb")
        buf.write(u"\u05fd\3\2\2\2\u05fc\u05fe\5\u00d0i\2\u05fd\u05fc\3\2")
        buf.write(u"\2\2\u05fd\u05fe\3\2\2\2\u05fe\u00dd\3\2\2\2\u05ff\u0600")
        buf.write(u"\bp\1\2\u0600\u0601\5\62\32\2\u0601\u0608\3\2\2\2\u0602")
        buf.write(u"\u0603\f\3\2\2\u0603\u0604\5\u011c\u008f\2\u0604\u0605")
        buf.write(u"\5\62\32\2\u0605\u0607\3\2\2\2\u0606\u0602\3\2\2\2\u0607")
        buf.write(u"\u060a\3\2\2\2\u0608\u0606\3\2\2\2\u0608\u0609\3\2\2")
        buf.write(u"\2\u0609\u00df\3\2\2\2\u060a\u0608\3\2\2\2\u060b\u060c")
        buf.write(u"\bq\1\2\u060c\u060d\5,\27\2\u060d\u0614\3\2\2\2\u060e")
        buf.write(u"\u060f\f\3\2\2\u060f\u0610\5\u011c\u008f\2\u0610\u0611")
        buf.write(u"\5,\27\2\u0611\u0613\3\2\2\2\u0612\u060e\3\2\2\2\u0613")
        buf.write(u"\u0616\3\2\2\2\u0614\u0612\3\2\2\2\u0614\u0615\3\2\2")
        buf.write(u"\2\u0615\u00e1\3\2\2\2\u0616\u0614\3\2\2\2\u0617\u0618")
        buf.write(u"\br\1\2\u0618\u0619\5<\37\2\u0619\u0620\3\2\2\2\u061a")
        buf.write(u"\u061b\f\3\2\2\u061b\u061c\5\u011c\u008f\2\u061c\u061d")
        buf.write(u"\5<\37\2\u061d\u061f\3\2\2\2\u061e\u061a\3\2\2\2\u061f")
        buf.write(u"\u0622\3\2\2\2\u0620\u061e\3\2\2\2\u0620\u0621\3\2\2")
        buf.write(u"\2\u0621\u00e3\3\2\2\2\u0622\u0620\3\2\2\2\u0623\u0624")
        buf.write(u"\bs\1\2\u0624\u0625\5L\'\2\u0625\u062c\3\2\2\2\u0626")
        buf.write(u"\u0627\f\3\2\2\u0627\u0628\5\u011c\u008f\2\u0628\u0629")
        buf.write(u"\5L\'\2\u0629\u062b\3\2\2\2\u062a\u0626\3\2\2\2\u062b")
        buf.write(u"\u062e\3\2\2\2\u062c\u062a\3\2\2\2\u062c\u062d\3\2\2")
        buf.write(u"\2\u062d\u00e5\3\2\2\2\u062e\u062c\3\2\2\2\u062f\u0630")
        buf.write(u"\7\23\2\2\u0630\u0631\5\u00e8u\2\u0631\u0632\7\17\2\2")
        buf.write(u"\u0632\u0633\5\u00e8u\2\u0633\u0634\7\24\2\2\u0634\u063e")
        buf.write(u"\3\2\2\2\u0635\u0636\7\23\2\2\u0636\u0637\5\u00eav\2")
        buf.write(u"\u0637\u0638\7\24\2\2\u0638\u063e\3\2\2\2\u0639\u063a")
        buf.write(u"\7%\2\2\u063a\u063b\5\u00eav\2\u063b\u063c\7#\2\2\u063c")
        buf.write(u"\u063e\3\2\2\2\u063d\u062f\3\2\2\2\u063d\u0635\3\2\2")
        buf.write(u"\2\u063d\u0639\3\2\2\2\u063e\u00e7\3\2\2\2\u063f\u064d")
        buf.write(u"\7\u008c\2\2\u0640\u064d\7\u008d\2\2\u0641\u064d\7\u0094")
        buf.write(u"\2\2\u0642\u064d\7\u0095\2\2\u0643\u064d\7\u008b\2\2")
        buf.write(u"\u0644\u064d\7\u0099\2\2\u0645\u064d\7\u0098\2\2\u0646")
        buf.write(u"\u064d\7\u0093\2\2\u0647\u064d\7\u0096\2\2\u0648\u064d")
        buf.write(u"\7\u0097\2\2\u0649\u064d\7\u008a\2\2\u064a\u064d\7\u009a")
        buf.write(u"\2\2\u064b\u064d\5z>\2\u064c\u063f\3\2\2\2\u064c\u0640")
        buf.write(u"\3\2\2\2\u064c\u0641\3\2\2\2\u064c\u0642\3\2\2\2\u064c")
        buf.write(u"\u0643\3\2\2\2\u064c\u0644\3\2\2\2\u064c\u0645\3\2\2")
        buf.write(u"\2\u064c\u0646\3\2\2\2\u064c\u0647\3\2\2\2\u064c\u0648")
        buf.write(u"\3\2\2\2\u064c\u0649\3\2\2\2\u064c\u064a\3\2\2\2\u064c")
        buf.write(u"\u064b\3\2\2\2\u064d\u00e9\3\2\2\2\u064e\u064f\bv\1\2")
        buf.write(u"\u064f\u0650\5\u00e8u\2\u0650\u0656\3\2\2\2\u0651\u0652")
        buf.write(u"\f\3\2\2\u0652\u0653\7\16\2\2\u0653\u0655\5\u00e8u\2")
        buf.write(u"\u0654\u0651\3\2\2\2\u0655\u0658\3\2\2\2\u0656\u0654")
        buf.write(u"\3\2\2\2\u0656\u0657\3\2\2\2\u0657\u00eb\3\2\2\2\u0658")
        buf.write(u"\u0656\3\2\2\2\u0659\u065e\5\u00f0y\2\u065a\u065e\5\u00f2")
        buf.write(u"z\2\u065b\u065e\5\u00a8U\2\u065c\u065e\5\u00eex\2\u065d")
        buf.write(u"\u0659\3\2\2\2\u065d\u065a\3\2\2\2\u065d\u065b\3\2\2")
        buf.write(u"\2\u065d\u065c\3\2\2\2\u065e\u00ed\3\2\2\2\u065f\u0660")
        buf.write(u"\t\3\2\2\u0660\u00ef\3\2\2\2\u0661\u0662\7\21\2\2\u0662")
        buf.write(u"\u0663\5X-\2\u0663\u0664\7\22\2\2\u0664\u00f1\3\2\2\2")
        buf.write(u"\u0665\u0668\5\u00e8u\2\u0666\u0668\5\u00f4{\2\u0667")
        buf.write(u"\u0665\3\2\2\2\u0667\u0666\3\2\2\2\u0668\u00f3\3\2\2")
        buf.write(u"\2\u0669\u066f\5\u0094K\2\u066a\u066f\5\u008eH\2\u066b")
        buf.write(u"\u066f\5\u0090I\2\u066c\u066f\5\u00f8}\2\u066d\u066f")
        buf.write(u"\5\u00f6|\2\u066e\u0669\3\2\2\2\u066e\u066a\3\2\2\2\u066e")
        buf.write(u"\u066b\3\2\2\2\u066e\u066c\3\2\2\2\u066e\u066d\3\2\2")
        buf.write(u"\2\u066f\u00f5\3\2\2\2\u0670\u0672\7\21\2\2\u0671\u0673")
        buf.write(u"\5\u00fa~\2\u0672\u0671\3\2\2\2\u0672\u0673\3\2\2\2\u0673")
        buf.write(u"\u0674\3\2\2\2\u0674\u0675\7\22\2\2\u0675\u00f7\3\2\2")
        buf.write(u"\2\u0676\u0678\7\25\2\2\u0677\u0679\5\u00fc\177\2\u0678")
        buf.write(u"\u0677\3\2\2\2\u0678\u0679\3\2\2\2\u0679\u067a\3\2\2")
        buf.write(u"\2\u067a\u067b\7\26\2\2\u067b\u00f9\3\2\2\2\u067c\u067d")
        buf.write(u"\b~\1\2\u067d\u067e\5X-\2\u067e\u0684\3\2\2\2\u067f\u0680")
        buf.write(u"\f\3\2\2\u0680\u0681\7\16\2\2\u0681\u0683\5X-\2\u0682")
        buf.write(u"\u067f\3\2\2\2\u0683\u0686\3\2\2\2\u0684\u0682\3\2\2")
        buf.write(u"\2\u0684\u0685\3\2\2\2\u0685\u00fb\3\2\2\2\u0686\u0684")
        buf.write(u"\3\2\2\2\u0687\u0688\b\177\1\2\u0688\u0689\5\u00fe\u0080")
        buf.write(u"\2\u0689\u068f\3\2\2\2\u068a\u068b\f\3\2\2\u068b\u068c")
        buf.write(u"\7\16\2\2\u068c\u068e\5\u00fe\u0080\2\u068d\u068a\3\2")
        buf.write(u"\2\2\u068e\u0691\3\2\2\2\u068f\u068d\3\2\2\2\u068f\u0690")
        buf.write(u"\3\2\2\2\u0690\u00fd\3\2\2\2\u0691\u068f\3\2\2\2\u0692")
        buf.write(u"\u0693\5X-\2\u0693\u0694\7\f\2\2\u0694\u0695\5X-\2\u0695")
        buf.write(u"\u00ff\3\2\2\2\u0696\u0697\5X-\2\u0697\u0698\7\f\2\2")
        buf.write(u"\u0698\u0699\5X-\2\u0699\u06a0\3\2\2\2\u069a\u069b\5")
        buf.write(u"X-\2\u069b\u069c\7\f\2\2\u069c\u06a0\3\2\2\2\u069d\u069e")
        buf.write(u"\7\f\2\2\u069e\u06a0\5X-\2\u069f\u0696\3\2\2\2\u069f")
        buf.write(u"\u069a\3\2\2\2\u069f\u069d\3\2\2\2\u06a0\u0101\3\2\2")
        buf.write(u"\2\u06a1\u06a2\5\u00aaV\2\u06a2\u06a3\5\u0110\u0089\2")
        buf.write(u"\u06a3\u06a4\5X-\2\u06a4\u0103\3\2\2\2\u06a5\u06a6\b")
        buf.write(u"\u0083\1\2\u06a6\u06a7\5\u00aaV\2\u06a7\u06ac\3\2\2\2")
        buf.write(u"\u06a8\u06a9\f\3\2\2\u06a9\u06ab\5v<\2\u06aa\u06a8\3")
        buf.write(u"\2\2\2\u06ab\u06ae\3\2\2\2\u06ac\u06aa\3\2\2\2\u06ac")
        buf.write(u"\u06ad\3\2\2\2\u06ad\u0105\3\2\2\2\u06ae\u06ac\3\2\2")
        buf.write(u"\2\u06af\u06b0\6\u0084?\3\u06b0\u06b1\7\u0090\2\2\u06b1")
        buf.write(u"\u06b4\5\u00ba^\2\u06b2\u06b4\5X-\2\u06b3\u06af\3\2\2")
        buf.write(u"\2\u06b3\u06b2\3\2\2\2\u06b4\u0107\3\2\2\2\u06b5\u06bc")
        buf.write(u"\7\35\2\2\u06b6\u06bc\7\36\2\2\u06b7\u06bc\5\u0112\u008a")
        buf.write(u"\2\u06b8\u06bc\5\u0114\u008b\2\u06b9\u06bc\5\u0116\u008c")
        buf.write(u"\2\u06ba\u06bc\5\u0118\u008d\2\u06bb\u06b5\3\2\2\2\u06bb")
        buf.write(u"\u06b6\3\2\2\2\u06bb\u06b7\3\2\2\2\u06bb\u06b8\3\2\2")
        buf.write(u"\2\u06bb\u06b9\3\2\2\2\u06bb\u06ba\3\2\2\2\u06bc\u0109")
        buf.write(u"\3\2\2\2\u06bd\u06be\7\u0090\2\2\u06be\u06bf\6\u0086")
        buf.write(u"@\3\u06bf\u010b\3\2\2\2\u06c0\u06c1\7\u0090\2\2\u06c1")
        buf.write(u"\u06c2\6\u0087A\3\u06c2\u010d\3\2\2\2\u06c3\u06c4\7\u0090")
        buf.write(u"\2\2\u06c4\u06c5\6\u0088B\3\u06c5\u010f\3\2\2\2\u06c6")
        buf.write(u"\u06c7\7(\2\2\u06c7\u0111\3\2\2\2\u06c8\u06c9\7\37\2")
        buf.write(u"\2\u06c9\u0113\3\2\2\2\u06ca\u06cb\7 \2\2\u06cb\u0115")
        buf.write(u"\3\2\2\2\u06cc\u06cd\7!\2\2\u06cd\u0117\3\2\2\2\u06ce")
        buf.write(u"\u06cf\t\4\2\2\u06cf\u0119\3\2\2\2\u06d0\u06d1\3\2\2")
        buf.write(u"\2\u06d1\u011b\3\2\2\2\u06d2\u06d3\3\2\2\2\u06d3\u011d")
        buf.write(u"\3\2\2\2\u06d4\u06d5\7v\2\2\u06d5\u06d6\5\u0120\u0091")
        buf.write(u"\2\u06d6\u06d7\7\r\2\2\u06d7\u06dc\3\2\2\2\u06d8\u06d9")
        buf.write(u"\5\u0120\u0091\2\u06d9\u06da\7\r\2\2\u06da\u06dc\3\2")
        buf.write(u"\2\2\u06db\u06d4\3\2\2\2\u06db\u06d8\3\2\2\2\u06dc\u011f")
        buf.write(u"\3\2\2\2\u06dd\u06de\b\u0091\1\2\u06de\u06df\5\u0122")
        buf.write(u"\u0092\2\u06df\u06e4\3\2\2\2\u06e0\u06e1\f\3\2\2\u06e1")
        buf.write(u"\u06e3\5\u0126\u0094\2\u06e2\u06e0\3\2\2\2\u06e3\u06e6")
        buf.write(u"\3\2\2\2\u06e4\u06e2\3\2\2\2\u06e4\u06e5\3\2\2\2\u06e5")
        buf.write(u"\u0121\3\2\2\2\u06e6\u06e4\3\2\2\2\u06e7\u06ee\5\u0124")
        buf.write(u"\u0093\2\u06e8\u06ee\5\u012e\u0098\2\u06e9\u06ee\5\u0130")
        buf.write(u"\u0099\2\u06ea\u06ee\5\u0132\u009a\2\u06eb\u06ee\5\u0128")
        buf.write(u"\u0095\2\u06ec\u06ee\5\u012c\u0097\2\u06ed\u06e7\3\2")
        buf.write(u"\2\2\u06ed\u06e8\3\2\2\2\u06ed\u06e9\3\2\2\2\u06ed\u06ea")
        buf.write(u"\3\2\2\2\u06ed\u06eb\3\2\2\2\u06ed\u06ec\3\2\2\2\u06ee")
        buf.write(u"\u0123\3\2\2\2\u06ef\u06f0\5\u00eex\2\u06f0\u0125\3\2")
        buf.write(u"\2\2\u06f1\u06f2\7\20\2\2\u06f2\u06f7\5\u0128\u0095\2")
        buf.write(u"\u06f3\u06f4\7\20\2\2\u06f4\u06f7\5\u0134\u009b\2\u06f5")
        buf.write(u"\u06f7\5\u012c\u0097\2\u06f6\u06f1\3\2\2\2\u06f6\u06f3")
        buf.write(u"\3\2\2\2\u06f6\u06f5\3\2\2\2\u06f7\u0127\3\2\2\2\u06f8")
        buf.write(u"\u06f9\5\u0134\u009b\2\u06f9\u06fb\7\21\2\2\u06fa\u06fc")
        buf.write(u"\5\u012a\u0096\2\u06fb\u06fa\3\2\2\2\u06fb\u06fc\3\2")
        buf.write(u"\2\2\u06fc\u06fd\3\2\2\2\u06fd\u06fe\7\22\2\2\u06fe\u0129")
        buf.write(u"\3\2\2\2\u06ff\u0700\b\u0096\1\2\u0700\u0701\5\u0120")
        buf.write(u"\u0091\2\u0701\u0707\3\2\2\2\u0702\u0703\f\3\2\2\u0703")
        buf.write(u"\u0704\7\16\2\2\u0704\u0706\5\u0120\u0091\2\u0705\u0702")
        buf.write(u"\3\2\2\2\u0706\u0709\3\2\2\2\u0707\u0705\3\2\2\2\u0707")
        buf.write(u"\u0708\3\2\2\2\u0708\u012b\3\2\2\2\u0709\u0707\3\2\2")
        buf.write(u"\2\u070a\u070b\7\23\2\2\u070b\u070c\5\u0120\u0091\2\u070c")
        buf.write(u"\u070d\7\24\2\2\u070d\u012d\3\2\2\2\u070e\u070f\7\21")
        buf.write(u"\2\2\u070f\u0710\5\u0120\u0091\2\u0710\u0711\7\22\2\2")
        buf.write(u"\u0711\u012f\3\2\2\2\u0712\u0713\5\u0134\u009b\2\u0713")
        buf.write(u"\u0131\3\2\2\2\u0714\u071a\7\u0094\2\2\u0715\u071a\7")
        buf.write(u"\u0096\2\2\u0716\u071a\7\u0093\2\2\u0717\u071a\7\u008a")
        buf.write(u"\2\2\u0718\u071a\7\u008b\2\2\u0719\u0714\3\2\2\2\u0719")
        buf.write(u"\u0715\3\2\2\2\u0719\u0716\3\2\2\2\u0719\u0717\3\2\2")
        buf.write(u"\2\u0719\u0718\3\2\2\2\u071a\u0133\3\2\2\2\u071b\u071c")
        buf.write(u"\t\5\2\2\u071c\u0135\3\2\2\2\u071d\u071e\7v\2\2\u071e")
        buf.write(u"\u0721\5\u0138\u009d\2\u071f\u0721\5\u0138\u009d\2\u0720")
        buf.write(u"\u071d\3\2\2\2\u0720\u071f\3\2\2\2\u0721\u0137\3\2\2")
        buf.write(u"\2\u0722\u0723\b\u009d\1\2\u0723\u0724\5\u013a\u009e")
        buf.write(u"\2\u0724\u0729\3\2\2\2\u0725\u0726\f\3\2\2\u0726\u0728")
        buf.write(u"\5\u013c\u009f\2\u0727\u0725\3\2\2\2\u0728\u072b\3\2")
        buf.write(u"\2\2\u0729\u0727\3\2\2\2\u0729\u072a\3\2\2\2\u072a\u0139")
        buf.write(u"\3\2\2\2\u072b\u0729\3\2\2\2\u072c\u0731\5\u0146\u00a4")
        buf.write(u"\2\u072d\u0731\5\u0148\u00a5\2\u072e\u0731\5\u014a\u00a6")
        buf.write(u"\2\u072f\u0731\5\u013e\u00a0\2\u0730\u072c\3\2\2\2\u0730")
        buf.write(u"\u072d\3\2\2\2\u0730\u072e\3\2\2\2\u0730\u072f\3\2\2")
        buf.write(u"\2\u0731\u013b\3\2\2\2\u0732\u0733\7\20\2\2\u0733\u0739")
        buf.write(u"\5\u013e\u00a0\2\u0734\u0735\7\23\2\2\u0735\u0736\5\u0138")
        buf.write(u"\u009d\2\u0736\u0737\7\24\2\2\u0737\u0739\3\2\2\2\u0738")
        buf.write(u"\u0732\3\2\2\2\u0738\u0734\3\2\2\2\u0739\u013d\3\2\2")
        buf.write(u"\2\u073a\u073b\5\u014c\u00a7\2\u073b\u073d\7\21\2\2\u073c")
        buf.write(u"\u073e\5\u0140\u00a1\2\u073d\u073c\3\2\2\2\u073d\u073e")
        buf.write(u"\3\2\2\2\u073e\u073f\3\2\2\2\u073f\u0740\7\22\2\2\u0740")
        buf.write(u"\u013f\3\2\2\2\u0741\u0748\5\u0142\u00a2\2\u0742\u0748")
        buf.write(u"\5\u0144\u00a3\2\u0743\u0744\5\u0142\u00a2\2\u0744\u0745")
        buf.write(u"\7\16\2\2\u0745\u0746\5\u0144\u00a3\2\u0746\u0748\3\2")
        buf.write(u"\2\2\u0747\u0741\3\2\2\2\u0747\u0742\3\2\2\2\u0747\u0743")
        buf.write(u"\3\2\2\2\u0748\u0141\3\2\2\2\u0749\u074a\b\u00a2\1\2")
        buf.write(u"\u074a\u074b\5\u0138\u009d\2\u074b\u0751\3\2\2\2\u074c")
        buf.write(u"\u074d\f\3\2\2\u074d\u074e\7\16\2\2\u074e\u0750\5\u0138")
        buf.write(u"\u009d\2\u074f\u074c\3\2\2\2\u0750\u0753\3\2\2\2\u0751")
        buf.write(u"\u074f\3\2\2\2\u0751\u0752\3\2\2\2\u0752\u0143\3\2\2")
        buf.write(u"\2\u0753\u0751\3\2\2\2\u0754\u0755\b\u00a3\1\2\u0755")
        buf.write(u"\u0756\5\u014c\u00a7\2\u0756\u0757\7(\2\2\u0757\u0758")
        buf.write(u"\5\u0138\u009d\2\u0758\u0761\3\2\2\2\u0759\u075a\f\3")
        buf.write(u"\2\2\u075a\u075b\7\16\2\2\u075b\u075c\5\u014c\u00a7\2")
        buf.write(u"\u075c\u075d\7(\2\2\u075d\u075e\5\u0138\u009d\2\u075e")
        buf.write(u"\u0760\3\2\2\2\u075f\u0759\3\2\2\2\u0760\u0763\3\2\2")
        buf.write(u"\2\u0761\u075f\3\2\2\2\u0761\u0762\3\2\2\2\u0762\u0145")
        buf.write(u"\3\2\2\2\u0763\u0761\3\2\2\2\u0764\u0765\7\21\2\2\u0765")
        buf.write(u"\u0766\5\u0138\u009d\2\u0766\u0767\7\22\2\2\u0767\u0147")
        buf.write(u"\3\2\2\2\u0768\u0769\b\u00a5\1\2\u0769\u076c\7\u0092")
        buf.write(u"\2\2\u076a\u076c\5\u014c\u00a7\2\u076b\u0768\3\2\2\2")
        buf.write(u"\u076b\u076a\3\2\2\2\u076c\u0772\3\2\2\2\u076d\u076e")
        buf.write(u"\f\3\2\2\u076e\u076f\7\20\2\2\u076f\u0771\5\u014c\u00a7")
        buf.write(u"\2\u0770\u076d\3\2\2\2\u0771\u0774\3\2\2\2\u0772\u0770")
        buf.write(u"\3\2\2\2\u0772\u0773\3\2\2\2\u0773\u0149\3\2\2\2\u0774")
        buf.write(u"\u0772\3\2\2\2\u0775\u077b\7\u0094\2\2\u0776\u077b\7")
        buf.write(u"\u0096\2\2\u0777\u077b\7\u0093\2\2\u0778\u077b\7\u008a")
        buf.write(u"\2\2\u0779\u077b\7\u008b\2\2\u077a\u0775\3\2\2\2\u077a")
        buf.write(u"\u0776\3\2\2\2\u077a\u0777\3\2\2\2\u077a\u0778\3\2\2")
        buf.write(u"\2\u077a\u0779\3\2\2\2\u077b\u014b\3\2\2\2\u077c\u077d")
        buf.write(u"\t\6\2\2\u077d\u014d\3\2\2\2\u077e\u077f\7v\2\2\u077f")
        buf.write(u"\u0780\5\u0150\u00a9\2\u0780\u0781\7\r\2\2\u0781\u0786")
        buf.write(u"\3\2\2\2\u0782\u0783\5\u0150\u00a9\2\u0783\u0784\7\r")
        buf.write(u"\2\2\u0784\u0786\3\2\2\2\u0785\u077e\3\2\2\2\u0785\u0782")
        buf.write(u"\3\2\2\2\u0786\u014f\3\2\2\2\u0787\u0788\b\u00a9\1\2")
        buf.write(u"\u0788\u0789\5\u0152\u00aa\2\u0789\u078e\3\2\2\2\u078a")
        buf.write(u"\u078b\f\3\2\2\u078b\u078d\5\u0156\u00ac\2\u078c\u078a")
        buf.write(u"\3\2\2\2\u078d\u0790\3\2\2\2\u078e\u078c\3\2\2\2\u078e")
        buf.write(u"\u078f\3\2\2\2\u078f\u0151\3\2\2\2\u0790\u078e\3\2\2")
        buf.write(u"\2\u0791\u0796\5\u0154\u00ab\2\u0792\u0796\5\u015e\u00b0")
        buf.write(u"\2\u0793\u0796\5\u0160\u00b1\2\u0794\u0796\5\u0164\u00b3")
        buf.write(u"\2\u0795\u0791\3\2\2\2\u0795\u0792\3\2\2\2\u0795\u0793")
        buf.write(u"\3\2\2\2\u0795\u0794\3\2\2\2\u0796\u0153\3\2\2\2\u0797")
        buf.write(u"\u0798\5\u00eex\2\u0798\u0155\3\2\2\2\u0799\u079a\7\20")
        buf.write(u"\2\2\u079a\u079d\5\u0158\u00ad\2\u079b\u079d\5\u015c")
        buf.write(u"\u00af\2\u079c\u0799\3\2\2\2\u079c\u079b\3\2\2\2\u079d")
        buf.write(u"\u0157\3\2\2\2\u079e\u079f\5\u0166\u00b4\2\u079f\u07a1")
        buf.write(u"\7\21\2\2\u07a0\u07a2\5\u015a\u00ae\2\u07a1\u07a0\3\2")
        buf.write(u"\2\2\u07a1\u07a2\3\2\2\2\u07a2\u07a3\3\2\2\2\u07a3\u07a4")
        buf.write(u"\7\22\2\2\u07a4\u0159\3\2\2\2\u07a5\u07a6\b\u00ae\1\2")
        buf.write(u"\u07a6\u07a7\5\u0150\u00a9\2\u07a7\u07ad\3\2\2\2\u07a8")
        buf.write(u"\u07a9\f\3\2\2\u07a9\u07aa\7\16\2\2\u07aa\u07ac\5\u0150")
        buf.write(u"\u00a9\2\u07ab\u07a8\3\2\2\2\u07ac\u07af\3\2\2\2\u07ad")
        buf.write(u"\u07ab\3\2\2\2\u07ad\u07ae\3\2\2\2\u07ae\u015b\3\2\2")
        buf.write(u"\2\u07af\u07ad\3\2\2\2\u07b0\u07b1\7\23\2\2\u07b1\u07b2")
        buf.write(u"\5\u0150\u00a9\2\u07b2\u07b3\7\24\2\2\u07b3\u015d\3\2")
        buf.write(u"\2\2\u07b4\u07b5\7\21\2\2\u07b5\u07b6\5\u0150\u00a9\2")
        buf.write(u"\u07b6\u07b7\7\22\2\2\u07b7\u015f\3\2\2\2\u07b8\u07b9")
        buf.write(u"\b\u00b1\1\2\u07b9\u07ba\5\u0166\u00b4\2\u07ba\u07c0")
        buf.write(u"\3\2\2\2\u07bb\u07bc\f\3\2\2\u07bc\u07bd\7\20\2\2\u07bd")
        buf.write(u"\u07bf\5\u0166\u00b4\2\u07be\u07bb\3\2\2\2\u07bf\u07c2")
        buf.write(u"\3\2\2\2\u07c0\u07be\3\2\2\2\u07c0\u07c1\3\2\2\2\u07c1")
        buf.write(u"\u0161\3\2\2\2\u07c2\u07c0\3\2\2\2\u07c3\u07c4\b\u00b2")
        buf.write(u"\1\2\u07c4\u07c5\5\u0160\u00b1\2\u07c5\u07ca\3\2\2\2")
        buf.write(u"\u07c6\u07c7\f\3\2\2\u07c7\u07c9\7\u0092\2\2\u07c8\u07c6")
        buf.write(u"\3\2\2\2\u07c9\u07cc\3\2\2\2\u07ca\u07c8\3\2\2\2\u07ca")
        buf.write(u"\u07cb\3\2\2\2\u07cb\u0163\3\2\2\2\u07cc\u07ca\3\2\2")
        buf.write(u"\2\u07cd\u07d3\7\u0094\2\2\u07ce\u07d3\7\u0096\2\2\u07cf")
        buf.write(u"\u07d3\7\u0093\2\2\u07d0\u07d3\7\u008a\2\2\u07d1\u07d3")
        buf.write(u"\7\u008b\2\2\u07d2\u07cd\3\2\2\2\u07d2\u07ce\3\2\2\2")
        buf.write(u"\u07d2\u07cf\3\2\2\2\u07d2\u07d0\3\2\2\2\u07d2\u07d1")
        buf.write(u"\3\2\2\2\u07d3\u0165\3\2\2\2\u07d4\u07d5\t\7\2\2\u07d5")
        buf.write(u"\u0167\3\2\2\2\u07d6\u07d7\7v\2\2\u07d7\u07d8\5\u016a")
        buf.write(u"\u00b6\2\u07d8\u07d9\7\r\2\2\u07d9\u07de\3\2\2\2\u07da")
        buf.write(u"\u07db\5\u016a\u00b6\2\u07db\u07dc\7\r\2\2\u07dc\u07de")
        buf.write(u"\3\2\2\2\u07dd\u07d6\3\2\2\2\u07dd\u07da\3\2\2\2\u07de")
        buf.write(u"\u0169\3\2\2\2\u07df\u07e0\b\u00b6\1\2\u07e0\u07e1\5")
        buf.write(u"\u016c\u00b7\2\u07e1\u07e6\3\2\2\2\u07e2\u07e3\f\3\2")
        buf.write(u"\2\u07e3\u07e5\5\u0170\u00b9\2\u07e4\u07e2\3\2\2\2\u07e5")
        buf.write(u"\u07e8\3\2\2\2\u07e6\u07e4\3\2\2\2\u07e6\u07e7\3\2\2")
        buf.write(u"\2\u07e7\u016b\3\2\2\2\u07e8\u07e6\3\2\2\2\u07e9\u07ee")
        buf.write(u"\5\u016e\u00b8\2\u07ea\u07ee\5\u0178\u00bd\2\u07eb\u07ee")
        buf.write(u"\5\u017a\u00be\2\u07ec\u07ee\5\u017c\u00bf\2\u07ed\u07e9")
        buf.write(u"\3\2\2\2\u07ed\u07ea\3\2\2\2\u07ed\u07eb\3\2\2\2\u07ed")
        buf.write(u"\u07ec\3\2\2\2\u07ee\u016d\3\2\2\2\u07ef\u07f0\5\u00ee")
        buf.write(u"x\2\u07f0\u016f\3\2\2\2\u07f1\u07f2\7\20\2\2\u07f2\u07f5")
        buf.write(u"\5\u0172\u00ba\2\u07f3\u07f5\5\u0176\u00bc\2\u07f4\u07f1")
        buf.write(u"\3\2\2\2\u07f4\u07f3\3\2\2\2\u07f5\u0171\3\2\2\2\u07f6")
        buf.write(u"\u07f7\5\u017e\u00c0\2\u07f7\u07f9\7\21\2\2\u07f8\u07fa")
        buf.write(u"\5\u0174\u00bb\2\u07f9\u07f8\3\2\2\2\u07f9\u07fa\3\2")
        buf.write(u"\2\2\u07fa\u07fb\3\2\2\2\u07fb\u07fc\7\22\2\2\u07fc\u0173")
        buf.write(u"\3\2\2\2\u07fd\u07fe\b\u00bb\1\2\u07fe\u07ff\5\u016a")
        buf.write(u"\u00b6\2\u07ff\u0805\3\2\2\2\u0800\u0801\f\3\2\2\u0801")
        buf.write(u"\u0802\7\16\2\2\u0802\u0804\5\u016a\u00b6\2\u0803\u0800")
        buf.write(u"\3\2\2\2\u0804\u0807\3\2\2\2\u0805\u0803\3\2\2\2\u0805")
        buf.write(u"\u0806\3\2\2\2\u0806\u0175\3\2\2\2\u0807\u0805\3\2\2")
        buf.write(u"\2\u0808\u0809\7\23\2\2\u0809\u080a\5\u016a\u00b6\2\u080a")
        buf.write(u"\u080b\7\24\2\2\u080b\u0177\3\2\2\2\u080c\u080d\7\21")
        buf.write(u"\2\2\u080d\u080e\5\u016a\u00b6\2\u080e\u080f\7\22\2\2")
        buf.write(u"\u080f\u0179\3\2\2\2\u0810\u0811\b\u00be\1\2\u0811\u0814")
        buf.write(u"\7\u0092\2\2\u0812\u0814\5\u017e\u00c0\2\u0813\u0810")
        buf.write(u"\3\2\2\2\u0813\u0812\3\2\2\2\u0814\u081a\3\2\2\2\u0815")
        buf.write(u"\u0816\f\3\2\2\u0816\u0817\7\20\2\2\u0817\u0819\5\u017e")
        buf.write(u"\u00c0\2\u0818\u0815\3\2\2\2\u0819\u081c\3\2\2\2\u081a")
        buf.write(u"\u0818\3\2\2\2\u081a\u081b\3\2\2\2\u081b\u017b\3\2\2")
        buf.write(u"\2\u081c\u081a\3\2\2\2\u081d\u0823\7\u0094\2\2\u081e")
        buf.write(u"\u0823\7\u0096\2\2\u081f\u0823\7\u0093\2\2\u0820\u0823")
        buf.write(u"\7\u008a\2\2\u0821\u0823\7\u008b\2\2\u0822\u081d\3\2")
        buf.write(u"\2\2\u0822\u081e\3\2\2\2\u0822\u081f\3\2\2\2\u0822\u0820")
        buf.write(u"\3\2\2\2\u0822\u0821\3\2\2\2\u0823\u017d\3\2\2\2\u0824")
        buf.write(u"\u0825\t\b\2\2\u0825\u017f\3\2\2\2\u00b0\u0187\u018b")
        buf.write(u"\u01a6\u01ad\u01b2\u01ba\u01be\u01c8\u01d4\u01da\u01dd")
        buf.write(u"\u01e0\u01e9\u01f1\u01f9\u0204\u0209\u020e\u0217\u021c")
        buf.write(u"\u0230\u023b\u0240\u0246\u024c\u0252\u0257\u025c\u0263")
        buf.write(u"\u027a\u0284\u0289\u0290\u0292\u02a6\u02c3\u02c5\u02cd")
        buf.write(u"\u02d4\u02d6\u02de\u02e8\u02fd\u0301\u0315\u0322\u0326")
        buf.write(u"\u032e\u0331\u0336\u0339\u0341\u034c\u0350\u0354\u035b")
        buf.write(u"\u0364\u036d\u0376\u038f\u03f3\u03f5\u0405\u040e\u043a")
        buf.write(u"\u0444\u0446\u0450\u045e\u0461\u0466\u046f\u0476\u0488")
        buf.write(u"\u0492\u04a0\u04a8\u04ae\u04b9\u04c5\u04d0\u04dd\u04e1")
        buf.write(u"\u04e7\u04f3\u0507\u0509\u050e\u051a\u0525\u052f\u0534")
        buf.write(u"\u0539\u0549\u054e\u0551\u0555\u055a\u0561\u056c\u056e")
        buf.write(u"\u057a\u0582\u058d\u0592\u059e\u05a2\u05ac\u05b4\u05ba")
        buf.write(u"\u05c1\u05c6\u05d0\u05d7\u05e2\u05ef\u05f3\u05f6\u05fa")
        buf.write(u"\u05fd\u0608\u0614\u0620\u062c\u063d\u064c\u0656\u065d")
        buf.write(u"\u0667\u066e\u0672\u0678\u0684\u068f\u069f\u06ac\u06b3")
        buf.write(u"\u06bb\u06db\u06e4\u06ed\u06f6\u06fb\u0707\u0719\u0720")
        buf.write(u"\u0729\u0730\u0738\u073d\u0747\u0751\u0761\u076b\u0772")
        buf.write(u"\u077a\u0785\u078e\u0795\u079c\u07a1\u07ad\u07c0\u07ca")
        buf.write(u"\u07d2\u07dd\u07e6\u07ed\u07f4\u07f9\u0805\u0813\u081a")
        buf.write(u"\u0822")
        return buf.getvalue()
		

class OParser ( AbstractParser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"' '", u"<INVALID>", u"<INVALID>", u"'Java:'", 
                     u"'C#:'", u"'Python2:'", u"'Python3:'", u"'JavaScript:'", 
                     u"'Swift:'", u"':'", u"';'", u"','", u"'..'", u"'.'", 
                     u"'('", u"')'", u"'['", u"']'", u"'{'", u"'}'", u"'?'", 
                     u"'!'", u"'&'", u"'&&'", u"'|'", u"'||'", u"'+'", u"'-'", 
                     u"'*'", u"'/'", u"'\\'", u"'%'", u"'>'", u"'>='", u"'<'", 
                     u"'<='", u"'<>'", u"'='", u"'!='", u"'=='", u"'~='", 
                     u"'~'", u"'<-'", u"'->'", u"'Boolean'", u"'Character'", 
                     u"'Text'", u"'Integer'", u"'Decimal'", u"'Date'", u"'Time'", 
                     u"'DateTime'", u"'Period'", u"'Method'", u"'Code'", 
                     u"'Document'", u"'abstract'", u"'all'", u"'always'", 
                     u"'and'", u"'any'", u"'as'", u"'attr'", u"'attribute'", 
                     u"'attributes'", u"'bindings'", u"'case'", u"'catch'", 
                     u"'category'", u"'class'", u"'close'", u"'contains'", 
                     u"'def'", u"'default'", u"'define'", u"'do'", u"'doing'", 
                     u"'each'", u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'finally'", u"'for'", u"'from'", u"'getter'", u"'if'", 
                     u"'in'", u"'invoke'", u"'is'", u"'matching'", u"'method'", 
                     u"'methods'", u"'modulo'", u"'mutable'", u"'native'", 
                     u"'None'", u"'not'", u"<INVALID>", u"'null'", u"'on'", 
                     u"'one'", u"'open'", u"'operator'", u"'or'", u"'otherwise'", 
                     u"'pass'", u"'raise'", u"'read'", u"'receiving'", u"'resource'", 
                     u"'return'", u"'returning'", u"'rows'", u"'self'", 
                     u"'setter'", u"'singleton'", u"'sorted'", u"'storable'", 
                     u"'store'", u"'switch'", u"'test'", u"'this'", u"'throw'", 
                     u"'to'", u"'try'", u"'with'", u"'when'", u"'where'", 
                     u"'while'", u"'write'", u"<INVALID>", u"<INVALID>", 
                     u"'MIN_INTEGER'", u"'MAX_INTEGER'" ]

    symbolicNames = [ u"<INVALID>", u"SPACE", u"WS", u"LF", u"JAVA", u"CSHARP", 
                      u"PYTHON2", u"PYTHON3", u"JAVASCRIPT", u"SWIFT", u"COLON", 
                      u"SEMI", u"COMMA", u"RANGE", u"DOT", u"LPAR", u"RPAR", 
                      u"LBRAK", u"RBRAK", u"LCURL", u"RCURL", u"QMARK", 
                      u"XMARK", u"AMP", u"AMP2", u"PIPE", u"PIPE2", u"PLUS", 
                      u"MINUS", u"STAR", u"SLASH", u"BSLASH", u"PERCENT", 
                      u"GT", u"GTE", u"LT", u"LTE", u"LTGT", u"EQ", u"XEQ", 
                      u"EQ2", u"TEQ", u"TILDE", u"LARROW", u"RARROW", u"BOOLEAN", 
                      u"CHARACTER", u"TEXT", u"INTEGER", u"DECIMAL", u"DATE", 
                      u"TIME", u"DATETIME", u"PERIOD", u"METHOD_T", u"CODE", 
                      u"DOCUMENT", u"ABSTRACT", u"ALL", u"ALWAYS", u"AND", 
                      u"ANY", u"AS", u"ATTR", u"ATTRIBUTE", u"ATTRIBUTES", 
                      u"BINDINGS", u"CASE", u"CATCH", u"CATEGORY", u"CLASS", 
                      u"CLOSE", u"CONTAINS", u"DEF", u"DEFAULT", u"DEFINE", 
                      u"DO", u"DOING", u"EACH", u"ELSE", u"ENUM", u"ENUMERATED", 
                      u"EXCEPT", u"EXECUTE", u"EXPECTING", u"EXTENDS", u"FETCH", 
                      u"FINALLY", u"FOR", u"FROM", u"GETTER", u"IF", u"IN", 
                      u"INVOKE", u"IS", u"MATCHING", u"METHOD", u"METHODS", 
                      u"MODULO", u"MUTABLE", u"NATIVE", u"NONE", u"NOT", 
                      u"NOTHING", u"NULL", u"ON", u"ONE", u"OPEN", u"OPERATOR", 
                      u"OR", u"OTHERWISE", u"PASS", u"RAISE", u"READ", u"RECEIVING", 
                      u"RESOURCE", u"RETURN", u"RETURNING", u"ROWS", u"SELF", 
                      u"SETTER", u"SINGLETON", u"SORTED", u"STORABLE", u"STORE", 
                      u"SWITCH", u"TEST", u"THIS", u"THROW", u"TO", u"TRY", 
                      u"WITH", u"WHEN", u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
                      u"CHAR_LITERAL", u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"INTEGER_LITERAL", 
                      u"HEXA_LITERAL", u"DECIMAL_LITERAL", u"DATETIME_LITERAL", 
                      u"TIME_LITERAL", u"DATE_LITERAL", u"PERIOD_LITERAL", 
                      u"COMMENT" ]

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
    RULE_getter_method_declaration = 11
    RULE_native_resource_declaration = 12
    RULE_native_category_declaration = 13
    RULE_native_category_bindings = 14
    RULE_native_category_binding_list = 15
    RULE_attribute_list = 16
    RULE_abstract_method_declaration = 17
    RULE_concrete_method_declaration = 18
    RULE_native_method_declaration = 19
    RULE_test_method_declaration = 20
    RULE_assertion = 21
    RULE_typed_argument = 22
    RULE_statement_or_list = 23
    RULE_statement = 24
    RULE_store_statement = 25
    RULE_with_resource_statement = 26
    RULE_with_singleton_statement = 27
    RULE_switch_statement = 28
    RULE_switch_case_statement = 29
    RULE_for_each_statement = 30
    RULE_do_while_statement = 31
    RULE_while_statement = 32
    RULE_if_statement = 33
    RULE_else_if_statement_list = 34
    RULE_raise_statement = 35
    RULE_try_statement = 36
    RULE_catch_statement = 37
    RULE_return_statement = 38
    RULE_method_call = 39
    RULE_method_selector = 40
    RULE_callable_parent = 41
    RULE_callable_selector = 42
    RULE_expression = 43
    RULE_an_expression = 44
    RULE_closure_expression = 45
    RULE_instance_expression = 46
    RULE_method_expression = 47
    RULE_document_expression = 48
    RULE_read_expression = 49
    RULE_write_statement = 50
    RULE_fetch_expression = 51
    RULE_sorted_expression = 52
    RULE_selector_expression = 53
    RULE_constructor_expression = 54
    RULE_argument_assignment_list = 55
    RULE_argument_assignment = 56
    RULE_assign_instance_statement = 57
    RULE_child_instance = 58
    RULE_assign_tuple_statement = 59
    RULE_null_literal = 60
    RULE_declaration_list = 61
    RULE_declarations = 62
    RULE_declaration = 63
    RULE_resource_declaration = 64
    RULE_enum_declaration = 65
    RULE_native_symbol_list = 66
    RULE_category_symbol_list = 67
    RULE_symbol_list = 68
    RULE_attribute_constraint = 69
    RULE_list_literal = 70
    RULE_set_literal = 71
    RULE_expression_list = 72
    RULE_range_literal = 73
    RULE_typedef = 74
    RULE_primary_type = 75
    RULE_native_type = 76
    RULE_category_type = 77
    RULE_code_type = 78
    RULE_document_type = 79
    RULE_category_declaration = 80
    RULE_type_identifier_list = 81
    RULE_method_identifier = 82
    RULE_identifier = 83
    RULE_variable_identifier = 84
    RULE_type_identifier = 85
    RULE_symbol_identifier = 86
    RULE_argument_list = 87
    RULE_argument = 88
    RULE_operator_argument = 89
    RULE_named_argument = 90
    RULE_code_argument = 91
    RULE_category_or_any_type = 92
    RULE_any_type = 93
    RULE_member_method_declaration_list = 94
    RULE_member_method_declaration = 95
    RULE_native_member_method_declaration_list = 96
    RULE_native_member_method_declaration = 97
    RULE_native_category_binding = 98
    RULE_python_category_binding = 99
    RULE_python_module = 100
    RULE_module_token = 101
    RULE_javascript_category_binding = 102
    RULE_javascript_module = 103
    RULE_variable_identifier_list = 104
    RULE_method_declaration = 105
    RULE_native_statement_list = 106
    RULE_native_statement = 107
    RULE_python_native_statement = 108
    RULE_javascript_native_statement = 109
    RULE_statement_list = 110
    RULE_assertion_list = 111
    RULE_switch_case_statement_list = 112
    RULE_catch_statement_list = 113
    RULE_literal_collection = 114
    RULE_atomic_literal = 115
    RULE_literal_list_literal = 116
    RULE_selectable_expression = 117
    RULE_this_expression = 118
    RULE_parenthesis_expression = 119
    RULE_literal_expression = 120
    RULE_collection_literal = 121
    RULE_tuple_literal = 122
    RULE_dict_literal = 123
    RULE_expression_tuple = 124
    RULE_dict_entry_list = 125
    RULE_dict_entry = 126
    RULE_slice_arguments = 127
    RULE_assign_variable_statement = 128
    RULE_assignable_instance = 129
    RULE_is_expression = 130
    RULE_operator = 131
    RULE_key_token = 132
    RULE_value_token = 133
    RULE_symbols_token = 134
    RULE_assign = 135
    RULE_multiply = 136
    RULE_divide = 137
    RULE_idivide = 138
    RULE_modulo = 139
    RULE_lfs = 140
    RULE_lfp = 141
    RULE_javascript_statement = 142
    RULE_javascript_expression = 143
    RULE_javascript_primary_expression = 144
    RULE_javascript_this_expression = 145
    RULE_javascript_selector_expression = 146
    RULE_javascript_method_expression = 147
    RULE_javascript_arguments = 148
    RULE_javascript_item_expression = 149
    RULE_javascript_parenthesis_expression = 150
    RULE_javascript_identifier_expression = 151
    RULE_javascript_literal_expression = 152
    RULE_javascript_identifier = 153
    RULE_python_statement = 154
    RULE_python_expression = 155
    RULE_python_primary_expression = 156
    RULE_python_selector_expression = 157
    RULE_python_method_expression = 158
    RULE_python_argument_list = 159
    RULE_python_ordinal_argument_list = 160
    RULE_python_named_argument_list = 161
    RULE_python_parenthesis_expression = 162
    RULE_python_identifier_expression = 163
    RULE_python_literal_expression = 164
    RULE_python_identifier = 165
    RULE_java_statement = 166
    RULE_java_expression = 167
    RULE_java_primary_expression = 168
    RULE_java_this_expression = 169
    RULE_java_selector_expression = 170
    RULE_java_method_expression = 171
    RULE_java_arguments = 172
    RULE_java_item_expression = 173
    RULE_java_parenthesis_expression = 174
    RULE_java_identifier_expression = 175
    RULE_java_class_identifier_expression = 176
    RULE_java_literal_expression = 177
    RULE_java_identifier = 178
    RULE_csharp_statement = 179
    RULE_csharp_expression = 180
    RULE_csharp_primary_expression = 181
    RULE_csharp_this_expression = 182
    RULE_csharp_selector_expression = 183
    RULE_csharp_method_expression = 184
    RULE_csharp_arguments = 185
    RULE_csharp_item_expression = 186
    RULE_csharp_parenthesis_expression = 187
    RULE_csharp_identifier_expression = 188
    RULE_csharp_literal_expression = 189
    RULE_csharp_identifier = 190

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"category_symbol", u"native_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"category_method_list", u"operator_method_declaration", 
                   u"setter_method_declaration", u"getter_method_declaration", 
                   u"native_resource_declaration", u"native_category_declaration", 
                   u"native_category_bindings", u"native_category_binding_list", 
                   u"attribute_list", u"abstract_method_declaration", u"concrete_method_declaration", 
                   u"native_method_declaration", u"test_method_declaration", 
                   u"assertion", u"typed_argument", u"statement_or_list", 
                   u"statement", u"store_statement", u"with_resource_statement", 
                   u"with_singleton_statement", u"switch_statement", u"switch_case_statement", 
                   u"for_each_statement", u"do_while_statement", u"while_statement", 
                   u"if_statement", u"else_if_statement_list", u"raise_statement", 
                   u"try_statement", u"catch_statement", u"return_statement", 
                   u"method_call", u"method_selector", u"callable_parent", 
                   u"callable_selector", u"expression", u"an_expression", 
                   u"closure_expression", u"instance_expression", u"method_expression", 
                   u"document_expression", u"read_expression", u"write_statement", 
                   u"fetch_expression", u"sorted_expression", u"selector_expression", 
                   u"constructor_expression", u"argument_assignment_list", 
                   u"argument_assignment", u"assign_instance_statement", 
                   u"child_instance", u"assign_tuple_statement", u"null_literal", 
                   u"declaration_list", u"declarations", u"declaration", 
                   u"resource_declaration", u"enum_declaration", u"native_symbol_list", 
                   u"category_symbol_list", u"symbol_list", u"attribute_constraint", 
                   u"list_literal", u"set_literal", u"expression_list", 
                   u"range_literal", u"typedef", u"primary_type", u"native_type", 
                   u"category_type", u"code_type", u"document_type", u"category_declaration", 
                   u"type_identifier_list", u"method_identifier", u"identifier", 
                   u"variable_identifier", u"type_identifier", u"symbol_identifier", 
                   u"argument_list", u"argument", u"operator_argument", 
                   u"named_argument", u"code_argument", u"category_or_any_type", 
                   u"any_type", u"member_method_declaration_list", u"member_method_declaration", 
                   u"native_member_method_declaration_list", u"native_member_method_declaration", 
                   u"native_category_binding", u"python_category_binding", 
                   u"python_module", u"module_token", u"javascript_category_binding", 
                   u"javascript_module", u"variable_identifier_list", u"method_declaration", 
                   u"native_statement_list", u"native_statement", u"python_native_statement", 
                   u"javascript_native_statement", u"statement_list", u"assertion_list", 
                   u"switch_case_statement_list", u"catch_statement_list", 
                   u"literal_collection", u"atomic_literal", u"literal_list_literal", 
                   u"selectable_expression", u"this_expression", u"parenthesis_expression", 
                   u"literal_expression", u"collection_literal", u"tuple_literal", 
                   u"dict_literal", u"expression_tuple", u"dict_entry_list", 
                   u"dict_entry", u"slice_arguments", u"assign_variable_statement", 
                   u"assignable_instance", u"is_expression", u"operator", 
                   u"key_token", u"value_token", u"symbols_token", u"assign", 
                   u"multiply", u"divide", u"idivide", u"modulo", u"lfs", 
                   u"lfp", u"javascript_statement", u"javascript_expression", 
                   u"javascript_primary_expression", u"javascript_this_expression", 
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
                   u"java_selector_expression", u"java_method_expression", 
                   u"java_arguments", u"java_item_expression", u"java_parenthesis_expression", 
                   u"java_identifier_expression", u"java_class_identifier_expression", 
                   u"java_literal_expression", u"java_identifier", u"csharp_statement", 
                   u"csharp_expression", u"csharp_primary_expression", u"csharp_this_expression", 
                   u"csharp_selector_expression", u"csharp_method_expression", 
                   u"csharp_arguments", u"csharp_item_expression", u"csharp_parenthesis_expression", 
                   u"csharp_identifier_expression", u"csharp_literal_expression", 
                   u"csharp_identifier" ]

    EOF = Token.EOF
    SPACE=1
    WS=2
    LF=3
    JAVA=4
    CSHARP=5
    PYTHON2=6
    PYTHON3=7
    JAVASCRIPT=8
    SWIFT=9
    COLON=10
    SEMI=11
    COMMA=12
    RANGE=13
    DOT=14
    LPAR=15
    RPAR=16
    LBRAK=17
    RBRAK=18
    LCURL=19
    RCURL=20
    QMARK=21
    XMARK=22
    AMP=23
    AMP2=24
    PIPE=25
    PIPE2=26
    PLUS=27
    MINUS=28
    STAR=29
    SLASH=30
    BSLASH=31
    PERCENT=32
    GT=33
    GTE=34
    LT=35
    LTE=36
    LTGT=37
    EQ=38
    XEQ=39
    EQ2=40
    TEQ=41
    TILDE=42
    LARROW=43
    RARROW=44
    BOOLEAN=45
    CHARACTER=46
    TEXT=47
    INTEGER=48
    DECIMAL=49
    DATE=50
    TIME=51
    DATETIME=52
    PERIOD=53
    METHOD_T=54
    CODE=55
    DOCUMENT=56
    ABSTRACT=57
    ALL=58
    ALWAYS=59
    AND=60
    ANY=61
    AS=62
    ATTR=63
    ATTRIBUTE=64
    ATTRIBUTES=65
    BINDINGS=66
    CASE=67
    CATCH=68
    CATEGORY=69
    CLASS=70
    CLOSE=71
    CONTAINS=72
    DEF=73
    DEFAULT=74
    DEFINE=75
    DO=76
    DOING=77
    EACH=78
    ELSE=79
    ENUM=80
    ENUMERATED=81
    EXCEPT=82
    EXECUTE=83
    EXPECTING=84
    EXTENDS=85
    FETCH=86
    FINALLY=87
    FOR=88
    FROM=89
    GETTER=90
    IF=91
    IN=92
    INVOKE=93
    IS=94
    MATCHING=95
    METHOD=96
    METHODS=97
    MODULO=98
    MUTABLE=99
    NATIVE=100
    NONE=101
    NOT=102
    NOTHING=103
    NULL=104
    ON=105
    ONE=106
    OPEN=107
    OPERATOR=108
    OR=109
    OTHERWISE=110
    PASS=111
    RAISE=112
    READ=113
    RECEIVING=114
    RESOURCE=115
    RETURN=116
    RETURNING=117
    ROWS=118
    SELF=119
    SETTER=120
    SINGLETON=121
    SORTED=122
    STORABLE=123
    STORE=124
    SWITCH=125
    TEST=126
    THIS=127
    THROW=128
    TO=129
    TRY=130
    WITH=131
    WHEN=132
    WHERE=133
    WHILE=134
    WRITE=135
    BOOLEAN_LITERAL=136
    CHAR_LITERAL=137
    MIN_INTEGER=138
    MAX_INTEGER=139
    SYMBOL_IDENTIFIER=140
    TYPE_IDENTIFIER=141
    VARIABLE_IDENTIFIER=142
    NATIVE_IDENTIFIER=143
    DOLLAR_IDENTIFIER=144
    TEXT_LITERAL=145
    INTEGER_LITERAL=146
    HEXA_LITERAL=147
    DECIMAL_LITERAL=148
    DATETIME_LITERAL=149
    TIME_LITERAL=150
    DATE_LITERAL=151
    PERIOD_LITERAL=152
    COMMENT=153

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
            self.attrs = None # Attribute_listContext
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

        def attribute_list(self):
            return self.getTypedRuleContext(OParser.Attribute_listContext,0)


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
            self.state = 382
            self.match(OParser.ENUMERATED)
            self.state = 383
            self.match(OParser.CATEGORY)
            self.state = 384 
            localctx.name = self.type_identifier()
            self.state = 389
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 385
                self.match(OParser.LPAR)
                self.state = 386 
                localctx.attrs = self.attribute_list(0)
                self.state = 387
                self.match(OParser.RPAR)


            self.state = 393
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 391
                self.match(OParser.EXTENDS)
                self.state = 392 
                localctx.derived = self.type_identifier()


            self.state = 395
            self.match(OParser.LCURL)
            self.state = 396 
            localctx.symbols = self.category_symbol_list(0)
            self.state = 397
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
            self.state = 399
            self.match(OParser.ENUMERATED)
            self.state = 400 
            localctx.name = self.type_identifier()
            self.state = 401
            self.match(OParser.LPAR)
            self.state = 402 
            localctx.typ = self.native_type()
            self.state = 403
            self.match(OParser.RPAR)
            self.state = 404
            self.match(OParser.LCURL)
            self.state = 405 
            localctx.symbols = self.native_symbol_list(0)
            self.state = 406
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
            self.state = 408 
            localctx.name = self.symbol_identifier()
            self.state = 409
            self.match(OParser.LPAR)
            self.state = 410 
            localctx.args = self.argument_assignment_list(0)
            self.state = 411
            self.match(OParser.RPAR)
            self.state = 412
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
            self.state = 414 
            localctx.name = self.symbol_identifier()
            self.state = 415
            self.match(OParser.EQ)
            self.state = 416 
            localctx.exp = self.expression(0)
            self.state = 417
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
            self.name = None # Variable_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext

        def ATTRIBUTE(self):
            return self.getToken(OParser.ATTRIBUTE, 0)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(OParser.Attribute_constraintContext,0)


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
            self.state = 420
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 419
                self.match(OParser.STORABLE)


            self.state = 422
            self.match(OParser.ATTRIBUTE)
            self.state = 423 
            localctx.name = self.variable_identifier()
            self.state = 424
            self.match(OParser.COLON)
            self.state = 425 
            localctx.typ = self.typedef(0)
            self.state = 427
            _la = self._input.LA(1)
            if _la==OParser.IN or _la==OParser.MATCHING:
                self.state = 426 
                localctx.match = self.attribute_constraint()


            self.state = 429
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
            self.attrs = None # Attribute_listContext
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

        def attribute_list(self):
            return self.getTypedRuleContext(OParser.Attribute_listContext,0)


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
            self.state = 432
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 431
                self.match(OParser.STORABLE)


            self.state = 434
            self.match(OParser.CATEGORY)
            self.state = 435 
            localctx.name = self.type_identifier()
            self.state = 440
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 436
                self.match(OParser.LPAR)
                self.state = 437 
                localctx.attrs = self.attribute_list(0)
                self.state = 438
                self.match(OParser.RPAR)


            self.state = 444
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 442
                self.match(OParser.EXTENDS)
                self.state = 443 
                localctx.derived = self.derived_list(0)


            self.state = 446 
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
            self.attrs = None # Attribute_listContext
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

        def attribute_list(self):
            return self.getTypedRuleContext(OParser.Attribute_listContext,0)


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
            self.state = 448
            self.match(OParser.SINGLETON)
            self.state = 449 
            localctx.name = self.type_identifier()
            self.state = 454
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 450
                self.match(OParser.LPAR)
                self.state = 451 
                localctx.attrs = self.attribute_list(0)
                self.state = 452
                self.match(OParser.RPAR)


            self.state = 456 
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

            self.state = 459 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.DerivedListItemContext(self, OParser.Derived_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_derived_list)
                    self.state = 461
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 462
                    self.match(OParser.COMMA)
                    self.state = 463 
                    localctx.item = self.type_identifier() 
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 475
            token = self._input.LA(1)
            if token in [OParser.SEMI]:
                localctx = OParser.EmptyCategoryMethodListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.match(OParser.SEMI)

            elif token in [OParser.LCURL]:
                localctx = OParser.CurlyCategoryMethodListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(OParser.LCURL)
                self.state = 472
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.ABSTRACT))) != 0) or ((((_la - 90)) & ~0x3f) == 0 and ((1 << (_la - 90)) & ((1 << (OParser.GETTER - 90)) | (1 << (OParser.METHOD - 90)) | (1 << (OParser.OPERATOR - 90)) | (1 << (OParser.SETTER - 90)) | (1 << (OParser.TYPE_IDENTIFIER - 90)))) != 0):
                    self.state = 471 
                    localctx.items = self.member_method_declaration_list(0)


                self.state = 474
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
            self.state = 478
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 477 
                localctx.typ = self.typedef(0)


            self.state = 480
            self.match(OParser.OPERATOR)
            self.state = 481 
            localctx.op = self.operator()
            self.state = 482
            self.match(OParser.LPAR)
            self.state = 483 
            localctx.arg = self.operator_argument()
            self.state = 484
            self.match(OParser.RPAR)
            self.state = 485
            self.match(OParser.LCURL)
            self.state = 487
            _la = self._input.LA(1)
            if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                self.state = 486 
                localctx.stmts = self.statement_list(0)


            self.state = 489
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
            self.state = 491
            self.match(OParser.SETTER)
            self.state = 492 
            localctx.name = self.variable_identifier()
            self.state = 493
            self.match(OParser.LCURL)
            self.state = 495
            _la = self._input.LA(1)
            if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                self.state = 494 
                localctx.stmts = self.statement_list(0)


            self.state = 497
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
        self.enterRule(localctx, 22, self.RULE_getter_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(OParser.GETTER)
            self.state = 500 
            localctx.name = self.variable_identifier()
            self.state = 501
            self.match(OParser.LCURL)
            self.state = 503
            _la = self._input.LA(1)
            if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                self.state = 502 
                localctx.stmts = self.statement_list(0)


            self.state = 505
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
            self.attrs = None # Attribute_listContext
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

        def attribute_list(self):
            return self.getTypedRuleContext(OParser.Attribute_listContext,0)


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
        self.enterRule(localctx, 24, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(OParser.NATIVE)
            self.state = 508
            self.match(OParser.RESOURCE)
            self.state = 509 
            localctx.name = self.type_identifier()
            self.state = 514
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 510
                self.match(OParser.LPAR)
                self.state = 511 
                localctx.attrs = self.attribute_list(0)
                self.state = 512
                self.match(OParser.RPAR)


            self.state = 516
            self.match(OParser.LCURL)
            self.state = 517 
            localctx.bindings = self.native_category_bindings()
            self.state = 519
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.ABSTRACT) | (1 << OParser.ANY))) != 0) or ((((_la - 90)) & ~0x3f) == 0 and ((1 << (_la - 90)) & ((1 << (OParser.GETTER - 90)) | (1 << (OParser.METHOD - 90)) | (1 << (OParser.NATIVE - 90)) | (1 << (OParser.OPERATOR - 90)) | (1 << (OParser.SETTER - 90)) | (1 << (OParser.TYPE_IDENTIFIER - 90)))) != 0):
                self.state = 518 
                localctx.methods = self.native_member_method_declaration_list(0)


            self.state = 521
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
            self.attrs = None # Attribute_listContext
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

        def attribute_list(self):
            return self.getTypedRuleContext(OParser.Attribute_listContext,0)


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
        self.enterRule(localctx, 26, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 523
                self.match(OParser.STORABLE)


            self.state = 526
            self.match(OParser.NATIVE)
            self.state = 527
            self.match(OParser.CATEGORY)
            self.state = 528 
            localctx.name = self.type_identifier()
            self.state = 533
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 529
                self.match(OParser.LPAR)
                self.state = 530 
                localctx.attrs = self.attribute_list(0)
                self.state = 531
                self.match(OParser.RPAR)


            self.state = 535
            self.match(OParser.LCURL)
            self.state = 536 
            localctx.bindings = self.native_category_bindings()
            self.state = 538
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.ABSTRACT) | (1 << OParser.ANY))) != 0) or ((((_la - 90)) & ~0x3f) == 0 and ((1 << (_la - 90)) & ((1 << (OParser.GETTER - 90)) | (1 << (OParser.METHOD - 90)) | (1 << (OParser.NATIVE - 90)) | (1 << (OParser.OPERATOR - 90)) | (1 << (OParser.SETTER - 90)) | (1 << (OParser.TYPE_IDENTIFIER - 90)))) != 0):
                self.state = 537 
                localctx.methods = self.native_member_method_declaration_list(0)


            self.state = 540
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
        self.enterRule(localctx, 28, self.RULE_native_category_bindings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(OParser.CATEGORY)
            self.state = 543
            self.match(OParser.BINDINGS)
            self.state = 544
            self.match(OParser.LCURL)
            self.state = 545 
            localctx.items = self.native_category_binding_list(0)
            self.state = 546
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 549 
            localctx.item = self.native_category_binding()
            self.state = 550
            self.match(OParser.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 558
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.NativeCategoryBindingListItemContext(self, OParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 552
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 553 
                    localctx.item = self.native_category_binding()
                    self.state = 554
                    self.match(OParser.SEMI) 
                self.state = 560
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Attribute_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_attribute_list

     
        def copyFrom(self, ctx):
            super(OParser.Attribute_listContext, self).copyFrom(ctx)


    class AttributeListContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_listContext)
            super(OParser.AttributeListContext, self).__init__(parser)
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAttributeList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAttributeList(self)


    class AttributeListItemContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_listContext)
            super(OParser.AttributeListItemContext, self).__init__(parser)
            self.items = None # Attribute_listContext
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def attribute_list(self):
            return self.getTypedRuleContext(OParser.Attribute_listContext,0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAttributeListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAttributeListItem(self)



    def attribute_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Attribute_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_attribute_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.AttributeListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 562 
            localctx.item = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 569
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.AttributeListItemContext(self, OParser.Attribute_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_attribute_list)
                    self.state = 564
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 565
                    self.match(OParser.COMMA)
                    self.state = 566 
                    localctx.item = self.variable_identifier() 
                self.state = 571
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
        self.enterRule(localctx, 34, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(OParser.ABSTRACT)
            self.state = 574
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 573 
                localctx.typ = self.typedef(0)


            self.state = 576
            self.match(OParser.METHOD)
            self.state = 577 
            localctx.name = self.method_identifier()
            self.state = 578
            self.match(OParser.LPAR)
            self.state = 580
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.ANY))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (OParser.MUTABLE - 99)) | (1 << (OParser.TYPE_IDENTIFIER - 99)) | (1 << (OParser.VARIABLE_IDENTIFIER - 99)))) != 0):
                self.state = 579 
                localctx.args = self.argument_list(0)


            self.state = 582
            self.match(OParser.RPAR)
            self.state = 583
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
        self.enterRule(localctx, 36, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 585 
                localctx.typ = self.typedef(0)


            self.state = 588
            self.match(OParser.METHOD)
            self.state = 589 
            localctx.name = self.method_identifier()
            self.state = 590
            self.match(OParser.LPAR)
            self.state = 592
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.ANY))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (OParser.MUTABLE - 99)) | (1 << (OParser.TYPE_IDENTIFIER - 99)) | (1 << (OParser.VARIABLE_IDENTIFIER - 99)))) != 0):
                self.state = 591 
                localctx.args = self.argument_list(0)


            self.state = 594
            self.match(OParser.RPAR)
            self.state = 595
            self.match(OParser.LCURL)
            self.state = 597
            _la = self._input.LA(1)
            if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                self.state = 596 
                localctx.stmts = self.statement_list(0)


            self.state = 599
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

        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

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
        self.enterRule(localctx, 38, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.ANY))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 601 
                localctx.typ = self.category_or_any_type()


            self.state = 604
            self.match(OParser.NATIVE)
            self.state = 605
            self.match(OParser.METHOD)
            self.state = 606 
            localctx.name = self.method_identifier()
            self.state = 607
            self.match(OParser.LPAR)
            self.state = 609
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.CODE) | (1 << OParser.ANY))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (OParser.MUTABLE - 99)) | (1 << (OParser.TYPE_IDENTIFIER - 99)) | (1 << (OParser.VARIABLE_IDENTIFIER - 99)))) != 0):
                self.state = 608 
                localctx.args = self.argument_list(0)


            self.state = 611
            self.match(OParser.RPAR)
            self.state = 612
            self.match(OParser.LCURL)
            self.state = 613 
            localctx.stmts = self.native_statement_list(0)
            self.state = 614
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

        def EXPECTING(self):
            return self.getToken(OParser.EXPECTING, 0)

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
        self.enterRule(localctx, 40, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self.match(OParser.TEST)
            self.state = 617
            self.match(OParser.METHOD)
            self.state = 618
            localctx.name = self.match(OParser.TEXT_LITERAL)
            self.state = 619
            self.match(OParser.LPAR)
            self.state = 620
            self.match(OParser.RPAR)
            self.state = 621
            self.match(OParser.LCURL)
            self.state = 622 
            localctx.stmts = self.statement_list(0)
            self.state = 623
            self.match(OParser.RCURL)
            self.state = 624
            self.match(OParser.EXPECTING)
            self.state = 632
            token = self._input.LA(1)
            if token in [OParser.LCURL]:
                self.state = 625
                self.match(OParser.LCURL)
                self.state = 626 
                localctx.exps = self.assertion_list(0)
                self.state = 627
                self.match(OParser.RCURL)

            elif token in [OParser.SYMBOL_IDENTIFIER]:
                self.state = 629 
                localctx.error = self.symbol_identifier()
                self.state = 630
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
        self.enterRule(localctx, 42, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634 
            localctx.exp = self.expression(0)
            self.state = 635
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
            self.attrs = None # Attribute_listContext
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

        def attribute_list(self):
            return self.getTypedRuleContext(OParser.Attribute_listContext,0)


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
        self.enterRule(localctx, 44, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637 
            localctx.typ = self.category_or_any_type()
            self.state = 642
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 638
                self.match(OParser.LPAR)
                self.state = 639 
                localctx.attrs = self.attribute_list(0)
                self.state = 640
                self.match(OParser.RPAR)


            self.state = 644 
            localctx.name = self.variable_identifier()
            self.state = 647
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 645
                self.match(OParser.EQ)
                self.state = 646 
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
        self.enterRule(localctx, 46, self.RULE_statement_or_list)
        try:
            self.state = 656
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.CODE, OParser.DO, OParser.FOR, OParser.IF, OParser.METHOD, OParser.RETURN, OParser.STORE, OParser.SWITCH, OParser.THROW, OParser.TRY, OParser.WITH, OParser.WHILE, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.SingleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 649 
                localctx.stmt = self.statement()

            elif token in [OParser.LCURL]:
                localctx = OParser.CurlyStatementListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 650
                self.match(OParser.LCURL)
                self.state = 654
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 651 
                    localctx.items = self.statement_list(0)
                    self.state = 652
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
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.state = 676
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                localctx = OParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 658 
                localctx.stmt = self.method_call()
                self.state = 659
                self.match(OParser.SEMI)
                pass

            elif la_ == 2:
                localctx = OParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 661 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = OParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 662 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = OParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 663 
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = OParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 664 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 6:
                localctx = OParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 665 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 7:
                localctx = OParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 666 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 8:
                localctx = OParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 667 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 9:
                localctx = OParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 668 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 10:
                localctx = OParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 669 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 11:
                localctx = OParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 670 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 12:
                localctx = OParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 671 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 13:
                localctx = OParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 672 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 14:
                localctx = OParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 673 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 15:
                localctx = OParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 674 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 16:
                localctx = OParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 675 
                localctx.decl = self.concrete_method_declaration()
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
            super(OParser.Store_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exps = None # Expression_listContext

        def STORE(self):
            return self.getToken(OParser.STORE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression_list(self):
            return self.getTypedRuleContext(OParser.Expression_listContext,0)


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
        self.enterRule(localctx, 50, self.RULE_store_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
            self.match(OParser.STORE)
            self.state = 679
            self.match(OParser.LPAR)
            self.state = 680 
            localctx.exps = self.expression_list(0)
            self.state = 681
            self.match(OParser.RPAR)
            self.state = 682
            self.match(OParser.SEMI)
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
        self.enterRule(localctx, 52, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.match(OParser.WITH)
            self.state = 685
            self.match(OParser.LPAR)
            self.state = 686 
            localctx.stmt = self.assign_variable_statement()
            self.state = 687
            self.match(OParser.RPAR)
            self.state = 688 
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
        self.enterRule(localctx, 54, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 690
            self.match(OParser.WITH)
            self.state = 691
            self.match(OParser.LPAR)
            self.state = 692 
            localctx.typ = self.type_identifier()
            self.state = 693
            self.match(OParser.RPAR)
            self.state = 694 
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
        self.enterRule(localctx, 56, self.RULE_switch_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 696
            self.match(OParser.SWITCH)
            self.state = 697
            self.match(OParser.LPAR)
            self.state = 698 
            localctx.exp = self.expression(0)
            self.state = 699
            self.match(OParser.RPAR)
            self.state = 700
            self.match(OParser.LCURL)
            self.state = 701 
            localctx.cases = self.switch_case_statement_list(0)
            self.state = 707
            _la = self._input.LA(1)
            if _la==OParser.DEFAULT:
                self.state = 702
                self.match(OParser.DEFAULT)
                self.state = 703
                self.match(OParser.COLON)
                self.state = 705
                _la = self._input.LA(1)
                if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                    self.state = 704 
                    localctx.stmts = self.statement_list(0)




            self.state = 709
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
        self.enterRule(localctx, 58, self.RULE_switch_case_statement)
        try:
            self.state = 724
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                localctx = OParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 711
                self.match(OParser.CASE)
                self.state = 712 
                localctx.exp = self.atomic_literal()
                self.state = 713
                self.match(OParser.COLON)
                self.state = 715
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 714 
                    localctx.stmts = self.statement_list(0)


                pass

            elif la_ == 2:
                localctx = OParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 717
                self.match(OParser.CASE)
                self.state = 718
                self.match(OParser.IN)
                self.state = 719 
                localctx.exp = self.literal_collection()
                self.state = 720
                self.match(OParser.COLON)
                self.state = 722
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 721 
                    localctx.stmts = self.statement_list(0)


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
        self.enterRule(localctx, 60, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 726
            self.match(OParser.FOR)
            self.state = 727
            self.match(OParser.EACH)
            self.state = 728
            self.match(OParser.LPAR)
            self.state = 729 
            localctx.name1 = self.variable_identifier()
            self.state = 732
            _la = self._input.LA(1)
            if _la==OParser.COMMA:
                self.state = 730
                self.match(OParser.COMMA)
                self.state = 731 
                localctx.name2 = self.variable_identifier()


            self.state = 734
            self.match(OParser.IN)
            self.state = 735 
            localctx.source = self.expression(0)
            self.state = 736
            self.match(OParser.RPAR)
            self.state = 737 
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
        self.enterRule(localctx, 62, self.RULE_do_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
            self.match(OParser.DO)
            self.state = 740
            self.match(OParser.LCURL)
            self.state = 742
            _la = self._input.LA(1)
            if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                self.state = 741 
                localctx.stmts = self.statement_list(0)


            self.state = 744
            self.match(OParser.RCURL)
            self.state = 745
            self.match(OParser.WHILE)
            self.state = 746
            self.match(OParser.LPAR)
            self.state = 747 
            localctx.exp = self.expression(0)
            self.state = 748
            self.match(OParser.RPAR)
            self.state = 749
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
        self.enterRule(localctx, 64, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 751
            self.match(OParser.WHILE)
            self.state = 752
            self.match(OParser.LPAR)
            self.state = 753 
            localctx.exp = self.expression(0)
            self.state = 754
            self.match(OParser.RPAR)
            self.state = 755 
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
        self.enterRule(localctx, 66, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 757
            self.match(OParser.IF)
            self.state = 758
            self.match(OParser.LPAR)
            self.state = 759 
            localctx.exp = self.expression(0)
            self.state = 760
            self.match(OParser.RPAR)
            self.state = 761 
            localctx.stmts = self.statement_or_list()
            self.state = 763
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 762 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 767
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 765
                self.match(OParser.ELSE)
                self.state = 766 
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 770
            self.match(OParser.ELSE)
            self.state = 771
            self.match(OParser.IF)
            self.state = 772
            self.match(OParser.LPAR)
            self.state = 773 
            localctx.exp = self.expression(0)
            self.state = 774
            self.match(OParser.RPAR)
            self.state = 775 
            localctx.stmts = self.statement_or_list()
            self._ctx.stop = self._input.LT(-1)
            self.state = 787
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ElseIfStatementListItemContext(self, OParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 777
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 778
                    self.match(OParser.ELSE)
                    self.state = 779
                    self.match(OParser.IF)
                    self.state = 780
                    self.match(OParser.LPAR)
                    self.state = 781 
                    localctx.exp = self.expression(0)
                    self.state = 782
                    self.match(OParser.RPAR)
                    self.state = 783 
                    localctx.stmts = self.statement_or_list() 
                self.state = 789
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 790
            self.match(OParser.THROW)
            self.state = 791 
            localctx.exp = self.expression(0)
            self.state = 792
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
        self.enterRule(localctx, 72, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 794
            self.match(OParser.TRY)
            self.state = 795
            self.match(OParser.LPAR)
            self.state = 796 
            localctx.name = self.variable_identifier()
            self.state = 797
            self.match(OParser.RPAR)
            self.state = 798
            self.match(OParser.LCURL)
            self.state = 800
            _la = self._input.LA(1)
            if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                self.state = 799 
                localctx.stmts = self.statement_list(0)


            self.state = 802
            self.match(OParser.RCURL)
            self.state = 804
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 803 
                localctx.handlers = self.catch_statement_list(0)


            self.state = 815
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 806
                self.match(OParser.CATCH)
                self.state = 807
                self.match(OParser.LPAR)
                self.state = 808
                self.match(OParser.ANY)
                self.state = 809
                self.match(OParser.RPAR)
                self.state = 810
                self.match(OParser.LCURL)
                self.state = 812
                _la = self._input.LA(1)
                if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                    self.state = 811 
                    localctx.anyStmts = self.statement_list(0)


                self.state = 814
                self.match(OParser.RCURL)


            self.state = 823
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 817
                self.match(OParser.FINALLY)
                self.state = 818
                self.match(OParser.LCURL)
                self.state = 820
                _la = self._input.LA(1)
                if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                    self.state = 819 
                    localctx.finalStmts = self.statement_list(0)


                self.state = 822
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
        self.enterRule(localctx, 74, self.RULE_catch_statement)
        self._la = 0 # Token type
        try:
            self.state = 846
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                localctx = OParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 825
                self.match(OParser.CATCH)
                self.state = 826
                self.match(OParser.LPAR)
                self.state = 827 
                localctx.name = self.symbol_identifier()
                self.state = 828
                self.match(OParser.RPAR)
                self.state = 829
                self.match(OParser.LCURL)
                self.state = 831
                _la = self._input.LA(1)
                if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                    self.state = 830 
                    localctx.stmts = self.statement_list(0)


                self.state = 833
                self.match(OParser.RCURL)
                pass

            elif la_ == 2:
                localctx = OParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 835
                self.match(OParser.CATCH)
                self.state = 836
                self.match(OParser.IN)
                self.state = 837
                self.match(OParser.LPAR)
                self.state = 838 
                localctx.exp = self.symbol_list(0)
                self.state = 839
                self.match(OParser.RPAR)
                self.state = 840
                self.match(OParser.LCURL)
                self.state = 842
                _la = self._input.LA(1)
                if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.DO - 45)) | (1 << (OParser.FOR - 45)) | (1 << (OParser.IF - 45)) | (1 << (OParser.METHOD - 45)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.RETURN - 116)) | (1 << (OParser.STORE - 116)) | (1 << (OParser.SWITCH - 116)) | (1 << (OParser.THROW - 116)) | (1 << (OParser.TRY - 116)) | (1 << (OParser.WITH - 116)) | (1 << (OParser.WHILE - 116)) | (1 << (OParser.WRITE - 116)) | (1 << (OParser.SYMBOL_IDENTIFIER - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                    self.state = 841 
                    localctx.stmts = self.statement_list(0)


                self.state = 844
                self.match(OParser.RCURL)
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
        self.enterRule(localctx, 76, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 848
            self.match(OParser.RETURN)
            self.state = 850
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT))) != 0) or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (OParser.EXECUTE - 83)) | (1 << (OParser.FETCH - 83)) | (1 << (OParser.MUTABLE - 83)) | (1 << (OParser.NULL - 83)) | (1 << (OParser.READ - 83)) | (1 << (OParser.SELF - 83)) | (1 << (OParser.SORTED - 83)) | (1 << (OParser.THIS - 83)) | (1 << (OParser.BOOLEAN_LITERAL - 83)) | (1 << (OParser.CHAR_LITERAL - 83)) | (1 << (OParser.MIN_INTEGER - 83)) | (1 << (OParser.MAX_INTEGER - 83)) | (1 << (OParser.SYMBOL_IDENTIFIER - 83)) | (1 << (OParser.TYPE_IDENTIFIER - 83)) | (1 << (OParser.VARIABLE_IDENTIFIER - 83)) | (1 << (OParser.TEXT_LITERAL - 83)) | (1 << (OParser.INTEGER_LITERAL - 83)))) != 0) or ((((_la - 147)) & ~0x3f) == 0 and ((1 << (_la - 147)) & ((1 << (OParser.HEXA_LITERAL - 147)) | (1 << (OParser.DECIMAL_LITERAL - 147)) | (1 << (OParser.DATETIME_LITERAL - 147)) | (1 << (OParser.TIME_LITERAL - 147)) | (1 << (OParser.DATE_LITERAL - 147)) | (1 << (OParser.PERIOD_LITERAL - 147)))) != 0):
                self.state = 849 
                localctx.exp = self.expression(0)


            self.state = 852
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
        self.enterRule(localctx, 78, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 854 
            localctx.method = self.method_selector()
            self.state = 855
            self.match(OParser.LPAR)
            self.state = 857
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT))) != 0) or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (OParser.EXECUTE - 83)) | (1 << (OParser.FETCH - 83)) | (1 << (OParser.MUTABLE - 83)) | (1 << (OParser.NULL - 83)) | (1 << (OParser.READ - 83)) | (1 << (OParser.SELF - 83)) | (1 << (OParser.SORTED - 83)) | (1 << (OParser.THIS - 83)) | (1 << (OParser.BOOLEAN_LITERAL - 83)) | (1 << (OParser.CHAR_LITERAL - 83)) | (1 << (OParser.MIN_INTEGER - 83)) | (1 << (OParser.MAX_INTEGER - 83)) | (1 << (OParser.SYMBOL_IDENTIFIER - 83)) | (1 << (OParser.TYPE_IDENTIFIER - 83)) | (1 << (OParser.VARIABLE_IDENTIFIER - 83)) | (1 << (OParser.TEXT_LITERAL - 83)) | (1 << (OParser.INTEGER_LITERAL - 83)))) != 0) or ((((_la - 147)) & ~0x3f) == 0 and ((1 << (_la - 147)) & ((1 << (OParser.HEXA_LITERAL - 147)) | (1 << (OParser.DECIMAL_LITERAL - 147)) | (1 << (OParser.DATETIME_LITERAL - 147)) | (1 << (OParser.TIME_LITERAL - 147)) | (1 << (OParser.DATE_LITERAL - 147)) | (1 << (OParser.PERIOD_LITERAL - 147)))) != 0):
                self.state = 856 
                localctx.args = self.argument_assignment_list(0)


            self.state = 859
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
        self.enterRule(localctx, 80, self.RULE_method_selector)
        try:
            self.state = 866
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                localctx = OParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 861 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = OParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 862 
                localctx.parent = self.callable_parent(0)
                self.state = 863
                self.match(OParser.DOT)
                self.state = 864 
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 869 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 875
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CallableSelectorContext(self, OParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 871
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 872 
                    localctx.select = self.callable_selector() 
                self.state = 877
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_callable_selector)
        try:
            self.state = 884
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 878
                self.match(OParser.DOT)
                self.state = 879 
                localctx.name = self.variable_identifier()

            elif token in [OParser.LBRAK]:
                localctx = OParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 880
                self.match(OParser.LBRAK)
                self.state = 881 
                localctx.exp = self.expression(0)
                self.state = 882
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 909
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                localctx = OParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 887
                self.match(OParser.MINUS)
                self.state = 888 
                localctx.exp = self.expression(33)
                pass

            elif la_ == 2:
                localctx = OParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 889
                self.match(OParser.XMARK)
                self.state = 890 
                localctx.exp = self.expression(32)
                pass

            elif la_ == 3:
                localctx = OParser.CastExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 891
                self.match(OParser.LPAR)
                self.state = 892 
                localctx.right = self.category_or_any_type()
                self.state = 893
                self.match(OParser.RPAR)
                self.state = 894 
                localctx.left = self.expression(12)
                pass

            elif la_ == 4:
                localctx = OParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 896 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 5:
                localctx = OParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 897 
                localctx.exp = self.method_expression()
                pass

            elif la_ == 6:
                localctx = OParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 898
                self.match(OParser.CODE)
                self.state = 899
                self.match(OParser.LPAR)
                self.state = 900 
                localctx.exp = self.expression(0)
                self.state = 901
                self.match(OParser.RPAR)
                pass

            elif la_ == 7:
                localctx = OParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 903
                self.match(OParser.EXECUTE)
                self.state = 904
                self.match(OParser.LPAR)
                self.state = 905 
                localctx.name = self.variable_identifier()
                self.state = 906
                self.match(OParser.RPAR)
                pass

            elif la_ == 8:
                localctx = OParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 908 
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1011
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1009
                    la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                    if la_ == 1:
                        localctx = OParser.MultiplyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 911
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 912 
                        self.multiply()
                        self.state = 913 
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 2:
                        localctx = OParser.DivideExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 915
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 916 
                        self.divide()
                        self.state = 917 
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 3:
                        localctx = OParser.ModuloExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 919
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 920 
                        self.modulo()
                        self.state = 921 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 4:
                        localctx = OParser.IntDivideExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 923
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 924 
                        self.idivide()
                        self.state = 925 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 5:
                        localctx = OParser.AddExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 927
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 928
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==OParser.PLUS or _la==OParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 929 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 6:
                        localctx = OParser.LessThanExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 930
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 931
                        self.match(OParser.LT)
                        self.state = 932 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 7:
                        localctx = OParser.LessThanOrEqualExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 933
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 934
                        self.match(OParser.LTE)
                        self.state = 935 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 8:
                        localctx = OParser.GreaterThanExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 936
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 937
                        self.match(OParser.GT)
                        self.state = 938 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 9:
                        localctx = OParser.GreaterThanOrEqualExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 939
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 940
                        self.match(OParser.GTE)
                        self.state = 941 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 10:
                        localctx = OParser.IsNotExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 942
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 943
                        self.match(OParser.IS)
                        self.state = 944
                        self.match(OParser.NOT)
                        self.state = 945 
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 11:
                        localctx = OParser.IsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 946
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 947
                        self.match(OParser.IS)
                        self.state = 948 
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 12:
                        localctx = OParser.EqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 949
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 950
                        self.match(OParser.EQ2)
                        self.state = 951 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 13:
                        localctx = OParser.NotEqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 952
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 953
                        self.match(OParser.XEQ)
                        self.state = 954 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 14:
                        localctx = OParser.RoughlyEqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 955
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 956
                        self.match(OParser.TEQ)
                        self.state = 957 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 15:
                        localctx = OParser.OrExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 958
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 959
                        self.match(OParser.PIPE2)
                        self.state = 960 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 16:
                        localctx = OParser.AndExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 961
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 962
                        self.match(OParser.AMP2)
                        self.state = 963 
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 17:
                        localctx = OParser.TernaryExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.test = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 964
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 965
                        self.match(OParser.QMARK)
                        self.state = 966 
                        localctx.ifTrue = self.expression(0)
                        self.state = 967
                        self.match(OParser.COLON)
                        self.state = 968 
                        localctx.ifFalse = self.expression(14)
                        pass

                    elif la_ == 18:
                        localctx = OParser.InExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 970
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 971
                        self.match(OParser.IN)
                        self.state = 972 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 19:
                        localctx = OParser.ContainsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 973
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 974
                        self.match(OParser.CONTAINS)
                        self.state = 975 
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 20:
                        localctx = OParser.ContainsAllExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 976
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 977
                        self.match(OParser.CONTAINS)
                        self.state = 978
                        self.match(OParser.ALL)
                        self.state = 979 
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 21:
                        localctx = OParser.ContainsAnyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 980
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 981
                        self.match(OParser.CONTAINS)
                        self.state = 982
                        self.match(OParser.ANY)
                        self.state = 983 
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 22:
                        localctx = OParser.NotInExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 984
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 985
                        self.match(OParser.NOT)
                        self.state = 986
                        self.match(OParser.IN)
                        self.state = 987 
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 23:
                        localctx = OParser.NotContainsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 988
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 989
                        self.match(OParser.NOT)
                        self.state = 990
                        self.match(OParser.CONTAINS)
                        self.state = 991 
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 24:
                        localctx = OParser.NotContainsAllExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 992
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 993
                        self.match(OParser.NOT)
                        self.state = 994
                        self.match(OParser.CONTAINS)
                        self.state = 995
                        self.match(OParser.ALL)
                        self.state = 996 
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 25:
                        localctx = OParser.NotContainsAnyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 997
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 998
                        self.match(OParser.NOT)
                        self.state = 999
                        self.match(OParser.CONTAINS)
                        self.state = 1000
                        self.match(OParser.ANY)
                        self.state = 1001 
                        localctx.right = self.expression(5)
                        pass

                    elif la_ == 26:
                        localctx = OParser.IsNotAnExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1002
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1003
                        self.match(OParser.IS)
                        self.state = 1004
                        self.match(OParser.NOT)
                        self.state = 1005 
                        localctx.right = self.an_expression()
                        pass

                    elif la_ == 27:
                        localctx = OParser.IsAnExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1006
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1007
                        self.match(OParser.IS)
                        self.state = 1008 
                        localctx.right = self.an_expression()
                        pass

             
                self.state = 1013
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

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
        self.enterRule(localctx, 88, self.RULE_an_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1014
            if not self.willBeAOrAn():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willBeAOrAn()")
            self.state = 1015
            self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1016 
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
        self.enterRule(localctx, 90, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1018 
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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1021 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1027
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.SelectorExpressionContext(self, OParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1023
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1024 
                    localctx.selector = self.selector_expression() 
                self.state = 1029
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

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


        def getRuleIndex(self):
            return OParser.RULE_method_expression

     
        def copyFrom(self, ctx):
            super(OParser.Method_expressionContext, self).copyFrom(ctx)



    class ReadExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_expressionContext)
            super(OParser.ReadExpressionContext, self).__init__(parser)
            self.exp = None # Read_expressionContext
            self.copyFrom(ctx)

        def read_expression(self):
            return self.getTypedRuleContext(OParser.Read_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterReadExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitReadExpression(self)


    class MethodCallExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_expressionContext)
            super(OParser.MethodCallExpressionContext, self).__init__(parser)
            self.exp = None # Method_callContext
            self.copyFrom(ctx)

        def method_call(self):
            return self.getTypedRuleContext(OParser.Method_callContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterMethodCallExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethodCallExpression(self)


    class FetchExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_expressionContext)
            super(OParser.FetchExpressionContext, self).__init__(parser)
            self.exp = None # Fetch_expressionContext
            self.copyFrom(ctx)

        def fetch_expression(self):
            return self.getTypedRuleContext(OParser.Fetch_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterFetchExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitFetchExpression(self)


    class ConstructorExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_expressionContext)
            super(OParser.ConstructorExpressionContext, self).__init__(parser)
            self.exp = None # Constructor_expressionContext
            self.copyFrom(ctx)

        def constructor_expression(self):
            return self.getTypedRuleContext(OParser.Constructor_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterConstructorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitConstructorExpression(self)


    class DocumentExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_expressionContext)
            super(OParser.DocumentExpressionContext, self).__init__(parser)
            self.exp = None # Document_expressionContext
            self.copyFrom(ctx)

        def document_expression(self):
            return self.getTypedRuleContext(OParser.Document_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDocumentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDocumentExpression(self)


    class SortedExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_expressionContext)
            super(OParser.SortedExpressionContext, self).__init__(parser)
            self.exp = None # Sorted_expressionContext
            self.copyFrom(ctx)

        def sorted_expression(self):
            return self.getTypedRuleContext(OParser.Sorted_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSortedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSortedExpression(self)



    def method_expression(self):

        localctx = OParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_method_expression)
        try:
            self.state = 1036
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = OParser.DocumentExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1030 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 2:
                localctx = OParser.FetchExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1031 
                localctx.exp = self.fetch_expression()
                pass

            elif la_ == 3:
                localctx = OParser.ReadExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1032 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 4:
                localctx = OParser.SortedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1033 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 5:
                localctx = OParser.MethodCallExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1034 
                localctx.exp = self.method_call()
                pass

            elif la_ == 6:
                localctx = OParser.ConstructorExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1035 
                localctx.exp = self.constructor_expression()
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
            super(OParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def document_type(self):
            return self.getTypedRuleContext(OParser.Document_typeContext,0)


        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

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
        self.enterRule(localctx, 96, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1038 
            self.document_type()
            self.state = 1039
            self.match(OParser.LPAR)
            self.state = 1040
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
        self.enterRule(localctx, 98, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1042
            self.match(OParser.READ)
            self.state = 1043
            self.match(OParser.FROM)
            self.state = 1044 
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
        self.enterRule(localctx, 100, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1046
            self.match(OParser.WRITE)
            self.state = 1047
            self.match(OParser.LPAR)
            self.state = 1048 
            localctx.what = self.expression(0)
            self.state = 1049
            self.match(OParser.RPAR)
            self.state = 1050
            self.match(OParser.TO)
            self.state = 1051 
            localctx.target = self.expression(0)
            self.state = 1052
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Fetch_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_fetch_expression

     
        def copyFrom(self, ctx):
            super(OParser.Fetch_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Fetch_expressionContext)
            super(OParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Category_typeContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(OParser.FETCH, 0)
        def ONE(self):
            return self.getToken(OParser.ONE, 0)
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
        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)
        def category_type(self):
            return self.getTypedRuleContext(OParser.Category_typeContext,0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitFetchOne(self)


    class FetchListContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Fetch_expressionContext)
            super(OParser.FetchListContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(OParser.FETCH, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def FROM(self):
            return self.getToken(OParser.FROM, 0)
        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterFetchList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitFetchList(self)


    class FetchAllContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Fetch_expressionContext)
            super(OParser.FetchAllContext, self).__init__(parser)
            self.start = None # ExpressionContext
            self.end = None # ExpressionContext
            self.typ = None # Category_typeContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(OParser.FETCH, 0)
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
        def category_type(self):
            return self.getTypedRuleContext(OParser.Category_typeContext,0)

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

        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterFetchAll(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitFetchAll(self)



    def fetch_expression(self):

        localctx = OParser.Fetch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_fetch_expression)
        try:
            self.state = 1092
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                localctx = OParser.FetchListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1054
                self.match(OParser.FETCH)
                self.state = 1055
                self.match(OParser.LPAR)
                self.state = 1056 
                localctx.name = self.variable_identifier()
                self.state = 1057
                self.match(OParser.RPAR)
                self.state = 1058
                self.match(OParser.FROM)
                self.state = 1059 
                localctx.source = self.expression(0)
                self.state = 1060
                self.match(OParser.WHERE)
                self.state = 1061 
                localctx.xfilter = self.expression(0)
                pass

            elif la_ == 2:
                localctx = OParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1063
                self.match(OParser.FETCH)
                self.state = 1064
                self.match(OParser.ONE)
                self.state = 1065
                self.match(OParser.LPAR)
                self.state = 1066 
                localctx.typ = self.category_type()
                self.state = 1067
                self.match(OParser.RPAR)
                self.state = 1068
                self.match(OParser.WHERE)
                self.state = 1069
                self.match(OParser.LPAR)
                self.state = 1070 
                localctx.xfilter = self.expression(0)
                self.state = 1071
                self.match(OParser.RPAR)
                pass

            elif la_ == 3:
                localctx = OParser.FetchAllContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1073
                self.match(OParser.FETCH)
                self.state = 1080
                token = self._input.LA(1)
                if token in [OParser.ALL]:
                    self.state = 1074
                    self.match(OParser.ALL)

                elif token in [OParser.ROWS]:
                    self.state = 1075
                    self.match(OParser.ROWS)
                    self.state = 1076 
                    localctx.start = self.expression(0)
                    self.state = 1077
                    self.match(OParser.TO)
                    self.state = 1078 
                    localctx.end = self.expression(0)

                else:
                    raise NoViableAltException(self)

                self.state = 1082
                self.match(OParser.LPAR)
                self.state = 1083 
                localctx.typ = self.category_type()
                self.state = 1084
                self.match(OParser.RPAR)
                self.state = 1090
                la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                if la_ == 1:
                    self.state = 1085
                    self.match(OParser.WHERE)
                    self.state = 1086
                    self.match(OParser.LPAR)
                    self.state = 1087 
                    localctx.xfilter = self.expression(0)
                    self.state = 1088
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
        self.enterRule(localctx, 104, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1094
            self.match(OParser.SORTED)
            self.state = 1095
            self.match(OParser.LPAR)
            self.state = 1096 
            localctx.source = self.instance_expression(0)
            self.state = 1102
            _la = self._input.LA(1)
            if _la==OParser.COMMA:
                self.state = 1097
                self.match(OParser.COMMA)
                self.state = 1098 
                self.key_token()
                self.state = 1099
                self.match(OParser.EQ)
                self.state = 1100 
                localctx.key = self.instance_expression(0)


            self.state = 1104
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
        self.enterRule(localctx, 106, self.RULE_selector_expression)
        try:
            self.state = 1116
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                localctx = OParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1106
                self.match(OParser.DOT)
                self.state = 1107 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = OParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1108
                self.match(OParser.LBRAK)
                self.state = 1109 
                localctx.exp = self.expression(0)
                self.state = 1110
                self.match(OParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = OParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1112
                self.match(OParser.LBRAK)
                self.state = 1113 
                localctx.xslice = self.slice_arguments()
                self.state = 1114
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
            self.typ = None # Category_typeContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def category_type(self):
            return self.getTypedRuleContext(OParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

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
        self.enterRule(localctx, 108, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1119
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1118
                self.match(OParser.MUTABLE)


            self.state = 1121 
            localctx.typ = self.category_type()
            self.state = 1122
            self.match(OParser.LPAR)
            self.state = 1124
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT))) != 0) or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (OParser.EXECUTE - 83)) | (1 << (OParser.FETCH - 83)) | (1 << (OParser.MUTABLE - 83)) | (1 << (OParser.NULL - 83)) | (1 << (OParser.READ - 83)) | (1 << (OParser.SELF - 83)) | (1 << (OParser.SORTED - 83)) | (1 << (OParser.THIS - 83)) | (1 << (OParser.BOOLEAN_LITERAL - 83)) | (1 << (OParser.CHAR_LITERAL - 83)) | (1 << (OParser.MIN_INTEGER - 83)) | (1 << (OParser.MAX_INTEGER - 83)) | (1 << (OParser.SYMBOL_IDENTIFIER - 83)) | (1 << (OParser.TYPE_IDENTIFIER - 83)) | (1 << (OParser.VARIABLE_IDENTIFIER - 83)) | (1 << (OParser.TEXT_LITERAL - 83)) | (1 << (OParser.INTEGER_LITERAL - 83)))) != 0) or ((((_la - 147)) & ~0x3f) == 0 and ((1 << (_la - 147)) & ((1 << (OParser.HEXA_LITERAL - 147)) | (1 << (OParser.DECIMAL_LITERAL - 147)) | (1 << (OParser.DATETIME_LITERAL - 147)) | (1 << (OParser.TIME_LITERAL - 147)) | (1 << (OParser.DATE_LITERAL - 147)) | (1 << (OParser.PERIOD_LITERAL - 147)))) != 0):
                self.state = 1123 
                localctx.args = self.argument_assignment_list(0)


            self.state = 1126
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
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1133
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                localctx = OParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1129 
                localctx.exp = self.expression(0)
                self.state = 1130
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = OParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1132 
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ArgumentAssignmentListItemContext(self, OParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1135
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1136
                    self.match(OParser.COMMA)
                    self.state = 1137 
                    localctx.item = self.argument_assignment() 
                self.state = 1142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

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
        self.enterRule(localctx, 112, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1143 
            localctx.name = self.variable_identifier()
            self.state = 1144 
            self.assign()
            self.state = 1145 
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
        self.enterRule(localctx, 114, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1147 
            localctx.inst = self.assignable_instance(0)
            self.state = 1148 
            self.assign()
            self.state = 1149 
            localctx.exp = self.expression(0)
            self.state = 1150
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
        self.enterRule(localctx, 116, self.RULE_child_instance)
        try:
            self.state = 1158
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1152
                self.match(OParser.DOT)
                self.state = 1153 
                localctx.name = self.variable_identifier()

            elif token in [OParser.LBRAK]:
                localctx = OParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1154
                self.match(OParser.LBRAK)
                self.state = 1155 
                localctx.exp = self.expression(0)
                self.state = 1156
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
        self.enterRule(localctx, 118, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1160 
            localctx.items = self.variable_identifier_list(0)
            self.state = 1161 
            self.assign()
            self.state = 1162 
            localctx.exp = self.expression(0)
            self.state = 1163
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
        self.enterRule(localctx, 120, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1165
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
            self.items = None # DeclarationsContext
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
        self.enterRule(localctx, 122, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = OParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1168
            _la = self._input.LA(1)
            if ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (OParser.BOOLEAN - 45)) | (1 << (OParser.CHARACTER - 45)) | (1 << (OParser.TEXT - 45)) | (1 << (OParser.INTEGER - 45)) | (1 << (OParser.DECIMAL - 45)) | (1 << (OParser.DATE - 45)) | (1 << (OParser.TIME - 45)) | (1 << (OParser.DATETIME - 45)) | (1 << (OParser.PERIOD - 45)) | (1 << (OParser.CODE - 45)) | (1 << (OParser.ABSTRACT - 45)) | (1 << (OParser.ANY - 45)) | (1 << (OParser.ATTRIBUTE - 45)) | (1 << (OParser.CATEGORY - 45)) | (1 << (OParser.ENUMERATED - 45)) | (1 << (OParser.METHOD - 45)) | (1 << (OParser.NATIVE - 45)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (OParser.SINGLETON - 121)) | (1 << (OParser.STORABLE - 121)) | (1 << (OParser.TEST - 121)) | (1 << (OParser.TYPE_IDENTIFIER - 121)))) != 0):
                self.state = 1167 
                localctx.items = self.declarations(0)


            self.state = 1170 
            self.lfs()
            self.state = 1171
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


        def getRuleIndex(self):
            return OParser.RULE_declarations

     
        def copyFrom(self, ctx):
            super(OParser.DeclarationsContext, self).copyFrom(ctx)


    class DeclarationListItemContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a OParser.DeclarationsContext)
            super(OParser.DeclarationListItemContext, self).__init__(parser)
            self.items = None # DeclarationsContext
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(OParser.LfpContext,0)

        def declarations(self):
            return self.getTypedRuleContext(OParser.DeclarationsContext,0)

        def declaration(self):
            return self.getTypedRuleContext(OParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDeclarationListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDeclarationListItem(self)


    class DeclarationListContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a OParser.DeclarationsContext)
            super(OParser.DeclarationListContext, self).__init__(parser)
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(OParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDeclarationList(self)



    def declarations(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.DeclarationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_declarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.DeclarationListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1174 
            localctx.item = self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1182
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.DeclarationListItemContext(self, OParser.DeclarationsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarations)
                    self.state = 1176
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1177 
                    self.lfp()
                    self.state = 1178 
                    localctx.item = self.declaration() 
                self.state = 1184
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_declaration

     
        def copyFrom(self, ctx):
            super(OParser.DeclarationContext, self).copyFrom(ctx)



    class ResourceDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a OParser.DeclarationContext)
            super(OParser.ResourceDeclarationContext, self).__init__(parser)
            self.decl = None # Resource_declarationContext
            self.copyFrom(ctx)

        def resource_declaration(self):
            return self.getTypedRuleContext(OParser.Resource_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterResourceDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitResourceDeclaration(self)


    class MethodDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a OParser.DeclarationContext)
            super(OParser.MethodDeclarationContext, self).__init__(parser)
            self.decl = None # Method_declarationContext
            self.copyFrom(ctx)

        def method_declaration(self):
            return self.getTypedRuleContext(OParser.Method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethodDeclaration(self)


    class CategoryDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a OParser.DeclarationContext)
            super(OParser.CategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Category_declarationContext
            self.copyFrom(ctx)

        def category_declaration(self):
            return self.getTypedRuleContext(OParser.Category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategoryDeclaration(self)


    class AttributeDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a OParser.DeclarationContext)
            super(OParser.AttributeDeclarationContext, self).__init__(parser)
            self.decl = None # Attribute_declarationContext
            self.copyFrom(ctx)

        def attribute_declaration(self):
            return self.getTypedRuleContext(OParser.Attribute_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAttributeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAttributeDeclaration(self)


    class EnumDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a OParser.DeclarationContext)
            super(OParser.EnumDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_declarationContext
            self.copyFrom(ctx)

        def enum_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitEnumDeclaration(self)



    def declaration(self):

        localctx = OParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_declaration)
        try:
            self.state = 1190
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                localctx = OParser.AttributeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1185 
                localctx.decl = self.attribute_declaration()
                pass

            elif la_ == 2:
                localctx = OParser.CategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1186 
                localctx.decl = self.category_declaration()
                pass

            elif la_ == 3:
                localctx = OParser.ResourceDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1187 
                localctx.decl = self.resource_declaration()
                pass

            elif la_ == 4:
                localctx = OParser.EnumDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1188 
                localctx.decl = self.enum_declaration()
                pass

            elif la_ == 5:
                localctx = OParser.MethodDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1189 
                localctx.decl = self.method_declaration()
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
            self.decl = None # Native_resource_declarationContext

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
        self.enterRule(localctx, 128, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1192 
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
            super(OParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_enum_declaration

     
        def copyFrom(self, ctx):
            super(OParser.Enum_declarationContext, self).copyFrom(ctx)



    class EnumCategoryDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Enum_declarationContext)
            super(OParser.EnumCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_category_declarationContext
            self.copyFrom(ctx)

        def enum_category_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterEnumCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitEnumCategoryDeclaration(self)


    class EnumNativeDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Enum_declarationContext)
            super(OParser.EnumNativeDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_native_declarationContext
            self.copyFrom(ctx)

        def enum_native_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_native_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterEnumNativeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitEnumNativeDeclaration(self)



    def enum_declaration(self):

        localctx = OParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_enum_declaration)
        try:
            self.state = 1196
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                localctx = OParser.EnumCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1194 
                localctx.decl = self.enum_category_declaration()
                pass

            elif la_ == 2:
                localctx = OParser.EnumNativeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1195 
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
            super(OParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_native_symbol_list

     
        def copyFrom(self, ctx):
            super(OParser.Native_symbol_listContext, self).copyFrom(ctx)


    class NativeSymbolListContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_symbol_listContext)
            super(OParser.NativeSymbolListContext, self).__init__(parser)
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def native_symbol(self):
            return self.getTypedRuleContext(OParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNativeSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNativeSymbolList(self)


    class NativeSymbolListItemContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_symbol_listContext)
            super(OParser.NativeSymbolListItemContext, self).__init__(parser)
            self.items = None # Native_symbol_listContext
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(OParser.LfpContext,0)

        def native_symbol_list(self):
            return self.getTypedRuleContext(OParser.Native_symbol_listContext,0)

        def native_symbol(self):
            return self.getTypedRuleContext(OParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNativeSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNativeSymbolListItem(self)



    def native_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Native_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_native_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.NativeSymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1199 
            localctx.item = self.native_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,78,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.NativeSymbolListItemContext(self, OParser.Native_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_symbol_list)
                    self.state = 1201
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1202 
                    self.lfp()
                    self.state = 1203 
                    localctx.item = self.native_symbol() 
                self.state = 1209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_category_symbol_list

     
        def copyFrom(self, ctx):
            super(OParser.Category_symbol_listContext, self).copyFrom(ctx)


    class CategorySymbolListItemContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_symbol_listContext)
            super(OParser.CategorySymbolListItemContext, self).__init__(parser)
            self.items = None # Category_symbol_listContext
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(OParser.LfpContext,0)

        def category_symbol_list(self):
            return self.getTypedRuleContext(OParser.Category_symbol_listContext,0)

        def category_symbol(self):
            return self.getTypedRuleContext(OParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCategorySymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategorySymbolListItem(self)


    class CategorySymbolListContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_symbol_listContext)
            super(OParser.CategorySymbolListContext, self).__init__(parser)
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def category_symbol(self):
            return self.getTypedRuleContext(OParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCategorySymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategorySymbolList(self)



    def category_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Category_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_category_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CategorySymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1211 
            localctx.item = self.category_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CategorySymbolListItemContext(self, OParser.Category_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_symbol_list)
                    self.state = 1213
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1214 
                    self.lfp()
                    self.state = 1215 
                    localctx.item = self.category_symbol() 
                self.state = 1221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_symbol_list

     
        def copyFrom(self, ctx):
            super(OParser.Symbol_listContext, self).copyFrom(ctx)


    class SymbolListContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Symbol_listContext)
            super(OParser.SymbolListContext, self).__init__(parser)
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSymbolList(self)


    class SymbolListItemContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Symbol_listContext)
            super(OParser.SymbolListItemContext, self).__init__(parser)
            self.items = None # Symbol_listContext
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def symbol_list(self):
            return self.getTypedRuleContext(OParser.Symbol_listContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSymbolListItem(self)



    def symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.SymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1223 
            localctx.item = self.symbol_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.SymbolListItemContext(self, OParser.Symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_symbol_list)
                    self.state = 1225
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1226
                    self.match(OParser.COMMA)
                    self.state = 1227 
                    localctx.item = self.symbol_identifier() 
                self.state = 1232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 138, self.RULE_attribute_constraint)
        try:
            self.state = 1243
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                localctx = OParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1233
                self.match(OParser.IN)
                self.state = 1234 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = OParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1235
                self.match(OParser.IN)
                self.state = 1236 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = OParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1237
                self.match(OParser.IN)
                self.state = 1238 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = OParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1239
                self.match(OParser.MATCHING)
                self.state = 1240
                localctx.text = self.match(OParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = OParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1241
                self.match(OParser.MATCHING)
                self.state = 1242 
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
            self.items = None # Expression_listContext

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

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
        self.enterRule(localctx, 140, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1245
            self.match(OParser.LBRAK)
            self.state = 1247
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT))) != 0) or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (OParser.EXECUTE - 83)) | (1 << (OParser.FETCH - 83)) | (1 << (OParser.MUTABLE - 83)) | (1 << (OParser.NULL - 83)) | (1 << (OParser.READ - 83)) | (1 << (OParser.SELF - 83)) | (1 << (OParser.SORTED - 83)) | (1 << (OParser.THIS - 83)) | (1 << (OParser.BOOLEAN_LITERAL - 83)) | (1 << (OParser.CHAR_LITERAL - 83)) | (1 << (OParser.MIN_INTEGER - 83)) | (1 << (OParser.MAX_INTEGER - 83)) | (1 << (OParser.SYMBOL_IDENTIFIER - 83)) | (1 << (OParser.TYPE_IDENTIFIER - 83)) | (1 << (OParser.VARIABLE_IDENTIFIER - 83)) | (1 << (OParser.TEXT_LITERAL - 83)) | (1 << (OParser.INTEGER_LITERAL - 83)))) != 0) or ((((_la - 147)) & ~0x3f) == 0 and ((1 << (_la - 147)) & ((1 << (OParser.HEXA_LITERAL - 147)) | (1 << (OParser.DECIMAL_LITERAL - 147)) | (1 << (OParser.DATETIME_LITERAL - 147)) | (1 << (OParser.TIME_LITERAL - 147)) | (1 << (OParser.DATE_LITERAL - 147)) | (1 << (OParser.PERIOD_LITERAL - 147)))) != 0):
                self.state = 1246 
                localctx.items = self.expression_list(0)


            self.state = 1249
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
            self.items = None # Expression_listContext

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

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
        self.enterRule(localctx, 142, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1251
            self.match(OParser.LT)
            self.state = 1253
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT))) != 0) or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (OParser.EXECUTE - 83)) | (1 << (OParser.FETCH - 83)) | (1 << (OParser.MUTABLE - 83)) | (1 << (OParser.NULL - 83)) | (1 << (OParser.READ - 83)) | (1 << (OParser.SELF - 83)) | (1 << (OParser.SORTED - 83)) | (1 << (OParser.THIS - 83)) | (1 << (OParser.BOOLEAN_LITERAL - 83)) | (1 << (OParser.CHAR_LITERAL - 83)) | (1 << (OParser.MIN_INTEGER - 83)) | (1 << (OParser.MAX_INTEGER - 83)) | (1 << (OParser.SYMBOL_IDENTIFIER - 83)) | (1 << (OParser.TYPE_IDENTIFIER - 83)) | (1 << (OParser.VARIABLE_IDENTIFIER - 83)) | (1 << (OParser.TEXT_LITERAL - 83)) | (1 << (OParser.INTEGER_LITERAL - 83)))) != 0) or ((((_la - 147)) & ~0x3f) == 0 and ((1 << (_la - 147)) & ((1 << (OParser.HEXA_LITERAL - 147)) | (1 << (OParser.DECIMAL_LITERAL - 147)) | (1 << (OParser.DATETIME_LITERAL - 147)) | (1 << (OParser.TIME_LITERAL - 147)) | (1 << (OParser.DATE_LITERAL - 147)) | (1 << (OParser.PERIOD_LITERAL - 147)))) != 0):
                self.state = 1252 
                localctx.items = self.expression_list(0)


            self.state = 1255
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


        def getRuleIndex(self):
            return OParser.RULE_expression_list

     
        def copyFrom(self, ctx):
            super(OParser.Expression_listContext, self).copyFrom(ctx)


    class ValueListContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Expression_listContext)
            super(OParser.ValueListContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterValueList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitValueList(self)


    class ValueListItemContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Expression_listContext)
            super(OParser.ValueListItemContext, self).__init__(parser)
            self.items = None # Expression_listContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def expression_list(self):
            return self.getTypedRuleContext(OParser.Expression_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterValueListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitValueListItem(self)



    def expression_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 144
        self.enterRecursionRule(localctx, 144, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.ValueListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1258 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ValueListItemContext(self, OParser.Expression_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 1260
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1261
                    self.match(OParser.COMMA)
                    self.state = 1262 
                    localctx.item = self.expression(0) 
                self.state = 1267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 146, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1268
            self.match(OParser.LBRAK)
            self.state = 1269 
            localctx.low = self.expression(0)
            self.state = 1270
            self.match(OParser.RANGE)
            self.state = 1271 
            localctx.high = self.expression(0)
            self.state = 1272
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
        _startState = 148
        self.enterRecursionRule(localctx, 148, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PrimaryTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1275 
            localctx.p = self.primary_type()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1287
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1285
                    la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
                    if la_ == 1:
                        localctx = OParser.SetTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1277
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1278
                        self.match(OParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = OParser.ListTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1279
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1280
                        self.match(OParser.LBRAK)
                        self.state = 1281
                        self.match(OParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = OParser.DictTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1282
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1283
                        self.match(OParser.LCURL)
                        self.state = 1284
                        self.match(OParser.RCURL)
                        pass

             
                self.state = 1289
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

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
        self.enterRule(localctx, 150, self.RULE_primary_type)
        try:
            self.state = 1292
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.CODE]:
                localctx = OParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1290 
                localctx.n = self.native_type()

            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1291 
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



    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.IntegerTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitIntegerType(self)


    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.PeriodTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitPeriodType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DateTimeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDateTimeType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.BooleanTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitBooleanType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DecimalTypeContext, self).__init__(parser)
            self.t1 = None # Token
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
            self.t1 = None # Token
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(OParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCodeType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.CharacterTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCharacterType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DateTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDateType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.TextTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTextType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.TimeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTimeType(self)



    def native_type(self):

        localctx = OParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_native_type)
        try:
            self.state = 1304
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN]:
                localctx = OParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1294
                localctx.t1 = self.match(OParser.BOOLEAN)

            elif token in [OParser.CHARACTER]:
                localctx = OParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1295
                localctx.t1 = self.match(OParser.CHARACTER)

            elif token in [OParser.TEXT]:
                localctx = OParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1296
                localctx.t1 = self.match(OParser.TEXT)

            elif token in [OParser.INTEGER]:
                localctx = OParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1297
                localctx.t1 = self.match(OParser.INTEGER)

            elif token in [OParser.DECIMAL]:
                localctx = OParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1298
                localctx.t1 = self.match(OParser.DECIMAL)

            elif token in [OParser.DATE]:
                localctx = OParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1299
                localctx.t1 = self.match(OParser.DATE)

            elif token in [OParser.DATETIME]:
                localctx = OParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1300
                localctx.t1 = self.match(OParser.DATETIME)

            elif token in [OParser.TIME]:
                localctx = OParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1301
                localctx.t1 = self.match(OParser.TIME)

            elif token in [OParser.PERIOD]:
                localctx = OParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1302
                localctx.t1 = self.match(OParser.PERIOD)

            elif token in [OParser.CODE]:
                localctx = OParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1303
                localctx.t1 = self.match(OParser.CODE)

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
        self.enterRule(localctx, 154, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1306
            localctx.t1 = self.match(OParser.TYPE_IDENTIFIER)
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
        self.enterRule(localctx, 156, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1308
            localctx.t1 = self.match(OParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Document_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def DOCUMENT(self):
            return self.getToken(OParser.DOCUMENT, 0)

        def getRuleIndex(self):
            return OParser.RULE_document_type

        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDocument_type(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDocument_type(self)




    def document_type(self):

        localctx = OParser.Document_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_document_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1310
            localctx.t1 = self.match(OParser.DOCUMENT)
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
        self.enterRule(localctx, 160, self.RULE_category_declaration)
        try:
            self.state = 1315
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                localctx = OParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1312 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = OParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1313 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = OParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1314 
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


        def getRuleIndex(self):
            return OParser.RULE_type_identifier_list

     
        def copyFrom(self, ctx):
            super(OParser.Type_identifier_listContext, self).copyFrom(ctx)


    class TypeIdentifierListContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Type_identifier_listContext)
            super(OParser.TypeIdentifierListContext, self).__init__(parser)
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTypeIdentifierList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTypeIdentifierList(self)


    class TypeIdentifierListItemContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Type_identifier_listContext)
            super(OParser.TypeIdentifierListItemContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def type_identifier_list(self):
            return self.getTypedRuleContext(OParser.Type_identifier_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTypeIdentifierListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTypeIdentifierListItem(self)



    def type_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Type_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 162
        self.enterRecursionRule(localctx, 162, self.RULE_type_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.TypeIdentifierListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1318 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,90,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.TypeIdentifierListItemContext(self, OParser.Type_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_identifier_list)
                    self.state = 1320
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1321
                    self.match(OParser.COMMA)
                    self.state = 1322 
                    localctx.item = self.type_identifier() 
                self.state = 1327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,90,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_method_identifier

     
        def copyFrom(self, ctx):
            super(OParser.Method_identifierContext, self).copyFrom(ctx)



    class MethodVariableIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_identifierContext)
            super(OParser.MethodVariableIdentifierContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterMethodVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethodVariableIdentifier(self)


    class MethodTypeIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_identifierContext)
            super(OParser.MethodTypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterMethodTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitMethodTypeIdentifier(self)



    def method_identifier(self):

        localctx = OParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_method_identifier)
        try:
            self.state = 1330
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.MethodVariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1328 
                localctx.name = self.variable_identifier()

            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.MethodTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1329 
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
            super(OParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(OParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a OParser.IdentifierContext)
            super(OParser.TypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
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
            self.name = None # Symbol_identifierContext
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
            self.name = None # Variable_identifierContext
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
        self.enterRule(localctx, 166, self.RULE_identifier)
        try:
            self.state = 1335
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1332 
                localctx.name = self.variable_identifier()

            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1333 
                localctx.name = self.type_identifier()

            elif token in [OParser.SYMBOL_IDENTIFIER]:
                localctx = OParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1334 
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
        self.enterRule(localctx, 168, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1337
            self.match(OParser.VARIABLE_IDENTIFIER)
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
        self.enterRule(localctx, 170, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1339
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
        self.enterRule(localctx, 172, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1341
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


        def getRuleIndex(self):
            return OParser.RULE_argument_list

     
        def copyFrom(self, ctx):
            super(OParser.Argument_listContext, self).copyFrom(ctx)


    class ArgumentListItemContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Argument_listContext)
            super(OParser.ArgumentListItemContext, self).__init__(parser)
            self.items = None # Argument_listContext
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def argument_list(self):
            return self.getTypedRuleContext(OParser.Argument_listContext,0)

        def argument(self):
            return self.getTypedRuleContext(OParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitArgumentListItem(self)


    class ArgumentListContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Argument_listContext)
            super(OParser.ArgumentListContext, self).__init__(parser)
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def argument(self):
            return self.getTypedRuleContext(OParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitArgumentList(self)



    def argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 174
        self.enterRecursionRule(localctx, 174, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.ArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1344 
            localctx.item = self.argument()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,93,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ArgumentListItemContext(self, OParser.Argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 1346
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1347
                    self.match(OParser.COMMA)
                    self.state = 1348 
                    localctx.item = self.argument() 
                self.state = 1353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,93,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 176, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1359
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                localctx = OParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1354 
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = OParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1356
                _la = self._input.LA(1)
                if _la==OParser.MUTABLE:
                    self.state = 1355
                    self.match(OParser.MUTABLE)


                self.state = 1358 
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


        def getRuleIndex(self):
            return OParser.RULE_operator_argument

     
        def copyFrom(self, ctx):
            super(OParser.Operator_argumentContext, self).copyFrom(ctx)



    class TypedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a OParser.Operator_argumentContext)
            super(OParser.TypedArgumentContext, self).__init__(parser)
            self.arg = None # Typed_argumentContext
            self.copyFrom(ctx)

        def typed_argument(self):
            return self.getTypedRuleContext(OParser.Typed_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTypedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTypedArgument(self)


    class NamedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a OParser.Operator_argumentContext)
            super(OParser.NamedArgumentContext, self).__init__(parser)
            self.arg = None # Named_argumentContext
            self.copyFrom(ctx)

        def named_argument(self):
            return self.getTypedRuleContext(OParser.Named_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNamedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNamedArgument(self)



    def operator_argument(self):

        localctx = OParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_operator_argument)
        try:
            self.state = 1363
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.NamedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1361 
                localctx.arg = self.named_argument()

            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.CODE, OParser.ANY, OParser.TYPE_IDENTIFIER]:
                localctx = OParser.TypedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1362 
                localctx.arg = self.typed_argument()

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
            self.name = None # Variable_identifierContext
            self.value = None # Literal_expressionContext

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
        self.enterRule(localctx, 180, self.RULE_named_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1365 
            localctx.name = self.variable_identifier()
            self.state = 1368
            la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
            if la_ == 1:
                self.state = 1366
                self.match(OParser.EQ)
                self.state = 1367 
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
        self.enterRule(localctx, 182, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1370 
            self.code_type()
            self.state = 1371 
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


        def getRuleIndex(self):
            return OParser.RULE_category_or_any_type

     
        def copyFrom(self, ctx):
            super(OParser.Category_or_any_typeContext, self).copyFrom(ctx)



    class AnyArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_or_any_typeContext)
            super(OParser.AnyArgumentTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(OParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAnyArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAnyArgumentType(self)


    class CategoryArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_or_any_typeContext)
            super(OParser.CategoryArgumentTypeContext, self).__init__(parser)
            self.typ = None # TypedefContext
            self.copyFrom(ctx)

        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCategoryArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategoryArgumentType(self)



    def category_or_any_type(self):

        localctx = OParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_category_or_any_type)
        try:
            self.state = 1375
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.CODE, OParser.TYPE_IDENTIFIER]:
                localctx = OParser.CategoryArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1373 
                localctx.typ = self.typedef(0)

            elif token in [OParser.ANY]:
                localctx = OParser.AnyArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1374 
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
            super(OParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(OParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Any_typeContext)
            super(OParser.AnyListTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def any_type(self):
            return self.getTypedRuleContext(OParser.Any_typeContext,0)


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
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def any_type(self):
            return self.getTypedRuleContext(OParser.Any_typeContext,0)


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
        _startState = 186
        self.enterRecursionRule(localctx, 186, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1378
            self.match(OParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,100,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1386
                    la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
                    if la_ == 1:
                        localctx = OParser.AnyListTypeContext(self, OParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1380
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1381
                        self.match(OParser.LBRAK)
                        self.state = 1382
                        self.match(OParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = OParser.AnyDictTypeContext(self, OParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1383
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1384
                        self.match(OParser.LCURL)
                        self.state = 1385
                        self.match(OParser.RCURL)
                        pass

             
                self.state = 1390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,100,self._ctx)

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


        def getRuleIndex(self):
            return OParser.RULE_member_method_declaration_list

     
        def copyFrom(self, ctx):
            super(OParser.Member_method_declaration_listContext, self).copyFrom(ctx)


    class CategoryMethodListItemContext(Member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Member_method_declaration_listContext)
            super(OParser.CategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Member_method_declaration_listContext
            self.item = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(OParser.LfpContext,0)

        def member_method_declaration_list(self):
            return self.getTypedRuleContext(OParser.Member_method_declaration_listContext,0)

        def member_method_declaration(self):
            return self.getTypedRuleContext(OParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategoryMethodListItem(self)


    class CategoryMethodListContext(Member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Member_method_declaration_listContext)
            super(OParser.CategoryMethodListContext, self).__init__(parser)
            self.item = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def member_method_declaration(self):
            return self.getTypedRuleContext(OParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCategoryMethodList(self)



    def member_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Member_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 188
        self.enterRecursionRule(localctx, 188, self.RULE_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1392 
            localctx.item = self.member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1400
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,101,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CategoryMethodListItemContext(self, OParser.Member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_method_declaration_list)
                    self.state = 1394
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1395 
                    self.lfp()
                    self.state = 1396 
                    localctx.item = self.member_method_declaration() 
                self.state = 1402
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,101,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 190, self.RULE_member_method_declaration)
        try:
            self.state = 1408
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1403 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1404 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1405 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1406 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1407 
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


        def getRuleIndex(self):
            return OParser.RULE_native_member_method_declaration_list

     
        def copyFrom(self, ctx):
            super(OParser.Native_member_method_declaration_listContext, self).copyFrom(ctx)


    class NativeCategoryMethodListContext(Native_member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_member_method_declaration_listContext)
            super(OParser.NativeCategoryMethodListContext, self).__init__(parser)
            self.item = None # Native_member_method_declarationContext
            self.copyFrom(ctx)

        def native_member_method_declaration(self):
            return self.getTypedRuleContext(OParser.Native_member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNativeCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNativeCategoryMethodList(self)


    class NativeCategoryMethodListItemContext(Native_member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_member_method_declaration_listContext)
            super(OParser.NativeCategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Native_member_method_declaration_listContext
            self.item = None # Native_member_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(OParser.LfpContext,0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(OParser.Native_member_method_declaration_listContext,0)

        def native_member_method_declaration(self):
            return self.getTypedRuleContext(OParser.Native_member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNativeCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNativeCategoryMethodListItem(self)



    def native_member_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Native_member_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 192
        self.enterRecursionRule(localctx, 192, self.RULE_native_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.NativeCategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1411 
            localctx.item = self.native_member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1419
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,103,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.NativeCategoryMethodListItemContext(self, OParser.Native_member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_member_method_declaration_list)
                    self.state = 1413
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1414 
                    self.lfp()
                    self.state = 1415 
                    localctx.item = self.native_member_method_declaration() 
                self.state = 1421
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,103,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self):
            return self.getTypedRuleContext(OParser.Member_method_declarationContext,0)


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
        self.enterRule(localctx, 194, self.RULE_native_member_method_declaration)
        try:
            self.state = 1424
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1422 
                self.member_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1423 
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
        self.enterRule(localctx, 196, self.RULE_native_category_binding)
        try:
            self.state = 1436
            token = self._input.LA(1)
            if token in [OParser.JAVA]:
                localctx = OParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1426
                self.match(OParser.JAVA)
                self.state = 1427 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [OParser.CSHARP]:
                localctx = OParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1428
                self.match(OParser.CSHARP)
                self.state = 1429 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [OParser.PYTHON2]:
                localctx = OParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1430
                self.match(OParser.PYTHON2)
                self.state = 1431 
                localctx.binding = self.python_category_binding()

            elif token in [OParser.PYTHON3]:
                localctx = OParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1432
                self.match(OParser.PYTHON3)
                self.state = 1433 
                localctx.binding = self.python_category_binding()

            elif token in [OParser.JAVASCRIPT]:
                localctx = OParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1434
                self.match(OParser.JAVASCRIPT)
                self.state = 1435 
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
            self.id_ = None # IdentifierContext
            self.module = None # Python_moduleContext

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
        self.enterRule(localctx, 198, self.RULE_python_category_binding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1438 
            localctx.id_ = self.identifier()
            self.state = 1440
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1439 
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
        self.enterRule(localctx, 200, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1442
            self.match(OParser.FROM)
            self.state = 1443 
            self.module_token()
            self.state = 1444
            self.match(OParser.COLON)
            self.state = 1445 
            self.identifier()
            self.state = 1450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,107,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1446
                    self.match(OParser.DOT)
                    self.state = 1447 
                    self.identifier() 
                self.state = 1452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,107,self._ctx)

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
        self.enterRule(localctx, 202, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1453
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1454
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
            super(OParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Javascript_moduleContext

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
        self.enterRule(localctx, 204, self.RULE_javascript_category_binding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1456 
            localctx.id_ = self.identifier()
            self.state = 1458
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1457 
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
        self.enterRule(localctx, 206, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1460
            self.match(OParser.FROM)
            self.state = 1461 
            self.module_token()
            self.state = 1462
            self.match(OParser.COLON)
            self.state = 1464
            _la = self._input.LA(1)
            if _la==OParser.SLASH:
                self.state = 1463
                self.match(OParser.SLASH)


            self.state = 1466 
            self.javascript_identifier()
            self.state = 1471
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,110,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1467
                    self.match(OParser.SLASH)
                    self.state = 1468 
                    self.javascript_identifier() 
                self.state = 1473
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,110,self._ctx)

            self.state = 1476
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                self.state = 1474
                self.match(OParser.DOT)
                self.state = 1475 
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


        def getRuleIndex(self):
            return OParser.RULE_variable_identifier_list

     
        def copyFrom(self, ctx):
            super(OParser.Variable_identifier_listContext, self).copyFrom(ctx)


    class VariableListContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Variable_identifier_listContext)
            super(OParser.VariableListContext, self).__init__(parser)
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterVariableList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitVariableList(self)


    class VariableListItemContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Variable_identifier_listContext)
            super(OParser.VariableListItemContext, self).__init__(parser)
            self.items = None # Variable_identifier_listContext
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def variable_identifier_list(self):
            return self.getTypedRuleContext(OParser.Variable_identifier_listContext,0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterVariableListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitVariableListItem(self)



    def variable_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Variable_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 208
        self.enterRecursionRule(localctx, 208, self.RULE_variable_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.VariableListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1479 
            localctx.item = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1486
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,112,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.VariableListItemContext(self, OParser.Variable_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_variable_identifier_list)
                    self.state = 1481
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1482
                    self.match(OParser.COMMA)
                    self.state = 1483 
                    localctx.item = self.variable_identifier() 
                self.state = 1488
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,112,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_method_declaration

     
        def copyFrom(self, ctx):
            super(OParser.Method_declarationContext, self).copyFrom(ctx)



    class NativeMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_declarationContext)
            super(OParser.NativeMethodContext, self).__init__(parser)
            self.decl = None # Native_method_declarationContext
            self.copyFrom(ctx)

        def native_method_declaration(self):
            return self.getTypedRuleContext(OParser.Native_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNativeMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNativeMethod(self)


    class AbstractMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_declarationContext)
            super(OParser.AbstractMethodContext, self).__init__(parser)
            self.decl = None # Abstract_method_declarationContext
            self.copyFrom(ctx)

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(OParser.Abstract_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAbstractMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAbstractMethod(self)


    class ConcreteMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_declarationContext)
            super(OParser.ConcreteMethodContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterConcreteMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitConcreteMethod(self)


    class TestMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_declarationContext)
            super(OParser.TestMethodContext, self).__init__(parser)
            self.decl = None # Test_method_declarationContext
            self.copyFrom(ctx)

        def test_method_declaration(self):
            return self.getTypedRuleContext(OParser.Test_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTestMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTestMethod(self)



    def method_declaration(self):

        localctx = OParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_method_declaration)
        try:
            self.state = 1493
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                localctx = OParser.AbstractMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1489 
                localctx.decl = self.abstract_method_declaration()
                pass

            elif la_ == 2:
                localctx = OParser.ConcreteMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1490 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 3:
                localctx = OParser.NativeMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1491 
                localctx.decl = self.native_method_declaration()
                pass

            elif la_ == 4:
                localctx = OParser.TestMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1492 
                localctx.decl = self.test_method_declaration()
                pass


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


        def getRuleIndex(self):
            return OParser.RULE_native_statement_list

     
        def copyFrom(self, ctx):
            super(OParser.Native_statement_listContext, self).copyFrom(ctx)


    class NativeStatementListItemContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statement_listContext)
            super(OParser.NativeStatementListItemContext, self).__init__(parser)
            self.items = None # Native_statement_listContext
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(OParser.LfpContext,0)

        def native_statement_list(self):
            return self.getTypedRuleContext(OParser.Native_statement_listContext,0)

        def native_statement(self):
            return self.getTypedRuleContext(OParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNativeStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNativeStatementListItem(self)


    class NativeStatementListContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statement_listContext)
            super(OParser.NativeStatementListContext, self).__init__(parser)
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def native_statement(self):
            return self.getTypedRuleContext(OParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterNativeStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitNativeStatementList(self)



    def native_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Native_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 212
        self.enterRecursionRule(localctx, 212, self.RULE_native_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.NativeStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1496 
            localctx.item = self.native_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1504
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,114,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.NativeStatementListItemContext(self, OParser.Native_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_statement_list)
                    self.state = 1498
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1499 
                    self.lfp()
                    self.state = 1500 
                    localctx.item = self.native_statement() 
                self.state = 1506
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,114,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.stmt = None # Csharp_statementContext
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
            self.stmt = None # Java_statementContext
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
            self.stmt = None # Javascript_native_statementContext
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
            self.stmt = None # Python_native_statementContext
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
            self.stmt = None # Python_native_statementContext
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
        self.enterRule(localctx, 214, self.RULE_native_statement)
        try:
            self.state = 1517
            token = self._input.LA(1)
            if token in [OParser.JAVA]:
                localctx = OParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1507
                self.match(OParser.JAVA)
                self.state = 1508 
                localctx.stmt = self.java_statement()

            elif token in [OParser.CSHARP]:
                localctx = OParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1509
                self.match(OParser.CSHARP)
                self.state = 1510 
                localctx.stmt = self.csharp_statement()

            elif token in [OParser.PYTHON2]:
                localctx = OParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1511
                self.match(OParser.PYTHON2)
                self.state = 1512 
                localctx.stmt = self.python_native_statement()

            elif token in [OParser.PYTHON3]:
                localctx = OParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1513
                self.match(OParser.PYTHON3)
                self.state = 1514 
                localctx.stmt = self.python_native_statement()

            elif token in [OParser.JAVASCRIPT]:
                localctx = OParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1515
                self.match(OParser.JAVASCRIPT)
                self.state = 1516 
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
            super(OParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Python_statementContext
            self.module = None # Python_moduleContext

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
        self.enterRule(localctx, 216, self.RULE_python_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1519 
            localctx.stmt = self.python_statement()
            self.state = 1521
            la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
            if la_ == 1:
                self.state = 1520
                self.match(OParser.SEMI)


            self.state = 1524
            la_ = self._interp.adaptivePredict(self._input,117,self._ctx)
            if la_ == 1:
                self.state = 1523 
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
            super(OParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Javascript_statementContext
            self.module = None # Javascript_moduleContext

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
        self.enterRule(localctx, 218, self.RULE_javascript_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1526 
            localctx.stmt = self.javascript_statement()
            self.state = 1528
            la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
            if la_ == 1:
                self.state = 1527
                self.match(OParser.SEMI)


            self.state = 1531
            la_ = self._interp.adaptivePredict(self._input,119,self._ctx)
            if la_ == 1:
                self.state = 1530 
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
            super(OParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_statement_list

     
        def copyFrom(self, ctx):
            super(OParser.Statement_listContext, self).copyFrom(ctx)


    class StatementListContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Statement_listContext)
            super(OParser.StatementListContext, self).__init__(parser)
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(OParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitStatementList(self)


    class StatementListItemContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Statement_listContext)
            super(OParser.StatementListItemContext, self).__init__(parser)
            self.items = None # Statement_listContext
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(OParser.LfpContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)

        def statement(self):
            return self.getTypedRuleContext(OParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitStatementListItem(self)



    def statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 220
        self.enterRecursionRule(localctx, 220, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.StatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1534 
            localctx.item = self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1542
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,120,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.StatementListItemContext(self, OParser.Statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 1536
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1537 
                    self.lfp()
                    self.state = 1538 
                    localctx.item = self.statement() 
                self.state = 1544
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,120,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_assertion_list

     
        def copyFrom(self, ctx):
            super(OParser.Assertion_listContext, self).copyFrom(ctx)


    class AssertionListContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Assertion_listContext)
            super(OParser.AssertionListContext, self).__init__(parser)
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def assertion(self):
            return self.getTypedRuleContext(OParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAssertionList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAssertionList(self)


    class AssertionListItemContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Assertion_listContext)
            super(OParser.AssertionListItemContext, self).__init__(parser)
            self.items = None # Assertion_listContext
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(OParser.LfpContext,0)

        def assertion_list(self):
            return self.getTypedRuleContext(OParser.Assertion_listContext,0)

        def assertion(self):
            return self.getTypedRuleContext(OParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAssertionListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAssertionListItem(self)



    def assertion_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Assertion_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 222
        self.enterRecursionRule(localctx, 222, self.RULE_assertion_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.AssertionListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1546 
            localctx.item = self.assertion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1554
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,121,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.AssertionListItemContext(self, OParser.Assertion_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assertion_list)
                    self.state = 1548
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1549 
                    self.lfp()
                    self.state = 1550 
                    localctx.item = self.assertion() 
                self.state = 1556
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,121,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_switch_case_statement_list

     
        def copyFrom(self, ctx):
            super(OParser.Switch_case_statement_listContext, self).copyFrom(ctx)


    class SwitchCaseStatementListContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Switch_case_statement_listContext)
            super(OParser.SwitchCaseStatementListContext, self).__init__(parser)
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def switch_case_statement(self):
            return self.getTypedRuleContext(OParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSwitchCaseStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSwitchCaseStatementList(self)


    class SwitchCaseStatementListItemContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Switch_case_statement_listContext)
            super(OParser.SwitchCaseStatementListItemContext, self).__init__(parser)
            self.items = None # Switch_case_statement_listContext
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(OParser.LfpContext,0)

        def switch_case_statement_list(self):
            return self.getTypedRuleContext(OParser.Switch_case_statement_listContext,0)

        def switch_case_statement(self):
            return self.getTypedRuleContext(OParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSwitchCaseStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSwitchCaseStatementListItem(self)



    def switch_case_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Switch_case_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 224
        self.enterRecursionRule(localctx, 224, self.RULE_switch_case_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.SwitchCaseStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1558 
            localctx.item = self.switch_case_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1566
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,122,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.SwitchCaseStatementListItemContext(self, OParser.Switch_case_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_switch_case_statement_list)
                    self.state = 1560
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1561 
                    self.lfp()
                    self.state = 1562 
                    localctx.item = self.switch_case_statement() 
                self.state = 1568
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,122,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_catch_statement_list

     
        def copyFrom(self, ctx):
            super(OParser.Catch_statement_listContext, self).copyFrom(ctx)


    class CatchStatementListContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Catch_statement_listContext)
            super(OParser.CatchStatementListContext, self).__init__(parser)
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def catch_statement(self):
            return self.getTypedRuleContext(OParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCatchStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCatchStatementList(self)


    class CatchStatementListItemContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Catch_statement_listContext)
            super(OParser.CatchStatementListItemContext, self).__init__(parser)
            self.items = None # Catch_statement_listContext
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(OParser.LfpContext,0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(OParser.Catch_statement_listContext,0)

        def catch_statement(self):
            return self.getTypedRuleContext(OParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCatchStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCatchStatementListItem(self)



    def catch_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Catch_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 226
        self.enterRecursionRule(localctx, 226, self.RULE_catch_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CatchStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1570 
            localctx.item = self.catch_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1578
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,123,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CatchStatementListItemContext(self, OParser.Catch_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_catch_statement_list)
                    self.state = 1572
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1573 
                    self.lfp()
                    self.state = 1574 
                    localctx.item = self.catch_statement() 
                self.state = 1580
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,123,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(OParser.Literal_list_literalContext,0)


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
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(OParser.LT, 0)
        def GT(self):
            return self.getToken(OParser.GT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(OParser.Literal_list_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = OParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_literal_collection)
        try:
            self.state = 1595
            la_ = self._interp.adaptivePredict(self._input,124,self._ctx)
            if la_ == 1:
                localctx = OParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1581
                self.match(OParser.LBRAK)
                self.state = 1582 
                localctx.low = self.atomic_literal()
                self.state = 1583
                self.match(OParser.RANGE)
                self.state = 1584 
                localctx.high = self.atomic_literal()
                self.state = 1585
                self.match(OParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = OParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1587
                self.match(OParser.LBRAK)
                self.state = 1588 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1589
                self.match(OParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = OParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1591
                self.match(OParser.LT)
                self.state = 1592 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1593
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
        self.enterRule(localctx, 230, self.RULE_atomic_literal)
        try:
            self.state = 1610
            token = self._input.LA(1)
            if token in [OParser.MIN_INTEGER]:
                localctx = OParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1597
                localctx.t = self.match(OParser.MIN_INTEGER)

            elif token in [OParser.MAX_INTEGER]:
                localctx = OParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1598
                localctx.t = self.match(OParser.MAX_INTEGER)

            elif token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1599
                localctx.t = self.match(OParser.INTEGER_LITERAL)

            elif token in [OParser.HEXA_LITERAL]:
                localctx = OParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1600
                localctx.t = self.match(OParser.HEXA_LITERAL)

            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1601
                localctx.t = self.match(OParser.CHAR_LITERAL)

            elif token in [OParser.DATE_LITERAL]:
                localctx = OParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1602
                localctx.t = self.match(OParser.DATE_LITERAL)

            elif token in [OParser.TIME_LITERAL]:
                localctx = OParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1603
                localctx.t = self.match(OParser.TIME_LITERAL)

            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1604
                localctx.t = self.match(OParser.TEXT_LITERAL)

            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1605
                localctx.t = self.match(OParser.DECIMAL_LITERAL)

            elif token in [OParser.DATETIME_LITERAL]:
                localctx = OParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1606
                localctx.t = self.match(OParser.DATETIME_LITERAL)

            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1607
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)

            elif token in [OParser.PERIOD_LITERAL]:
                localctx = OParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1608
                localctx.t = self.match(OParser.PERIOD_LITERAL)

            elif token in [OParser.NULL]:
                localctx = OParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1609 
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


        def getRuleIndex(self):
            return OParser.RULE_literal_list_literal

     
        def copyFrom(self, ctx):
            super(OParser.Literal_list_literalContext, self).copyFrom(ctx)


    class LiteralListContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Literal_list_literalContext)
            super(OParser.LiteralListContext, self).__init__(parser)
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(OParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterLiteralList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitLiteralList(self)


    class LiteralListItemContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Literal_list_literalContext)
            super(OParser.LiteralListItemContext, self).__init__(parser)
            self.items = None # Literal_list_literalContext
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(OParser.Literal_list_literalContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(OParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterLiteralListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitLiteralListItem(self)



    def literal_list_literal(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Literal_list_literalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 232
        self.enterRecursionRule(localctx, 232, self.RULE_literal_list_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.LiteralListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1613 
            localctx.item = self.atomic_literal()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1620
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.LiteralListItemContext(self, OParser.Literal_list_literalContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literal_list_literal)
                    self.state = 1615
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1616
                    self.match(OParser.COMMA)
                    self.state = 1617 
                    localctx.item = self.atomic_literal() 
                self.state = 1622
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 234, self.RULE_selectable_expression)
        try:
            self.state = 1627
            la_ = self._interp.adaptivePredict(self._input,127,self._ctx)
            if la_ == 1:
                localctx = OParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1623 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = OParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1624 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = OParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1625 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = OParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1626 
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
        self.enterRule(localctx, 236, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1629
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
            self.exp = None # ExpressionContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


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
        self.enterRule(localctx, 238, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1631
            self.match(OParser.LPAR)
            self.state = 1632 
            localctx.exp = self.expression(0)
            self.state = 1633
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


        def getRuleIndex(self):
            return OParser.RULE_literal_expression

     
        def copyFrom(self, ctx):
            super(OParser.Literal_expressionContext, self).copyFrom(ctx)



    class CollectionLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Literal_expressionContext)
            super(OParser.CollectionLiteralContext, self).__init__(parser)
            self.exp = None # Collection_literalContext
            self.copyFrom(ctx)

        def collection_literal(self):
            return self.getTypedRuleContext(OParser.Collection_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterCollectionLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitCollectionLiteral(self)


    class AtomicLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Literal_expressionContext)
            super(OParser.AtomicLiteralContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(OParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterAtomicLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitAtomicLiteral(self)



    def literal_expression(self):

        localctx = OParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_literal_expression)
        try:
            self.state = 1637
            token = self._input.LA(1)
            if token in [OParser.NULL, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.MIN_INTEGER, OParser.MAX_INTEGER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.HEXA_LITERAL, OParser.DECIMAL_LITERAL, OParser.DATETIME_LITERAL, OParser.TIME_LITERAL, OParser.DATE_LITERAL, OParser.PERIOD_LITERAL]:
                localctx = OParser.AtomicLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1635 
                localctx.exp = self.atomic_literal()

            elif token in [OParser.LPAR, OParser.LBRAK, OParser.LCURL, OParser.LT]:
                localctx = OParser.CollectionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1636 
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
            super(OParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_collection_literal

     
        def copyFrom(self, ctx):
            super(OParser.Collection_literalContext, self).copyFrom(ctx)



    class ListLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Collection_literalContext)
            super(OParser.ListLiteralContext, self).__init__(parser)
            self.exp = None # List_literalContext
            self.copyFrom(ctx)

        def list_literal(self):
            return self.getTypedRuleContext(OParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitListLiteral(self)


    class RangeLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Collection_literalContext)
            super(OParser.RangeLiteralContext, self).__init__(parser)
            self.exp = None # Range_literalContext
            self.copyFrom(ctx)

        def range_literal(self):
            return self.getTypedRuleContext(OParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitRangeLiteral(self)


    class TupleLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Collection_literalContext)
            super(OParser.TupleLiteralContext, self).__init__(parser)
            self.exp = None # Tuple_literalContext
            self.copyFrom(ctx)

        def tuple_literal(self):
            return self.getTypedRuleContext(OParser.Tuple_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterTupleLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitTupleLiteral(self)


    class SetLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Collection_literalContext)
            super(OParser.SetLiteralContext, self).__init__(parser)
            self.exp = None # Set_literalContext
            self.copyFrom(ctx)

        def set_literal(self):
            return self.getTypedRuleContext(OParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitSetLiteral(self)


    class DictLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Collection_literalContext)
            super(OParser.DictLiteralContext, self).__init__(parser)
            self.exp = None # Dict_literalContext
            self.copyFrom(ctx)

        def dict_literal(self):
            return self.getTypedRuleContext(OParser.Dict_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDictLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDictLiteral(self)



    def collection_literal(self):

        localctx = OParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_collection_literal)
        try:
            self.state = 1644
            la_ = self._interp.adaptivePredict(self._input,129,self._ctx)
            if la_ == 1:
                localctx = OParser.RangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1639 
                localctx.exp = self.range_literal()
                pass

            elif la_ == 2:
                localctx = OParser.ListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1640 
                localctx.exp = self.list_literal()
                pass

            elif la_ == 3:
                localctx = OParser.SetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1641 
                localctx.exp = self.set_literal()
                pass

            elif la_ == 4:
                localctx = OParser.DictLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1642 
                localctx.exp = self.dict_literal()
                pass

            elif la_ == 5:
                localctx = OParser.TupleLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1643 
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
            super(OParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_tupleContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

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
        self.enterRule(localctx, 244, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1646
            self.match(OParser.LPAR)
            self.state = 1648
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT))) != 0) or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (OParser.EXECUTE - 83)) | (1 << (OParser.FETCH - 83)) | (1 << (OParser.MUTABLE - 83)) | (1 << (OParser.NULL - 83)) | (1 << (OParser.READ - 83)) | (1 << (OParser.SELF - 83)) | (1 << (OParser.SORTED - 83)) | (1 << (OParser.THIS - 83)) | (1 << (OParser.BOOLEAN_LITERAL - 83)) | (1 << (OParser.CHAR_LITERAL - 83)) | (1 << (OParser.MIN_INTEGER - 83)) | (1 << (OParser.MAX_INTEGER - 83)) | (1 << (OParser.SYMBOL_IDENTIFIER - 83)) | (1 << (OParser.TYPE_IDENTIFIER - 83)) | (1 << (OParser.VARIABLE_IDENTIFIER - 83)) | (1 << (OParser.TEXT_LITERAL - 83)) | (1 << (OParser.INTEGER_LITERAL - 83)))) != 0) or ((((_la - 147)) & ~0x3f) == 0 and ((1 << (_la - 147)) & ((1 << (OParser.HEXA_LITERAL - 147)) | (1 << (OParser.DECIMAL_LITERAL - 147)) | (1 << (OParser.DATETIME_LITERAL - 147)) | (1 << (OParser.TIME_LITERAL - 147)) | (1 << (OParser.DATE_LITERAL - 147)) | (1 << (OParser.PERIOD_LITERAL - 147)))) != 0):
                self.state = 1647 
                localctx.items = self.expression_tuple(0)


            self.state = 1650
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
            self.items = None # Dict_entry_listContext

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

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
        self.enterRule(localctx, 246, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1652
            self.match(OParser.LCURL)
            self.state = 1654
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT))) != 0) or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (OParser.EXECUTE - 83)) | (1 << (OParser.FETCH - 83)) | (1 << (OParser.MUTABLE - 83)) | (1 << (OParser.NULL - 83)) | (1 << (OParser.READ - 83)) | (1 << (OParser.SELF - 83)) | (1 << (OParser.SORTED - 83)) | (1 << (OParser.THIS - 83)) | (1 << (OParser.BOOLEAN_LITERAL - 83)) | (1 << (OParser.CHAR_LITERAL - 83)) | (1 << (OParser.MIN_INTEGER - 83)) | (1 << (OParser.MAX_INTEGER - 83)) | (1 << (OParser.SYMBOL_IDENTIFIER - 83)) | (1 << (OParser.TYPE_IDENTIFIER - 83)) | (1 << (OParser.VARIABLE_IDENTIFIER - 83)) | (1 << (OParser.TEXT_LITERAL - 83)) | (1 << (OParser.INTEGER_LITERAL - 83)))) != 0) or ((((_la - 147)) & ~0x3f) == 0 and ((1 << (_la - 147)) & ((1 << (OParser.HEXA_LITERAL - 147)) | (1 << (OParser.DECIMAL_LITERAL - 147)) | (1 << (OParser.DATETIME_LITERAL - 147)) | (1 << (OParser.TIME_LITERAL - 147)) | (1 << (OParser.DATE_LITERAL - 147)) | (1 << (OParser.PERIOD_LITERAL - 147)))) != 0):
                self.state = 1653 
                localctx.items = self.dict_entry_list(0)


            self.state = 1656
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


        def getRuleIndex(self):
            return OParser.RULE_expression_tuple

     
        def copyFrom(self, ctx):
            super(OParser.Expression_tupleContext, self).copyFrom(ctx)


    class ValueTupleContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a OParser.Expression_tupleContext)
            super(OParser.ValueTupleContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterValueTuple(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitValueTuple(self)


    class ValueTupleItemContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a OParser.Expression_tupleContext)
            super(OParser.ValueTupleItemContext, self).__init__(parser)
            self.items = None # Expression_tupleContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def expression_tuple(self):
            return self.getTypedRuleContext(OParser.Expression_tupleContext,0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterValueTupleItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitValueTupleItem(self)



    def expression_tuple(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Expression_tupleContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 248
        self.enterRecursionRule(localctx, 248, self.RULE_expression_tuple, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.ValueTupleContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1659 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1666
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,132,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ValueTupleItemContext(self, OParser.Expression_tupleContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_tuple)
                    self.state = 1661
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1662
                    self.match(OParser.COMMA)
                    self.state = 1663 
                    localctx.item = self.expression(0) 
                self.state = 1668
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,132,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Dict_entry_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_dict_entry_list

     
        def copyFrom(self, ctx):
            super(OParser.Dict_entry_listContext, self).copyFrom(ctx)


    class DictEntryListContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Dict_entry_listContext)
            super(OParser.DictEntryListContext, self).__init__(parser)
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def dict_entry(self):
            return self.getTypedRuleContext(OParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDictEntryList(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDictEntryList(self)


    class DictEntryListItemContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Dict_entry_listContext)
            super(OParser.DictEntryListItemContext, self).__init__(parser)
            self.items = None # Dict_entry_listContext
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def dict_entry_list(self):
            return self.getTypedRuleContext(OParser.Dict_entry_listContext,0)

        def dict_entry(self):
            return self.getTypedRuleContext(OParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.enterDictEntryListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, OParserListener ):
                listener.exitDictEntryListItem(self)



    def dict_entry_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Dict_entry_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 250
        self.enterRecursionRule(localctx, 250, self.RULE_dict_entry_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.DictEntryListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1670 
            localctx.item = self.dict_entry()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1677
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,133,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.DictEntryListItemContext(self, OParser.Dict_entry_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dict_entry_list)
                    self.state = 1672
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1673
                    self.match(OParser.COMMA)
                    self.state = 1674 
                    localctx.item = self.dict_entry() 
                self.state = 1679
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,133,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 252, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1680 
            localctx.key = self.expression(0)
            self.state = 1681
            self.match(OParser.COLON)
            self.state = 1682 
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
        self.enterRule(localctx, 254, self.RULE_slice_arguments)
        try:
            self.state = 1693
            la_ = self._interp.adaptivePredict(self._input,134,self._ctx)
            if la_ == 1:
                localctx = OParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1684 
                localctx.first = self.expression(0)
                self.state = 1685
                self.match(OParser.COLON)
                self.state = 1686 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = OParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1688 
                localctx.first = self.expression(0)
                self.state = 1689
                self.match(OParser.COLON)
                pass

            elif la_ == 3:
                localctx = OParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1691
                self.match(OParser.COLON)
                self.state = 1692 
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
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


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
        self.enterRule(localctx, 256, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1695 
            localctx.name = self.variable_identifier()
            self.state = 1696 
            self.assign()
            self.state = 1697 
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
            super(OParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(OParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a OParser.Assignable_instanceContext)
            super(OParser.ChildInstanceContext, self).__init__(parser)
            self.parent = None # Assignable_instanceContext
            self.child = None # Child_instanceContext
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
            self.name = None # Variable_identifierContext
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
        _startState = 258
        self.enterRecursionRule(localctx, 258, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1700 
            localctx.name = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1706
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,135,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ChildInstanceContext(self, OParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1702
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1703 
                    localctx.child = self.child_instance() 
                self.state = 1708
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,135,self._ctx)

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
            self.typ = None # Category_or_any_typeContext
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
            self.exp = None # ExpressionContext
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
        self.enterRule(localctx, 260, self.RULE_is_expression)
        try:
            self.state = 1713
            la_ = self._interp.adaptivePredict(self._input,136,self._ctx)
            if la_ == 1:
                localctx = OParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1709
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1710
                self.match(OParser.VARIABLE_IDENTIFIER)
                self.state = 1711 
                localctx.typ = self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = OParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1712 
                localctx.exp = self.expression(0)
                pass


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
        self.enterRule(localctx, 262, self.RULE_operator)
        try:
            self.state = 1721
            token = self._input.LA(1)
            if token in [OParser.PLUS]:
                localctx = OParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1715
                self.match(OParser.PLUS)

            elif token in [OParser.MINUS]:
                localctx = OParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1716
                self.match(OParser.MINUS)

            elif token in [OParser.STAR]:
                localctx = OParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1717 
                self.multiply()

            elif token in [OParser.SLASH]:
                localctx = OParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1718 
                self.divide()

            elif token in [OParser.BSLASH]:
                localctx = OParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1719 
                self.idivide()

            elif token in [OParser.PERCENT, OParser.MODULO]:
                localctx = OParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1720 
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
        self.enterRule(localctx, 264, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1723
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1724
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
        self.enterRule(localctx, 266, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1726
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1727
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
        self.enterRule(localctx, 268, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1729
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1730
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
        self.enterRule(localctx, 270, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1732
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
        self.enterRule(localctx, 272, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1734
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
        self.enterRule(localctx, 274, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1736
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
        self.enterRule(localctx, 276, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1738
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
        self.enterRule(localctx, 278, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1740
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
        self.enterRule(localctx, 280, self.RULE_lfs)
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
        self.enterRule(localctx, 282, self.RULE_lfp)
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
        self.enterRule(localctx, 284, self.RULE_javascript_statement)
        try:
            self.state = 1753
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1746
                self.match(OParser.RETURN)
                self.state = 1747 
                localctx.exp = self.javascript_expression(0)
                self.state = 1748
                self.match(OParser.SEMI)

            elif token in [OParser.LPAR, OParser.LBRAK, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1750 
                localctx.exp = self.javascript_expression(0)
                self.state = 1751
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
        _startState = 286
        self.enterRecursionRule(localctx, 286, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1756 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1762
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavascriptSelectorExpressionContext(self, OParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1758
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1759 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1764
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,139,self._ctx)

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
        self.enterRule(localctx, 288, self.RULE_javascript_primary_expression)
        try:
            self.state = 1771
            la_ = self._interp.adaptivePredict(self._input,140,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1765 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1766 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1767 
                self.javascript_identifier_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1768 
                self.javascript_literal_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1769 
                self.javascript_method_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1770 
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
        self.enterRule(localctx, 290, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1773 
            self.this_expression()
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
        self.enterRule(localctx, 292, self.RULE_javascript_selector_expression)
        try:
            self.state = 1780
            la_ = self._interp.adaptivePredict(self._input,141,self._ctx)
            if la_ == 1:
                localctx = OParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1775
                self.match(OParser.DOT)
                self.state = 1776 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = OParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1777
                self.match(OParser.DOT)
                self.state = 1778 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = OParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1779 
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
        self.enterRule(localctx, 294, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1782 
            localctx.name = self.javascript_identifier()
            self.state = 1783
            self.match(OParser.LPAR)
            self.state = 1785
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.READ - 113)) | (1 << (OParser.SELF - 113)) | (1 << (OParser.TEST - 113)) | (1 << (OParser.THIS - 113)) | (1 << (OParser.WRITE - 113)) | (1 << (OParser.BOOLEAN_LITERAL - 113)) | (1 << (OParser.CHAR_LITERAL - 113)) | (1 << (OParser.SYMBOL_IDENTIFIER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)) | (1 << (OParser.DOLLAR_IDENTIFIER - 113)) | (1 << (OParser.TEXT_LITERAL - 113)) | (1 << (OParser.INTEGER_LITERAL - 113)) | (1 << (OParser.DECIMAL_LITERAL - 113)))) != 0):
                self.state = 1784 
                localctx.args = self.javascript_arguments(0)


            self.state = 1787
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
        _startState = 296
        self.enterRecursionRule(localctx, 296, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1790 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1797
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,143,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavascriptArgumentListItemContext(self, OParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1792
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1793
                    self.match(OParser.COMMA)
                    self.state = 1794 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1799
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,143,self._ctx)

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
        self.enterRule(localctx, 298, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1800
            self.match(OParser.LBRAK)
            self.state = 1801 
            localctx.exp = self.javascript_expression(0)
            self.state = 1802
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
        self.enterRule(localctx, 300, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1804
            self.match(OParser.LPAR)
            self.state = 1805 
            localctx.exp = self.javascript_expression(0)
            self.state = 1806
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
        self.enterRule(localctx, 302, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1808 
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
        self.enterRule(localctx, 304, self.RULE_javascript_literal_expression)
        try:
            self.state = 1815
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1810
                localctx.t = self.match(OParser.INTEGER_LITERAL)

            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1811
                localctx.t = self.match(OParser.DECIMAL_LITERAL)

            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1812
                localctx.t = self.match(OParser.TEXT_LITERAL)

            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1813
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)

            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1814
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
        self.enterRule(localctx, 306, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1817
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.READ - 113)) | (1 << (OParser.TEST - 113)) | (1 << (OParser.WRITE - 113)) | (1 << (OParser.SYMBOL_IDENTIFIER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)) | (1 << (OParser.DOLLAR_IDENTIFIER - 113)))) != 0)):
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
        self.enterRule(localctx, 308, self.RULE_python_statement)
        try:
            self.state = 1822
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1819
                self.match(OParser.RETURN)
                self.state = 1820 
                localctx.exp = self.python_expression(0)

            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1821 
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
        _startState = 310
        self.enterRecursionRule(localctx, 310, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1825 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1831
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,146,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonSelectorExpressionContext(self, OParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1827
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1828 
                    localctx.child = self.python_selector_expression() 
                self.state = 1833
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

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
        self.enterRule(localctx, 312, self.RULE_python_primary_expression)
        try:
            self.state = 1838
            la_ = self._interp.adaptivePredict(self._input,147,self._ctx)
            if la_ == 1:
                localctx = OParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1834 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = OParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1835 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = OParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1836 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = OParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1837 
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
        self.enterRule(localctx, 314, self.RULE_python_selector_expression)
        try:
            self.state = 1846
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1840
                self.match(OParser.DOT)
                self.state = 1841 
                localctx.exp = self.python_method_expression()

            elif token in [OParser.LBRAK]:
                localctx = OParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1842
                self.match(OParser.LBRAK)
                self.state = 1843 
                localctx.exp = self.python_expression(0)
                self.state = 1844
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
        self.enterRule(localctx, 316, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1848 
            localctx.name = self.python_identifier()
            self.state = 1849
            self.match(OParser.LPAR)
            self.state = 1851
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.READ - 113)) | (1 << (OParser.SELF - 113)) | (1 << (OParser.TEST - 113)) | (1 << (OParser.THIS - 113)) | (1 << (OParser.WRITE - 113)) | (1 << (OParser.BOOLEAN_LITERAL - 113)) | (1 << (OParser.CHAR_LITERAL - 113)) | (1 << (OParser.SYMBOL_IDENTIFIER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)) | (1 << (OParser.DOLLAR_IDENTIFIER - 113)) | (1 << (OParser.TEXT_LITERAL - 113)) | (1 << (OParser.INTEGER_LITERAL - 113)) | (1 << (OParser.DECIMAL_LITERAL - 113)))) != 0):
                self.state = 1850 
                localctx.args = self.python_argument_list()


            self.state = 1853
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
        self.enterRule(localctx, 318, self.RULE_python_argument_list)
        try:
            self.state = 1861
            la_ = self._interp.adaptivePredict(self._input,150,self._ctx)
            if la_ == 1:
                localctx = OParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1855 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = OParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1856 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = OParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1857 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 1858
                self.match(OParser.COMMA)
                self.state = 1859 
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
        _startState = 320
        self.enterRecursionRule(localctx, 320, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1864 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1871
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,151,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonOrdinalArgumentListItemContext(self, OParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 1866
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1867
                    self.match(OParser.COMMA)
                    self.state = 1868 
                    localctx.item = self.python_expression(0) 
                self.state = 1873
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,151,self._ctx)

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
        _startState = 322
        self.enterRecursionRule(localctx, 322, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1875 
            localctx.name = self.python_identifier()
            self.state = 1876
            self.match(OParser.EQ)
            self.state = 1877 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1887
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,152,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonNamedArgumentListItemContext(self, OParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 1879
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1880
                    self.match(OParser.COMMA)
                    self.state = 1881 
                    localctx.name = self.python_identifier()
                    self.state = 1882
                    self.match(OParser.EQ)
                    self.state = 1883 
                    localctx.exp = self.python_expression(0) 
                self.state = 1889
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,152,self._ctx)

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
        self.enterRule(localctx, 324, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1890
            self.match(OParser.LPAR)
            self.state = 1891 
            localctx.exp = self.python_expression(0)
            self.state = 1892
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
        _startState = 326
        self.enterRecursionRule(localctx, 326, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1897
            token = self._input.LA(1)
            if token in [OParser.DOLLAR_IDENTIFIER]:
                localctx = OParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1895
                self.match(OParser.DOLLAR_IDENTIFIER)

            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1896 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1904
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,154,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonChildIdentifierContext(self, OParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 1899
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1900
                    self.match(OParser.DOT)
                    self.state = 1901 
                    localctx.name = self.python_identifier() 
                self.state = 1906
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,154,self._ctx)

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
        self.enterRule(localctx, 328, self.RULE_python_literal_expression)
        try:
            self.state = 1912
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1907
                localctx.t = self.match(OParser.INTEGER_LITERAL)

            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1908
                localctx.t = self.match(OParser.DECIMAL_LITERAL)

            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1909
                localctx.t = self.match(OParser.TEXT_LITERAL)

            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1910
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)

            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1911
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
        self.enterRule(localctx, 330, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1914
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.READ - 113)) | (1 << (OParser.SELF - 113)) | (1 << (OParser.TEST - 113)) | (1 << (OParser.THIS - 113)) | (1 << (OParser.WRITE - 113)) | (1 << (OParser.SYMBOL_IDENTIFIER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)))) != 0)):
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
        self.enterRule(localctx, 332, self.RULE_java_statement)
        try:
            self.state = 1923
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1916
                self.match(OParser.RETURN)
                self.state = 1917 
                localctx.exp = self.java_expression(0)
                self.state = 1918
                self.match(OParser.SEMI)

            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.NATIVE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1920 
                localctx.exp = self.java_expression(0)
                self.state = 1921
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
        _startState = 334
        self.enterRecursionRule(localctx, 334, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1926 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1932
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaSelectorExpressionContext(self, OParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 1928
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1929 
                    localctx.child = self.java_selector_expression() 
                self.state = 1934
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

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
        self.enterRule(localctx, 336, self.RULE_java_primary_expression)
        try:
            self.state = 1939
            token = self._input.LA(1)
            if token in [OParser.SELF, OParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1935 
                self.java_this_expression()

            elif token in [OParser.LPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1936 
                self.java_parenthesis_expression()

            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.TEST, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.NATIVE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1937 
                self.java_identifier_expression(0)

            elif token in [OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1938 
                self.java_literal_expression()

            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 338, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1941 
            self.this_expression()
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
        self.enterRule(localctx, 340, self.RULE_java_selector_expression)
        try:
            self.state = 1946
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1943
                self.match(OParser.DOT)
                self.state = 1944 
                localctx.exp = self.java_method_expression()

            elif token in [OParser.LBRAK]:
                localctx = OParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1945 
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
        self.enterRule(localctx, 342, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1948 
            localctx.name = self.java_identifier()
            self.state = 1949
            self.match(OParser.LPAR)
            self.state = 1951
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.READ - 113)) | (1 << (OParser.SELF - 113)) | (1 << (OParser.TEST - 113)) | (1 << (OParser.THIS - 113)) | (1 << (OParser.WRITE - 113)) | (1 << (OParser.BOOLEAN_LITERAL - 113)) | (1 << (OParser.CHAR_LITERAL - 113)) | (1 << (OParser.SYMBOL_IDENTIFIER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)) | (1 << (OParser.NATIVE_IDENTIFIER - 113)) | (1 << (OParser.DOLLAR_IDENTIFIER - 113)) | (1 << (OParser.TEXT_LITERAL - 113)) | (1 << (OParser.INTEGER_LITERAL - 113)) | (1 << (OParser.DECIMAL_LITERAL - 113)))) != 0):
                self.state = 1950 
                localctx.args = self.java_arguments(0)


            self.state = 1953
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
        _startState = 344
        self.enterRecursionRule(localctx, 344, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1956 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1963
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,161,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaArgumentListItemContext(self, OParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 1958
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1959
                    self.match(OParser.COMMA)
                    self.state = 1960 
                    localctx.item = self.java_expression(0) 
                self.state = 1965
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,161,self._ctx)

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
        self.enterRule(localctx, 346, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1966
            self.match(OParser.LBRAK)
            self.state = 1967 
            localctx.exp = self.java_expression(0)
            self.state = 1968
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
        self.enterRule(localctx, 348, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1970
            self.match(OParser.LPAR)
            self.state = 1971 
            localctx.exp = self.java_expression(0)
            self.state = 1972
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
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1975 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1982
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,162,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaChildIdentifierContext(self, OParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 1977
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1978
                    self.match(OParser.DOT)
                    self.state = 1979 
                    localctx.name = self.java_identifier() 
                self.state = 1984
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,162,self._ctx)

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
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1986 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1992
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,163,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaChildClassIdentifierContext(self, OParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 1988
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1989
                    localctx.name = self.match(OParser.DOLLAR_IDENTIFIER) 
                self.state = 1994
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,163,self._ctx)

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
        self.enterRule(localctx, 354, self.RULE_java_literal_expression)
        try:
            self.state = 2000
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1995
                localctx.t = self.match(OParser.INTEGER_LITERAL)

            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1996
                localctx.t = self.match(OParser.DECIMAL_LITERAL)

            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1997
                localctx.t = self.match(OParser.TEXT_LITERAL)

            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1998
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)

            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1999
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
        self.enterRule(localctx, 356, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2002
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.READ - 113)) | (1 << (OParser.TEST - 113)) | (1 << (OParser.WRITE - 113)) | (1 << (OParser.SYMBOL_IDENTIFIER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)) | (1 << (OParser.NATIVE_IDENTIFIER - 113)) | (1 << (OParser.DOLLAR_IDENTIFIER - 113)))) != 0)):
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
        self.enterRule(localctx, 358, self.RULE_csharp_statement)
        try:
            self.state = 2011
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2004
                self.match(OParser.RETURN)
                self.state = 2005 
                localctx.exp = self.csharp_expression(0)
                self.state = 2006
                self.match(OParser.SEMI)

            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2008 
                localctx.exp = self.csharp_expression(0)
                self.state = 2009
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
        _startState = 360
        self.enterRecursionRule(localctx, 360, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2014 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2020
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,166,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpSelectorExpressionContext(self, OParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2016
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2017 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2022
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,166,self._ctx)

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
        self.enterRule(localctx, 362, self.RULE_csharp_primary_expression)
        try:
            self.state = 2027
            token = self._input.LA(1)
            if token in [OParser.SELF, OParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2023 
                self.csharp_this_expression()

            elif token in [OParser.LPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2024 
                self.csharp_parenthesis_expression()

            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.TEST, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2025 
                self.csharp_identifier_expression(0)

            elif token in [OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2026 
                self.csharp_literal_expression()

            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 364, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2029 
            self.this_expression()
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
        self.enterRule(localctx, 366, self.RULE_csharp_selector_expression)
        try:
            self.state = 2034
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2031
                self.match(OParser.DOT)
                self.state = 2032 
                localctx.exp = self.csharp_method_expression()

            elif token in [OParser.LBRAK]:
                localctx = OParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2033 
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
        self.enterRule(localctx, 368, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2036 
            localctx.name = self.csharp_identifier()
            self.state = 2037
            self.match(OParser.LPAR)
            self.state = 2039
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.READ - 113)) | (1 << (OParser.SELF - 113)) | (1 << (OParser.TEST - 113)) | (1 << (OParser.THIS - 113)) | (1 << (OParser.WRITE - 113)) | (1 << (OParser.BOOLEAN_LITERAL - 113)) | (1 << (OParser.CHAR_LITERAL - 113)) | (1 << (OParser.SYMBOL_IDENTIFIER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)) | (1 << (OParser.DOLLAR_IDENTIFIER - 113)) | (1 << (OParser.TEXT_LITERAL - 113)) | (1 << (OParser.INTEGER_LITERAL - 113)) | (1 << (OParser.DECIMAL_LITERAL - 113)))) != 0):
                self.state = 2038 
                localctx.args = self.csharp_arguments(0)


            self.state = 2041
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
        _startState = 370
        self.enterRecursionRule(localctx, 370, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2044 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2051
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,170,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpArgumentListItemContext(self, OParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2046
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2047
                    self.match(OParser.COMMA)
                    self.state = 2048 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2053
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,170,self._ctx)

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
        self.enterRule(localctx, 372, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2054
            self.match(OParser.LBRAK)
            self.state = 2055 
            localctx.exp = self.csharp_expression(0)
            self.state = 2056
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
        self.enterRule(localctx, 374, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2058
            self.match(OParser.LPAR)
            self.state = 2059 
            localctx.exp = self.csharp_expression(0)
            self.state = 2060
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
        _startState = 376
        self.enterRecursionRule(localctx, 376, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2065
            token = self._input.LA(1)
            if token in [OParser.DOLLAR_IDENTIFIER]:
                localctx = OParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2063
                self.match(OParser.DOLLAR_IDENTIFIER)

            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.READ, OParser.TEST, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2064 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2072
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,172,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpChildIdentifierContext(self, OParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2067
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2068
                    self.match(OParser.DOT)
                    self.state = 2069 
                    localctx.name = self.csharp_identifier() 
                self.state = 2074
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,172,self._ctx)

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
        self.enterRule(localctx, 378, self.RULE_csharp_literal_expression)
        try:
            self.state = 2080
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2075
                self.match(OParser.INTEGER_LITERAL)

            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2076
                self.match(OParser.DECIMAL_LITERAL)

            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2077
                self.match(OParser.TEXT_LITERAL)

            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2078
                self.match(OParser.BOOLEAN_LITERAL)

            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2079
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
        self.enterRule(localctx, 380, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2082
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.READ - 113)) | (1 << (OParser.TEST - 113)) | (1 << (OParser.WRITE - 113)) | (1 << (OParser.SYMBOL_IDENTIFIER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)) | (1 << (OParser.VARIABLE_IDENTIFIER - 113)))) != 0)):
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
        self._predicates[15] = self.native_category_binding_list_sempred
        self._predicates[16] = self.attribute_list_sempred
        self._predicates[34] = self.else_if_statement_list_sempred
        self._predicates[41] = self.callable_parent_sempred
        self._predicates[43] = self.expression_sempred
        self._predicates[44] = self.an_expression_sempred
        self._predicates[46] = self.instance_expression_sempred
        self._predicates[55] = self.argument_assignment_list_sempred
        self._predicates[62] = self.declarations_sempred
        self._predicates[66] = self.native_symbol_list_sempred
        self._predicates[67] = self.category_symbol_list_sempred
        self._predicates[68] = self.symbol_list_sempred
        self._predicates[72] = self.expression_list_sempred
        self._predicates[74] = self.typedef_sempred
        self._predicates[81] = self.type_identifier_list_sempred
        self._predicates[87] = self.argument_list_sempred
        self._predicates[93] = self.any_type_sempred
        self._predicates[94] = self.member_method_declaration_list_sempred
        self._predicates[96] = self.native_member_method_declaration_list_sempred
        self._predicates[101] = self.module_token_sempred
        self._predicates[104] = self.variable_identifier_list_sempred
        self._predicates[106] = self.native_statement_list_sempred
        self._predicates[110] = self.statement_list_sempred
        self._predicates[111] = self.assertion_list_sempred
        self._predicates[112] = self.switch_case_statement_list_sempred
        self._predicates[113] = self.catch_statement_list_sempred
        self._predicates[116] = self.literal_list_literal_sempred
        self._predicates[124] = self.expression_tuple_sempred
        self._predicates[125] = self.dict_entry_list_sempred
        self._predicates[129] = self.assignable_instance_sempred
        self._predicates[130] = self.is_expression_sempred
        self._predicates[132] = self.key_token_sempred
        self._predicates[133] = self.value_token_sempred
        self._predicates[134] = self.symbols_token_sempred
        self._predicates[143] = self.javascript_expression_sempred
        self._predicates[148] = self.javascript_arguments_sempred
        self._predicates[155] = self.python_expression_sempred
        self._predicates[160] = self.python_ordinal_argument_list_sempred
        self._predicates[161] = self.python_named_argument_list_sempred
        self._predicates[163] = self.python_identifier_expression_sempred
        self._predicates[167] = self.java_expression_sempred
        self._predicates[172] = self.java_arguments_sempred
        self._predicates[175] = self.java_identifier_expression_sempred
        self._predicates[176] = self.java_class_identifier_expression_sempred
        self._predicates[180] = self.csharp_expression_sempred
        self._predicates[185] = self.csharp_arguments_sempred
        self._predicates[188] = self.csharp_identifier_expression_sempred
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
         

    def attribute_list_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def else_if_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def callable_parent_sempred(self, localctx, predIndex):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx, predIndex):
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
                return self.precpred(self._ctx, 23)
         

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
                return self.precpred(self._ctx, 13)
         

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
                return self.precpred(self._ctx, 4)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 21)
         

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
         

    def declarations_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.precpred(self._ctx, 1)
         

    def native_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.precpred(self._ctx, 1)
         

    def category_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 38:
                return self.precpred(self._ctx, 1)
         

    def symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.precpred(self._ctx, 1)
         

    def expression_list_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 42:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 43:
                return self.precpred(self._ctx, 1)
         

    def type_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 44:
                return self.precpred(self._ctx, 1)
         

    def argument_list_sempred(self, localctx, predIndex):
            if predIndex == 45:
                return self.precpred(self._ctx, 1)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 47:
                return self.precpred(self._ctx, 1)
         

    def member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.precpred(self._ctx, 1)
         

    def native_member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.precpred(self._ctx, 1)
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.isText(localctx.i1,"module")
         

    def variable_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def native_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def statement_list_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def assertion_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def switch_case_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def catch_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def literal_list_literal_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def expression_tuple_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def dict_entry_list_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.willBeAOrAn()
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.isText(localctx.i1,"key")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 67:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 68:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 69:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 70:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 71:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 72:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 73:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 74:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 75:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 76:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 77:
                return self.precpred(self._ctx, 1)
         



