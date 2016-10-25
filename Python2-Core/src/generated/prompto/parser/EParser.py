# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .EParserListener import EParserListener
else:
    from EParserListener import EParserListener
from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\u00ae\u0918\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\3\2\5\2\u01a7\n\2\3\2\3\2\3\2\3\2\3\2\5\2\u01ae\n\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write(u"\3\5\3\5\5\5\u01cc\n\5\3\6\3\6\3\6\3\6\5\6\u01d2\n\6")
        buf.write(u"\3\6\3\6\3\6\5\6\u01d7\n\6\3\6\3\6\3\6\3\6\5\6\u01dd")
        buf.write(u"\n\6\5\6\u01df\n\6\3\6\5\6\u01e2\n\6\3\7\3\7\3\7\3\7")
        buf.write(u"\5\7\u01e8\n\7\3\7\3\7\5\7\u01ec\n\7\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\5\7\u01f7\n\7\3\7\3\7\3\7\3\7\3")
        buf.write(u"\7\3\7\3\7\5\7\u0200\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u020f\n\b\3\b\3\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\5\b\u0218\n\b\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write(u"\u021f\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0229")
        buf.write(u"\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u023f\n")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u0256\n\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write(u"\17\5\17\u0263\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\5\17\u026e\n\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u027c\n\17\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\5\20\u028a\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\5\20\u0298\n\20\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\3\22\7\22\u02aa\n\22\f\22\16\22\u02ad\13\22")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u02b7\n")
        buf.write(u"\23\5\23\u02b9\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write(u"\5\24\u02c2\n\24\3\24\3\24\5\24\u02c6\n\24\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\5\25\u02ce\n\25\3\25\3\25\5\25\u02d2")
        buf.write(u"\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3")
        buf.write(u"\26\5\26\u02de\n\26\3\26\3\26\3\26\5\26\u02e3\n\26\3")
        buf.write(u"\26\3\26\5\26\u02e7\n\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0302")
        buf.write(u"\n\27\3\30\3\30\3\31\3\31\3\31\5\31\u0309\n\31\3\32\3")
        buf.write(u"\32\3\32\5\32\u030e\n\32\3\32\3\32\5\32\u0312\n\32\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0327\n")
        buf.write(u"\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write(u"\3\35\3\35\5\35\u0335\n\35\3\36\3\36\5\36\u0339\n\36")
        buf.write(u"\3\36\5\36\u033c\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(u"\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!")
        buf.write(u"\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u035d\n!\3!\3!\3\"\3\"")
        buf.write(u"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write(u"\5\"\u0370\n\"\3#\3#\3#\3#\3#\5#\u0377\n#\3#\3#\3#\3")
        buf.write(u"#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%")
        buf.write(u"\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0399\n&\3&\3&\3")
        buf.write(u"&\3&\3&\3&\3&\5&\u03a2\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'")
        buf.write(u"\u03b7\n\'\f\'\16\'\u03ba\13\'\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\5)\u03c9\n)\3)\3)\3)\5)\u03ce\n)\3)")
        buf.write(u"\3)\3)\3)\3)\3)\5)\u03d6\n)\3)\3)\3)\3)\3)\3)\3)\5)\u03df")
        buf.write(u"\n)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write(u"*\3*\3*\3*\3*\5*\u03f6\n*\3+\3+\3,\3,\5,\u03fc\n,\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u041a\n-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\7-\u0481\n-\f-\16-\u0484")
        buf.write(u"\13-\3.\3.\3.\3.\3.\7.\u048b\n.\f.\16.\u048e\13.\3/\3")
        buf.write(u"/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write(u"\3\62\3\62\3\62\7\62\u04a0\n\62\f\62\16\62\u04a3\13\62")
        buf.write(u"\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write(u"\63\3\63\3\63\5\63\u04b2\n\63\3\64\3\64\3\64\5\64\u04b7")
        buf.write(u"\n\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\5\66\u04c1")
        buf.write(u"\n\66\3\66\3\66\3\66\5\66\u04c6\n\66\5\66\u04c8\n\66")
        buf.write(u"\3\66\3\66\3\66\3\66\5\66\u04ce\n\66\5\66\u04d0\n\66")
        buf.write(u"\5\66\u04d2\n\66\3\67\3\67\3\67\3\67\38\38\38\38\38\3")
        buf.write(u"9\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\5;\u04ec")
        buf.write(u"\n;\3;\3;\3;\3;\3;\5;\u04f3\n;\3;\5;\u04f6\n;\3;\3;\3")
        buf.write(u";\3;\5;\u04fc\n;\3;\3;\5;\u0500\n;\3;\3;\3;\5;\u0505")
        buf.write(u"\n;\5;\u0507\n;\3<\3<\5<\u050b\n<\3<\3<\3<\3<\3<\3<\5")
        buf.write(u"<\u0513\n<\3=\3=\3=\3=\3=\5=\u051a\n=\5=\u051c\n=\3=")
        buf.write(u"\3=\3=\5=\u0521\n=\5=\u0523\n=\3>\3>\3>\3>\3>\3>\3>\7")
        buf.write(u">\u052c\n>\f>\16>\u052f\13>\3?\3?\3?\3?\3@\3@\3@\3@\3")
        buf.write(u"A\3A\3A\3A\3A\3A\3A\3A\5A\u0541\nA\3B\3B\3B\3B\3C\7C")
        buf.write(u"\u0548\nC\fC\16C\u054b\13C\3D\6D\u054e\nD\rD\16D\u054f")
        buf.write(u"\3E\6E\u0553\nE\rE\16E\u0554\3E\3E\3F\7F\u055a\nF\fF")
        buf.write(u"\16F\u055d\13F\3F\3F\3G\3G\3H\5H\u0564\nH\3H\3H\3H\3")
        buf.write(u"I\3I\3I\3I\7I\u056d\nI\fI\16I\u0570\13I\3J\3J\3J\7J\u0575")
        buf.write(u"\nJ\fJ\16J\u0578\13J\3J\3J\3J\3J\3J\5J\u057f\nJ\3K\3")
        buf.write(u"K\3L\3L\5L\u0585\nL\3M\3M\3M\3M\7M\u058b\nM\fM\16M\u058e")
        buf.write(u"\13M\3N\3N\3N\3N\7N\u0594\nN\fN\16N\u0597\13N\3O\3O\3")
        buf.write(u"O\7O\u059c\nO\fO\16O\u059f\13O\3P\3P\3P\3P\3P\3P\3P\3")
        buf.write(u"P\3P\3P\5P\u05ab\nP\3Q\5Q\u05ae\nQ\3Q\3Q\5Q\u05b2\nQ")
        buf.write(u"\3Q\3Q\3R\5R\u05b7\nR\3R\3R\5R\u05bb\nR\3R\3R\3S\3S\3")
        buf.write(u"S\7S\u05c2\nS\fS\16S\u05c5\13S\3T\3T\3T\3T\3T\3T\3U\3")
        buf.write(u"U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\5U\u05d9\nU\3U\3U\3U")
        buf.write(u"\3U\3U\3U\3U\3U\7U\u05e3\nU\fU\16U\u05e6\13U\3V\3V\5")
        buf.write(u"V\u05ea\nV\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W")
        buf.write(u"\5W\u05fa\nW\3X\3X\3Y\5Y\u05ff\nY\3Y\3Y\3Z\3Z\3[\3[\3")
        buf.write(u"[\5[\u0608\n[\3\\\3\\\3\\\7\\\u060d\n\\\f\\\16\\\u0610")
        buf.write(u"\13\\\3]\3]\5]\u0614\n]\3^\3^\3^\5^\u0619\n^\3_\3_\3")
        buf.write(u"`\3`\3a\3a\3b\3b\3c\3c\3c\7c\u0626\nc\fc\16c\u0629\13")
        buf.write(u"c\3d\3d\5d\u062d\nd\3d\5d\u0630\nd\3e\3e\5e\u0634\ne")
        buf.write(u"\3f\3f\3f\5f\u0639\nf\3g\3g\3g\3h\3h\5h\u0640\nh\3i\3")
        buf.write(u"i\3i\3i\3i\3i\3i\3i\3i\7i\u064b\ni\fi\16i\u064e\13i\3")
        buf.write(u"j\3j\3j\3j\7j\u0654\nj\fj\16j\u0657\13j\3k\3k\3k\3k\3")
        buf.write(u"k\5k\u065e\nk\3l\3l\3l\3l\7l\u0664\nl\fl\16l\u0667\13")
        buf.write(u"l\3m\3m\3m\5m\u066c\nm\3n\3n\3n\3n\3n\3n\3n\3n\3n\3n")
        buf.write(u"\5n\u0678\nn\3o\3o\5o\u067c\no\3p\3p\3p\3p\3p\3p\7p\u0684")
        buf.write(u"\np\fp\16p\u0687\13p\3q\3q\5q\u068b\nq\3r\3r\3r\3r\5")
        buf.write(u"r\u0691\nr\3r\3r\3r\7r\u0696\nr\fr\16r\u0699\13r\3r\3")
        buf.write(u"r\5r\u069d\nr\3s\3s\3s\7s\u06a2\ns\fs\16s\u06a5\13s\3")
        buf.write(u"t\3t\3t\7t\u06aa\nt\ft\16t\u06ad\13t\3u\3u\3u\3u\5u\u06b3")
        buf.write(u"\nu\3v\3v\3w\3w\3w\3w\7w\u06bb\nw\fw\16w\u06be\13w\3")
        buf.write(u"x\3x\3x\3x\3x\3x\3x\3x\3x\3x\5x\u06ca\nx\3y\3y\5y\u06ce")
        buf.write(u"\ny\3y\5y\u06d1\ny\3z\3z\5z\u06d5\nz\3z\5z\u06d8\nz\3")
        buf.write(u"{\3{\3{\3{\7{\u06de\n{\f{\16{\u06e1\13{\3|\3|\3|\3|\7")
        buf.write(u"|\u06e7\n|\f|\16|\u06ea\13|\3}\3}\3}\3}\7}\u06f0\n}\f")
        buf.write(u"}\16}\u06f3\13}\3~\3~\3~\3~\7~\u06f9\n~\f~\16~\u06fc")
        buf.write(u"\13~\3\177\3\177\3\177\3\177\3\177\3\177\3\177\3\177")
        buf.write(u"\3\177\3\177\3\177\3\177\3\177\3\177\5\177\u070c\n\177")
        buf.write(u"\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080")
        buf.write(u"\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080")
        buf.write(u"\5\u0080\u071c\n\u0080\3\u0081\3\u0081\3\u0081\7\u0081")
        buf.write(u"\u0721\n\u0081\f\u0081\16\u0081\u0724\13\u0081\3\u0082")
        buf.write(u"\3\u0082\3\u0082\3\u0082\5\u0082\u072a\n\u0082\3\u0083")
        buf.write(u"\3\u0083\3\u0084\3\u0084\3\u0084\3\u0084\3\u0085\3\u0085")
        buf.write(u"\5\u0085\u0734\n\u0085\3\u0086\3\u0086\3\u0086\3\u0086")
        buf.write(u"\3\u0086\5\u0086\u073b\n\u0086\3\u0087\5\u0087\u073e")
        buf.write(u"\n\u0087\3\u0087\3\u0087\5\u0087\u0742\n\u0087\3\u0087")
        buf.write(u"\3\u0087\3\u0088\5\u0088\u0747\n\u0088\3\u0088\3\u0088")
        buf.write(u"\5\u0088\u074b\n\u0088\3\u0088\3\u0088\3\u0089\3\u0089")
        buf.write(u"\3\u0089\3\u0089\3\u0089\7\u0089\u0754\n\u0089\f\u0089")
        buf.write(u"\16\u0089\u0757\13\u0089\5\u0089\u0759\n\u0089\3\u008a")
        buf.write(u"\3\u008a\3\u008a\7\u008a\u075e\n\u008a\f\u008a\16\u008a")
        buf.write(u"\u0761\13\u008a\3\u008b\3\u008b\3\u008b\3\u008b\3\u008c")
        buf.write(u"\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c")
        buf.write(u"\3\u008c\5\u008c\u0770\n\u008c\3\u008d\3\u008d\3\u008d")
        buf.write(u"\3\u008d\3\u008e\3\u008e\3\u008e\3\u008e\3\u008e\7\u008e")
        buf.write(u"\u077b\n\u008e\f\u008e\16\u008e\u077e\13\u008e\3\u008f")
        buf.write(u"\3\u008f\3\u008f\3\u008f\5\u008f\u0784\n\u008f\3\u0090")
        buf.write(u"\3\u0090\3\u0090\7\u0090\u0789\n\u0090\f\u0090\16\u0090")
        buf.write(u"\u078c\13\u0090\3\u0091\3\u0091\3\u0091\7\u0091\u0791")
        buf.write(u"\n\u0091\f\u0091\16\u0091\u0794\13\u0091\3\u0091\5\u0091")
        buf.write(u"\u0797\n\u0091\3\u0092\3\u0092\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0092\5\u0092\u079f\n\u0092\3\u0093\3\u0093\3\u0093")
        buf.write(u"\3\u0094\3\u0094\3\u0094\3\u0095\3\u0095\3\u0095\3\u0096")
        buf.write(u"\3\u0096\3\u0096\3\u0097\3\u0097\3\u0097\3\u0098\3\u0098")
        buf.write(u"\3\u0099\3\u0099\3\u009a\3\u009a\3\u009b\3\u009b\3\u009c")
        buf.write(u"\3\u009c\3\u009d\3\u009d\3\u009d\3\u009d\3\u009d\3\u009d")
        buf.write(u"\3\u009d\5\u009d\u07c1\n\u009d\3\u009e\3\u009e\3\u009e")
        buf.write(u"\3\u009e\3\u009e\7\u009e\u07c8\n\u009e\f\u009e\16\u009e")
        buf.write(u"\u07cb\13\u009e\3\u009f\3\u009f\3\u009f\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\5\u009f\u07d4\n\u009f\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a1\3\u00a1\3\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2")
        buf.write(u"\3\u00a2\5\u00a2\u07e0\n\u00a2\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\5\u00a3\u07e5\n\u00a3\3\u00a3\3\u00a3\3\u00a4\3\u00a4")
        buf.write(u"\3\u00a4\3\u00a4\3\u00a4\3\u00a4\7\u00a4\u07ef\n\u00a4")
        buf.write(u"\f\u00a4\16\u00a4\u07f2\13\u00a4\3\u00a5\3\u00a5\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8\5\u00a8\u0803")
        buf.write(u"\n\u00a8\3\u00a9\3\u00a9\3\u00aa\3\u00aa\3\u00aa\5\u00aa")
        buf.write(u"\u080a\n\u00aa\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab")
        buf.write(u"\7\u00ab\u0811\n\u00ab\f\u00ab\16\u00ab\u0814\13\u00ab")
        buf.write(u"\3\u00ac\3\u00ac\3\u00ac\3\u00ac\5\u00ac\u081a\n\u00ac")
        buf.write(u"\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\5\u00ad")
        buf.write(u"\u0822\n\u00ad\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u0827")
        buf.write(u"\n\u00ae\3\u00ae\3\u00ae\3\u00af\3\u00af\3\u00af\3\u00af")
        buf.write(u"\3\u00af\3\u00af\5\u00af\u0831\n\u00af\3\u00b0\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b0\3\u00b0\7\u00b0\u0839\n\u00b0")
        buf.write(u"\f\u00b0\16\u00b0\u083c\13\u00b0\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\7\u00b1\u0849\n\u00b1\f\u00b1\16\u00b1\u084c")
        buf.write(u"\13\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b3\3\u00b3")
        buf.write(u"\3\u00b3\5\u00b3\u0855\n\u00b3\3\u00b3\3\u00b3\3\u00b3")
        buf.write(u"\7\u00b3\u085a\n\u00b3\f\u00b3\16\u00b3\u085d\13\u00b3")
        buf.write(u"\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\5\u00b4\u0864")
        buf.write(u"\n\u00b4\3\u00b5\3\u00b5\3\u00b6\3\u00b6\3\u00b6\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\5\u00b6\u086f\n\u00b6\3\u00b7")
        buf.write(u"\3\u00b7\3\u00b7\3\u00b7\3\u00b7\7\u00b7\u0876\n\u00b7")
        buf.write(u"\f\u00b7\16\u00b7\u0879\13\u00b7\3\u00b8\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b8\3\u00b8\5\u00b8\u0880\n\u00b8\3\u00b9\3\u00b9")
        buf.write(u"\3\u00ba\3\u00ba\3\u00ba\3\u00bb\3\u00bb\3\u00bb\5\u00bb")
        buf.write(u"\u088a\n\u00bb\3\u00bc\3\u00bc\3\u00bc\5\u00bc\u088f")
        buf.write(u"\n\u00bc\3\u00bc\3\u00bc\3\u00bd\3\u00bd\3\u00bd\3\u00bd")
        buf.write(u"\3\u00bd\3\u00bd\7\u00bd\u0899\n\u00bd\f\u00bd\16\u00bd")
        buf.write(u"\u089c\13\u00bd\3\u00be\3\u00be\3\u00be\3\u00be\3\u00bf")
        buf.write(u"\3\u00bf\3\u00bf\3\u00bf\3\u00c0\3\u00c0\3\u00c0\3\u00c0")
        buf.write(u"\3\u00c0\3\u00c0\7\u00c0\u08ac\n\u00c0\f\u00c0\16\u00c0")
        buf.write(u"\u08af\13\u00c0\3\u00c1\3\u00c1\3\u00c1\3\u00c1\3\u00c1")
        buf.write(u"\7\u00c1\u08b6\n\u00c1\f\u00c1\16\u00c1\u08b9\13\u00c1")
        buf.write(u"\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\5\u00c2\u08c0")
        buf.write(u"\n\u00c2\3\u00c3\3\u00c3\3\u00c4\3\u00c4\3\u00c4\3\u00c4")
        buf.write(u"\3\u00c4\3\u00c4\3\u00c4\5\u00c4\u08cb\n\u00c4\3\u00c5")
        buf.write(u"\3\u00c5\3\u00c5\3\u00c5\3\u00c5\7\u00c5\u08d2\n\u00c5")
        buf.write(u"\f\u00c5\16\u00c5\u08d5\13\u00c5\3\u00c6\3\u00c6\3\u00c6")
        buf.write(u"\3\u00c6\3\u00c6\5\u00c6\u08dc\n\u00c6\3\u00c7\3\u00c7")
        buf.write(u"\3\u00c8\3\u00c8\3\u00c8\3\u00c9\3\u00c9\3\u00c9\5\u00c9")
        buf.write(u"\u08e6\n\u00c9\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u08eb")
        buf.write(u"\n\u00ca\3\u00ca\3\u00ca\3\u00cb\3\u00cb\3\u00cb\3\u00cb")
        buf.write(u"\3\u00cb\3\u00cb\7\u00cb\u08f5\n\u00cb\f\u00cb\16\u00cb")
        buf.write(u"\u08f8\13\u00cb\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cd")
        buf.write(u"\3\u00cd\3\u00cd\3\u00cd\3\u00ce\3\u00ce\3\u00ce\5\u00ce")
        buf.write(u"\u0905\n\u00ce\3\u00ce\3\u00ce\3\u00ce\7\u00ce\u090a")
        buf.write(u"\n\u00ce\f\u00ce\16\u00ce\u090d\13\u00ce\3\u00cf\3\u00cf")
        buf.write(u"\3\u00cf\3\u00cf\3\u00cf\5\u00cf\u0914\n\u00cf\3\u00d0")
        buf.write(u"\3\u00d0\3\u00d0\2\30\"LXZbz\u00a8\u00d0\u011a\u013a")
        buf.write(u"\u0146\u0154\u015e\u0160\u0164\u016c\u0178\u017e\u0180")
        buf.write(u"\u0188\u0194\u019a\u00d1\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write(u"\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`")
        buf.write(u"bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write(u"\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e")
        buf.write(u"\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0")
        buf.write(u"\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2")
        buf.write(u"\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4")
        buf.write(u"\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2\u00e4\u00e6")
        buf.write(u"\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8")
        buf.write(u"\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106\u0108\u010a")
        buf.write(u"\u010c\u010e\u0110\u0112\u0114\u0116\u0118\u011a\u011c")
        buf.write(u"\u011e\u0120\u0122\u0124\u0126\u0128\u012a\u012c\u012e")
        buf.write(u"\u0130\u0132\u0134\u0136\u0138\u013a\u013c\u013e\u0140")
        buf.write(u"\u0142\u0144\u0146\u0148\u014a\u014c\u014e\u0150\u0152")
        buf.write(u"\u0154\u0156\u0158\u015a\u015c\u015e\u0160\u0162\u0164")
        buf.write(u"\u0166\u0168\u016a\u016c\u016e\u0170\u0172\u0174\u0176")
        buf.write(u"\u0178\u017a\u017c\u017e\u0180\u0182\u0184\u0186\u0188")
        buf.write(u"\u018a\u018c\u018e\u0190\u0192\u0194\u0196\u0198\u019a")
        buf.write(u"\u019c\u019e\2\13\3\2\"#\4\2\u008f\u008f\u00a3\u00a3")
        buf.write(u"\4\2\u008b\u008b\u0093\u0093\4\2KK\\\\\4\2\'\'uu\b\2")
        buf.write(u"\64<\u0085\u0085\u0092\u0092\u009c\u009c\u00a1\u00a3")
        buf.write(u"\u00a5\u00a5\b\2\64<\u0085\u0085\u008b\u008b\u0092\u0093")
        buf.write(u"\u009c\u009c\u00a1\u00a3\7\2\64<\u0085\u0085\u0092\u0092")
        buf.write(u"\u009c\u009c\u00a1\u00a5\7\2\64<\u0085\u0085\u0092\u0092")
        buf.write(u"\u009c\u009c\u00a1\u00a3\u099e\2\u01a0\3\2\2\2\4\u01b5")
        buf.write(u"\3\2\2\2\6\u01c1\3\2\2\2\b\u01c7\3\2\2\2\n\u01cd\3\2")
        buf.write(u"\2\2\f\u01e3\3\2\2\2\16\u0201\3\2\2\2\20\u021e\3\2\2")
        buf.write(u"\2\22\u0220\3\2\2\2\24\u0230\3\2\2\2\26\u023a\3\2\2\2")
        buf.write(u"\30\u0247\3\2\2\2\32\u0251\3\2\2\2\34\u025e\3\2\2\2\36")
        buf.write(u"\u027d\3\2\2\2 \u0299\3\2\2\2\"\u02a2\3\2\2\2$\u02b8")
        buf.write(u"\3\2\2\2&\u02ba\3\2\2\2(\u02c7\3\2\2\2*\u02d9\3\2\2\2")
        buf.write(u",\u02ee\3\2\2\2.\u0303\3\2\2\2\60\u0305\3\2\2\2\62\u030a")
        buf.write(u"\3\2\2\2\64\u0326\3\2\2\2\66\u0328\3\2\2\28\u0334\3\2")
        buf.write(u"\2\2:\u033b\3\2\2\2<\u033d\3\2\2\2>\u0346\3\2\2\2@\u034f")
        buf.write(u"\3\2\2\2B\u036f\3\2\2\2D\u0371\3\2\2\2F\u037f\3\2\2\2")
        buf.write(u"H\u0388\3\2\2\2J\u038f\3\2\2\2L\u03a3\3\2\2\2N\u03bb")
        buf.write(u"\3\2\2\2P\u03be\3\2\2\2R\u03f5\3\2\2\2T\u03f7\3\2\2\2")
        buf.write(u"V\u03f9\3\2\2\2X\u0419\3\2\2\2Z\u0485\3\2\2\2\\\u048f")
        buf.write(u"\3\2\2\2^\u0493\3\2\2\2`\u0498\3\2\2\2b\u049a\3\2\2\2")
        buf.write(u"d\u04b1\3\2\2\2f\u04b3\3\2\2\2h\u04b8\3\2\2\2j\u04d1")
        buf.write(u"\3\2\2\2l\u04d3\3\2\2\2n\u04d7\3\2\2\2p\u04dc\3\2\2\2")
        buf.write(u"r\u04e0\3\2\2\2t\u0506\3\2\2\2v\u0508\3\2\2\2x\u0522")
        buf.write(u"\3\2\2\2z\u0524\3\2\2\2|\u0530\3\2\2\2~\u0534\3\2\2\2")
        buf.write(u"\u0080\u0540\3\2\2\2\u0082\u0542\3\2\2\2\u0084\u0549")
        buf.write(u"\3\2\2\2\u0086\u054d\3\2\2\2\u0088\u0552\3\2\2\2\u008a")
        buf.write(u"\u055b\3\2\2\2\u008c\u0560\3\2\2\2\u008e\u0563\3\2\2")
        buf.write(u"\2\u0090\u0568\3\2\2\2\u0092\u0576\3\2\2\2\u0094\u0580")
        buf.write(u"\3\2\2\2\u0096\u0584\3\2\2\2\u0098\u0586\3\2\2\2\u009a")
        buf.write(u"\u058f\3\2\2\2\u009c\u0598\3\2\2\2\u009e\u05aa\3\2\2")
        buf.write(u"\2\u00a0\u05ad\3\2\2\2\u00a2\u05b6\3\2\2\2\u00a4\u05be")
        buf.write(u"\3\2\2\2\u00a6\u05c6\3\2\2\2\u00a8\u05d8\3\2\2\2\u00aa")
        buf.write(u"\u05e9\3\2\2\2\u00ac\u05f9\3\2\2\2\u00ae\u05fb\3\2\2")
        buf.write(u"\2\u00b0\u05fe\3\2\2\2\u00b2\u0602\3\2\2\2\u00b4\u0607")
        buf.write(u"\3\2\2\2\u00b6\u0609\3\2\2\2\u00b8\u0613\3\2\2\2\u00ba")
        buf.write(u"\u0618\3\2\2\2\u00bc\u061a\3\2\2\2\u00be\u061c\3\2\2")
        buf.write(u"\2\u00c0\u061e\3\2\2\2\u00c2\u0620\3\2\2\2\u00c4\u0622")
        buf.write(u"\3\2\2\2\u00c6\u062f\3\2\2\2\u00c8\u0633\3\2\2\2\u00ca")
        buf.write(u"\u0635\3\2\2\2\u00cc\u063a\3\2\2\2\u00ce\u063f\3\2\2")
        buf.write(u"\2\u00d0\u0641\3\2\2\2\u00d2\u064f\3\2\2\2\u00d4\u065d")
        buf.write(u"\3\2\2\2\u00d6\u065f\3\2\2\2\u00d8\u066b\3\2\2\2\u00da")
        buf.write(u"\u0677\3\2\2\2\u00dc\u0679\3\2\2\2\u00de\u067d\3\2\2")
        buf.write(u"\2\u00e0\u0688\3\2\2\2\u00e2\u068c\3\2\2\2\u00e4\u069e")
        buf.write(u"\3\2\2\2\u00e6\u06a6\3\2\2\2\u00e8\u06b2\3\2\2\2\u00ea")
        buf.write(u"\u06b4\3\2\2\2\u00ec\u06b6\3\2\2\2\u00ee\u06c9\3\2\2")
        buf.write(u"\2\u00f0\u06cb\3\2\2\2\u00f2\u06d2\3\2\2\2\u00f4\u06d9")
        buf.write(u"\3\2\2\2\u00f6\u06e2\3\2\2\2\u00f8\u06eb\3\2\2\2\u00fa")
        buf.write(u"\u06f4\3\2\2\2\u00fc\u070b\3\2\2\2\u00fe\u071b\3\2\2")
        buf.write(u"\2\u0100\u071d\3\2\2\2\u0102\u0729\3\2\2\2\u0104\u072b")
        buf.write(u"\3\2\2\2\u0106\u072d\3\2\2\2\u0108\u0733\3\2\2\2\u010a")
        buf.write(u"\u073a\3\2\2\2\u010c\u073d\3\2\2\2\u010e\u0746\3\2\2")
        buf.write(u"\2\u0110\u074e\3\2\2\2\u0112\u075a\3\2\2\2\u0114\u0762")
        buf.write(u"\3\2\2\2\u0116\u076f\3\2\2\2\u0118\u0771\3\2\2\2\u011a")
        buf.write(u"\u0775\3\2\2\2\u011c\u0783\3\2\2\2\u011e\u0785\3\2\2")
        buf.write(u"\2\u0120\u078d\3\2\2\2\u0122\u079e\3\2\2\2\u0124\u07a0")
        buf.write(u"\3\2\2\2\u0126\u07a3\3\2\2\2\u0128\u07a6\3\2\2\2\u012a")
        buf.write(u"\u07a9\3\2\2\2\u012c\u07ac\3\2\2\2\u012e\u07af\3\2\2")
        buf.write(u"\2\u0130\u07b1\3\2\2\2\u0132\u07b3\3\2\2\2\u0134\u07b5")
        buf.write(u"\3\2\2\2\u0136\u07b7\3\2\2\2\u0138\u07c0\3\2\2\2\u013a")
        buf.write(u"\u07c2\3\2\2\2\u013c\u07d3\3\2\2\2\u013e\u07d5\3\2\2")
        buf.write(u"\2\u0140\u07d7\3\2\2\2\u0142\u07df\3\2\2\2\u0144\u07e1")
        buf.write(u"\3\2\2\2\u0146\u07e8\3\2\2\2\u0148\u07f3\3\2\2\2\u014a")
        buf.write(u"\u07f7\3\2\2\2\u014c\u07fb\3\2\2\2\u014e\u0802\3\2\2")
        buf.write(u"\2\u0150\u0804\3\2\2\2\u0152\u0809\3\2\2\2\u0154\u080b")
        buf.write(u"\3\2\2\2\u0156\u0819\3\2\2\2\u0158\u0821\3\2\2\2\u015a")
        buf.write(u"\u0823\3\2\2\2\u015c\u0830\3\2\2\2\u015e\u0832\3\2\2")
        buf.write(u"\2\u0160\u083d\3\2\2\2\u0162\u084d\3\2\2\2\u0164\u0854")
        buf.write(u"\3\2\2\2\u0166\u0863\3\2\2\2\u0168\u0865\3\2\2\2\u016a")
        buf.write(u"\u086e\3\2\2\2\u016c\u0870\3\2\2\2\u016e\u087f\3\2\2")
        buf.write(u"\2\u0170\u0881\3\2\2\2\u0172\u0883\3\2\2\2\u0174\u0889")
        buf.write(u"\3\2\2\2\u0176\u088b\3\2\2\2\u0178\u0892\3\2\2\2\u017a")
        buf.write(u"\u089d\3\2\2\2\u017c\u08a1\3\2\2\2\u017e\u08a5\3\2\2")
        buf.write(u"\2\u0180\u08b0\3\2\2\2\u0182\u08bf\3\2\2\2\u0184\u08c1")
        buf.write(u"\3\2\2\2\u0186\u08ca\3\2\2\2\u0188\u08cc\3\2\2\2\u018a")
        buf.write(u"\u08db\3\2\2\2\u018c\u08dd\3\2\2\2\u018e\u08df\3\2\2")
        buf.write(u"\2\u0190\u08e5\3\2\2\2\u0192\u08e7\3\2\2\2\u0194\u08ee")
        buf.write(u"\3\2\2\2\u0196\u08f9\3\2\2\2\u0198\u08fd\3\2\2\2\u019a")
        buf.write(u"\u0904\3\2\2\2\u019c\u0913\3\2\2\2\u019e\u0915\3\2\2")
        buf.write(u"\2\u01a0\u01a1\7Z\2\2\u01a1\u01a2\5\u00c0a\2\u01a2\u01a3")
        buf.write(u"\7J\2\2\u01a3\u01a6\7b\2\2\u01a4\u01a7\7T\2\2\u01a5\u01a7")
        buf.write(u"\5\u00c0a\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write(u"\u01ad\3\2\2\2\u01a8\u01a9\5$\23\2\u01a9\u01aa\7\23\2")
        buf.write(u"\2\u01aa\u01ab\7H\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01ae")
        buf.write(u"\7\u0098\2\2\u01ad\u01a8\3\2\2\2\u01ad\u01ac\3\2\2\2")
        buf.write(u"\u01ae\u01af\3\2\2\2\u01af\u01b0\5\u012c\u0097\2\u01b0")
        buf.write(u"\u01b1\7\21\2\2\u01b1\u01b2\5\u0088E\2\u01b2\u01b3\5")
        buf.write(u"\u009aN\2\u01b3\u01b4\5\u008aF\2\u01b4\3\3\2\2\2\u01b5")
        buf.write(u"\u01b6\7Z\2\2\u01b6\u01b7\5\u00c0a\2\u01b7\u01b8\7J\2")
        buf.write(u"\2\u01b8\u01b9\7b\2\2\u01b9\u01ba\5\u00acW\2\u01ba\u01bb")
        buf.write(u"\7\u0098\2\2\u01bb\u01bc\5\u012c\u0097\2\u01bc\u01bd")
        buf.write(u"\7\21\2\2\u01bd\u01be\5\u0088E\2\u01be\u01bf\5\u0098")
        buf.write(u"M\2\u01bf\u01c0\5\u008aF\2\u01c0\5\3\2\2\2\u01c1\u01c2")
        buf.write(u"\5\u00c2b\2\u01c2\u01c3\7\u0098\2\2\u01c3\u01c4\5X-\2")
        buf.write(u"\u01c4\u01c5\7J\2\2\u01c5\u01c6\5\u012a\u0096\2\u01c6")
        buf.write(u"\7\3\2\2\2\u01c7\u01c8\5\u00c2b\2\u01c8\u01cb\5z>\2\u01c9")
        buf.write(u"\u01ca\7H\2\2\u01ca\u01cc\5|?\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write(u"\u01cc\3\2\2\2\u01cc\t\3\2\2\2\u01cd\u01ce\7Z\2\2\u01ce")
        buf.write(u"\u01cf\5\u00be`\2\u01cf\u01d1\7J\2\2\u01d0\u01d2\7\u008f")
        buf.write(u"\2\2\u01d1\u01d0\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3")
        buf.write(u"\3\2\2\2\u01d3\u01d4\5\u00a8U\2\u01d4\u01d6\7M\2\2\u01d5")
        buf.write(u"\u01d7\5\u009eP\2\u01d6\u01d5\3\2\2\2\u01d6\u01d7\3\2")
        buf.write(u"\2\2\u01d7\u01e1\3\2\2\2\u01d8\u01de\7\u0098\2\2\u01d9")
        buf.write(u"\u01dc\5\u00e4s\2\u01da\u01db\7H\2\2\u01db\u01dd\5\u00bc")
        buf.write(u"_\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df")
        buf.write(u"\3\2\2\2\u01de\u01d9\3\2\2\2\u01de\u01df\3\2\2\2\u01df")
        buf.write(u"\u01e0\3\2\2\2\u01e0\u01e2\7o\2\2\u01e1\u01d8\3\2\2\2")
        buf.write(u"\u01e1\u01e2\3\2\2\2\u01e2\13\3\2\2\2\u01e3\u01e4\7Z")
        buf.write(u"\2\2\u01e4\u01e5\5\u00c0a\2\u01e5\u01e7\7J\2\2\u01e6")
        buf.write(u"\u01e8\7\u008f\2\2\u01e7\u01e6\3\2\2\2\u01e7\u01e8\3")
        buf.write(u"\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01ec\7T\2\2\u01ea\u01ec")
        buf.write(u"\5\20\t\2\u01eb\u01e9\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write(u"\u01ff\3\2\2\2\u01ed\u01f6\5$\23\2\u01ee\u01ef\7\23\2")
        buf.write(u"\2\u01ef\u01f0\7H\2\2\u01f0\u01f1\7t\2\2\u01f1\u01f2")
        buf.write(u"\7\21\2\2\u01f2\u01f3\5\u0088E\2\u01f3\u01f4\5\u00d2")
        buf.write(u"j\2\u01f4\u01f5\5\u008aF\2\u01f5\u01f7\3\2\2\2\u01f6")
        buf.write(u"\u01ee\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u0200\3\2\2")
        buf.write(u"\2\u01f8\u01f9\7\u0098\2\2\u01f9\u01fa\7t\2\2\u01fa\u01fb")
        buf.write(u"\7\21\2\2\u01fb\u01fc\5\u0088E\2\u01fc\u01fd\5\u00d2")
        buf.write(u"j\2\u01fd\u01fe\5\u008aF\2\u01fe\u0200\3\2\2\2\u01ff")
        buf.write(u"\u01ed\3\2\2\2\u01ff\u01f8\3\2\2\2\u01ff\u0200\3\2\2")
        buf.write(u"\2\u0200\r\3\2\2\2\u0201\u0202\7Z\2\2\u0202\u0203\5\u00c0")
        buf.write(u"a\2\u0203\u0204\7J\2\2\u0204\u0217\7\u008d\2\2\u0205")
        buf.write(u"\u020e\5$\23\2\u0206\u0207\7\23\2\2\u0207\u0208\7H\2")
        buf.write(u"\2\u0208\u0209\7t\2\2\u0209\u020a\7\21\2\2\u020a\u020b")
        buf.write(u"\5\u0088E\2\u020b\u020c\5\u00d2j\2\u020c\u020d\5\u008a")
        buf.write(u"F\2\u020d\u020f\3\2\2\2\u020e\u0206\3\2\2\2\u020e\u020f")
        buf.write(u"\3\2\2\2\u020f\u0218\3\2\2\2\u0210\u0211\7\u0098\2\2")
        buf.write(u"\u0211\u0212\7t\2\2\u0212\u0213\7\21\2\2\u0213\u0214")
        buf.write(u"\5\u0088E\2\u0214\u0215\5\u00d2j\2\u0215\u0216\5\u008a")
        buf.write(u"F\2\u0216\u0218\3\2\2\2\u0217\u0205\3\2\2\2\u0217\u0210")
        buf.write(u"\3\2\2\2\u0217\u0218\3\2\2\2\u0218\17\3\2\2\2\u0219\u021f")
        buf.write(u"\5\u00b6\\\2\u021a\u021b\5\u00b6\\\2\u021b\u021c\7H\2")
        buf.write(u"\2\u021c\u021d\5\u00c0a\2\u021d\u021f\3\2\2\2\u021e\u0219")
        buf.write(u"\3\2\2\2\u021e\u021a\3\2\2\2\u021f\21\3\2\2\2\u0220\u0221")
        buf.write(u"\7Z\2\2\u0221\u0222\5\u0122\u0092\2\u0222\u0223\7J\2")
        buf.write(u"\2\u0223\u0224\7\177\2\2\u0224\u0225\7\u0086\2\2\u0225")
        buf.write(u"\u0228\5\u00c8e\2\u0226\u0227\7\u0089\2\2\u0227\u0229")
        buf.write(u"\5\u00a8U\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write(u"\u022a\3\2\2\2\u022a\u022b\7^\2\2\u022b\u022c\7\21\2")
        buf.write(u"\2\u022c\u022d\5\u0088E\2\u022d\u022e\5\u00f4{\2\u022e")
        buf.write(u"\u022f\5\u008aF\2\u022f\23\3\2\2\2\u0230\u0231\7Z\2\2")
        buf.write(u"\u0231\u0232\5\u00bc_\2\u0232\u0233\7J\2\2\u0233\u0234")
        buf.write(u"\7\u008c\2\2\u0234\u0235\7^\2\2\u0235\u0236\7\21\2\2")
        buf.write(u"\u0236\u0237\5\u0088E\2\u0237\u0238\5\u00f4{\2\u0238")
        buf.write(u"\u0239\5\u008aF\2\u0239\25\3\2\2\2\u023a\u023b\7Z\2\2")
        buf.write(u"\u023b\u023c\5\u00bc_\2\u023c\u023e\7J\2\2\u023d\u023f")
        buf.write(u"\7w\2\2\u023e\u023d\3\2\2\2\u023e\u023f\3\2\2\2\u023f")
        buf.write(u"\u0240\3\2\2\2\u0240\u0241\7\u008c\2\2\u0241\u0242\7")
        buf.write(u"^\2\2\u0242\u0243\7\21\2\2\u0243\u0244\5\u0088E\2\u0244")
        buf.write(u"\u0245\5\u00ecw\2\u0245\u0246\5\u008aF\2\u0246\27\3\2")
        buf.write(u"\2\2\u0247\u0248\7Z\2\2\u0248\u0249\5\u00bc_\2\u0249")
        buf.write(u"\u024a\7J\2\2\u024a\u024b\7l\2\2\u024b\u024c\7^\2\2\u024c")
        buf.write(u"\u024d\7\21\2\2\u024d\u024e\5\u0088E\2\u024e\u024f\5")
        buf.write(u"\u00f4{\2\u024f\u0250\5\u008aF\2\u0250\31\3\2\2\2\u0251")
        buf.write(u"\u0252\7Z\2\2\u0252\u0253\5\u00bc_\2\u0253\u0255\7J\2")
        buf.write(u"\2\u0254\u0256\7w\2\2\u0255\u0254\3\2\2\2\u0255\u0256")
        buf.write(u"\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258\7l\2\2\u0258")
        buf.write(u"\u0259\7^\2\2\u0259\u025a\7\21\2\2\u025a\u025b\5\u0088")
        buf.write(u"E\2\u025b\u025c\5\u00ecw\2\u025c\u025d\5\u008aF\2\u025d")
        buf.write(u"\33\3\2\2\2\u025e\u025f\7Z\2\2\u025f\u0260\5\u00c0a\2")
        buf.write(u"\u0260\u0262\7J\2\2\u0261\u0263\7\u008f\2\2\u0262\u0261")
        buf.write(u"\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0264\3\2\2\2\u0264")
        buf.write(u"\u0265\7w\2\2\u0265\u026d\7T\2\2\u0266\u0267\5$\23\2")
        buf.write(u"\u0267\u0268\7\23\2\2\u0268\u0269\7H\2\2\u0269\u026a")
        buf.write(u"\7O\2\2\u026a\u026e\3\2\2\2\u026b\u026c\7\u0098\2\2\u026c")
        buf.write(u"\u026e\7O\2\2\u026d\u0266\3\2\2\2\u026d\u026b\3\2\2\2")
        buf.write(u"\u026e\u026f\3\2\2\2\u026f\u0270\7\21\2\2\u0270\u0271")
        buf.write(u"\5\u0088E\2\u0271\u0272\5 \21\2\u0272\u027b\5\u008aF")
        buf.write(u"\2\u0273\u0274\5\u0086D\2\u0274\u0275\7H\2\2\u0275\u0276")
        buf.write(u"\7t\2\2\u0276\u0277\7\21\2\2\u0277\u0278\5\u0088E\2\u0278")
        buf.write(u"\u0279\5\u00d6l\2\u0279\u027a\5\u008aF\2\u027a\u027c")
        buf.write(u"\3\2\2\2\u027b\u0273\3\2\2\2\u027b\u027c\3\2\2\2\u027c")
        buf.write(u"\35\3\2\2\2\u027d\u027e\7Z\2\2\u027e\u027f\5\u00c0a\2")
        buf.write(u"\u027f\u0280\7J\2\2\u0280\u0281\7w\2\2\u0281\u0289\7")
        buf.write(u"\u0087\2\2\u0282\u0283\5$\23\2\u0283\u0284\7\23\2\2\u0284")
        buf.write(u"\u0285\7H\2\2\u0285\u0286\7O\2\2\u0286\u028a\3\2\2\2")
        buf.write(u"\u0287\u0288\7\u0098\2\2\u0288\u028a\7O\2\2\u0289\u0282")
        buf.write(u"\3\2\2\2\u0289\u0287\3\2\2\2\u028a\u028b\3\2\2\2\u028b")
        buf.write(u"\u028c\7\21\2\2\u028c\u028d\5\u0088E\2\u028d\u028e\5")
        buf.write(u" \21\2\u028e\u0297\5\u008aF\2\u028f\u0290\5\u0086D\2")
        buf.write(u"\u0290\u0291\7H\2\2\u0291\u0292\7t\2\2\u0292\u0293\7")
        buf.write(u"\21\2\2\u0293\u0294\5\u0088E\2\u0294\u0295\5\u00d6l\2")
        buf.write(u"\u0295\u0296\5\u008aF\2\u0296\u0298\3\2\2\2\u0297\u028f")
        buf.write(u"\3\2\2\2\u0297\u0298\3\2\2\2\u0298\37\3\2\2\2\u0299\u029a")
        buf.write(u"\7Z\2\2\u029a\u029b\7T\2\2\u029b\u029c\7O\2\2\u029c\u029d")
        buf.write(u"\7J\2\2\u029d\u029e\7\21\2\2\u029e\u029f\5\u0088E\2\u029f")
        buf.write(u"\u02a0\5\"\22\2\u02a0\u02a1\5\u008aF\2\u02a1!\3\2\2\2")
        buf.write(u"\u02a2\u02a3\b\22\1\2\u02a3\u02a4\5\u00dan\2\u02a4\u02ab")
        buf.write(u"\3\2\2\2\u02a5\u02a6\f\3\2\2\u02a6\u02a7\5\u0086D\2\u02a7")
        buf.write(u"\u02a8\5\u00dan\2\u02a8\u02aa\3\2\2\2\u02a9\u02a5\3\2")
        buf.write(u"\2\2\u02aa\u02ad\3\2\2\2\u02ab\u02a9\3\2\2\2\u02ab\u02ac")
        buf.write(u"\3\2\2\2\u02ac#\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ae\u02af")
        buf.write(u"\7\u0098\2\2\u02af\u02b0\7M\2\2\u02b0\u02b9\5\u00be`")
        buf.write(u"\2\u02b1\u02b2\7\u0098\2\2\u02b2\u02b3\7N\2\2\u02b3\u02b6")
        buf.write(u"\5\u00e6t\2\u02b4\u02b5\7H\2\2\u02b5\u02b7\5\u00be`\2")
        buf.write(u"\u02b6\u02b4\3\2\2\2\u02b6\u02b7\3\2\2\2\u02b7\u02b9")
        buf.write(u"\3\2\2\2\u02b8\u02ae\3\2\2\2\u02b8\u02b1\3\2\2\2\u02b9")
        buf.write(u"%\3\2\2\2\u02ba\u02bb\7Z\2\2\u02bb\u02bc\5\u00b8]\2\u02bc")
        buf.write(u"\u02bd\7J\2\2\u02bd\u02be\7E\2\2\u02be\u02c1\7s\2\2\u02bf")
        buf.write(u"\u02c0\7\u0086\2\2\u02c0\u02c2\5\60\31\2\u02c1\u02bf")
        buf.write(u"\3\2\2\2\u02c1\u02c2\3\2\2\2\u02c2\u02c5\3\2\2\2\u02c3")
        buf.write(u"\u02c4\7\u0089\2\2\u02c4\u02c6\5\u00a8U\2\u02c5\u02c3")
        buf.write(u"\3\2\2\2\u02c5\u02c6\3\2\2\2\u02c6\'\3\2\2\2\u02c7\u02c8")
        buf.write(u"\7Z\2\2\u02c8\u02c9\5\u00b8]\2\u02c9\u02ca\7J\2\2\u02ca")
        buf.write(u"\u02cd\7s\2\2\u02cb\u02cc\7\u0086\2\2\u02cc\u02ce\5\60")
        buf.write(u"\31\2\u02cd\u02cb\3\2\2\2\u02cd\u02ce\3\2\2\2\u02ce\u02d1")
        buf.write(u"\3\2\2\2\u02cf\u02d0\7\u0089\2\2\u02d0\u02d2\5\u00a8")
        buf.write(u"U\2\u02d1\u02cf\3\2\2\2\u02d1\u02d2\3\2\2\2\u02d2\u02d3")
        buf.write(u"\3\2\2\2\u02d3\u02d4\7^\2\2\u02d4\u02d5\7\21\2\2\u02d5")
        buf.write(u"\u02d6\5\u0088E\2\u02d6\u02d7\5\u00f4{\2\u02d7\u02d8")
        buf.write(u"\5\u008aF\2\u02d8)\3\2\2\2\u02d9\u02da\7Z\2\2\u02da\u02db")
        buf.write(u"\5\u00b8]\2\u02db\u02dd\7J\2\2\u02dc\u02de\7w\2\2\u02dd")
        buf.write(u"\u02dc\3\2\2\2\u02dd\u02de\3\2\2\2\u02de\u02df\3\2\2")
        buf.write(u"\2\u02df\u02e2\7s\2\2\u02e0\u02e1\7\u0086\2\2\u02e1\u02e3")
        buf.write(u"\5\60\31\2\u02e2\u02e0\3\2\2\2\u02e2\u02e3\3\2\2\2\u02e3")
        buf.write(u"\u02e6\3\2\2\2\u02e4\u02e5\7\u0089\2\2\u02e5\u02e7\5")
        buf.write(u"\u00ceh\2\u02e6\u02e4\3\2\2\2\u02e6\u02e7\3\2\2\2\u02e7")
        buf.write(u"\u02e8\3\2\2\2\u02e8\u02e9\7^\2\2\u02e9\u02ea\7\21\2")
        buf.write(u"\2\u02ea\u02eb\5\u0088E\2\u02eb\u02ec\5\u00ecw\2\u02ec")
        buf.write(u"\u02ed\5\u008aF\2\u02ed+\3\2\2\2\u02ee\u02ef\7Z\2\2\u02ef")
        buf.write(u"\u02f0\7\u00a6\2\2\u02f0\u02f1\7J\2\2\u02f1\u02f2\7\u0092")
        buf.write(u"\2\2\u02f2\u02f3\7s\2\2\u02f3\u02f4\7^\2\2\u02f4\u02f5")
        buf.write(u"\7\21\2\2\u02f5\u02f6\5\u0088E\2\u02f6\u02f7\5\u00f4")
        buf.write(u"{\2\u02f7\u02f8\5\u008aF\2\u02f8\u02f9\5\u0086D\2\u02f9")
        buf.write(u"\u02fa\7H\2\2\u02fa\u0301\7\u0097\2\2\u02fb\u02fc\7\21")
        buf.write(u"\2\2\u02fc\u02fd\5\u0088E\2\u02fd\u02fe\5\u00f6|\2\u02fe")
        buf.write(u"\u02ff\5\u008aF\2\u02ff\u0302\3\2\2\2\u0300\u0302\5\u00c2")
        buf.write(u"b\2\u0301\u02fb\3\2\2\2\u0301\u0300\3\2\2\2\u0302-\3")
        buf.write(u"\2\2\2\u0303\u0304\5X-\2\u0304/\3\2\2\2\u0305\u0308\5")
        buf.write(u"\u00c4c\2\u0306\u0307\7H\2\2\u0307\u0309\5\u00c6d\2\u0308")
        buf.write(u"\u0306\3\2\2\2\u0308\u0309\3\2\2\2\u0309\61\3\2\2\2\u030a")
        buf.write(u"\u030b\5\u00ceh\2\u030b\u030d\5\u00bc_\2\u030c\u030e")
        buf.write(u"\5$\23\2\u030d\u030c\3\2\2\2\u030d\u030e\3\2\2\2\u030e")
        buf.write(u"\u0311\3\2\2\2\u030f\u0310\7-\2\2\u0310\u0312\5\u0108")
        buf.write(u"\u0085\2\u0311\u030f\3\2\2\2\u0311\u0312\3\2\2\2\u0312")
        buf.write(u"\63\3\2\2\2\u0313\u0327\5~@\2\u0314\u0327\5:\36\2\u0315")
        buf.write(u"\u0327\5\u0082B\2\u0316\u0327\58\35\2\u0317\u0327\5\66")
        buf.write(u"\34\2\u0318\u0327\5T+\2\u0319\u0327\5V,\2\u031a\u0327")
        buf.write(u"\5J&\2\u031b\u0327\5@!\2\u031c\u0327\5D#\2\u031d\u0327")
        buf.write(u"\5H%\2\u031e\u0327\5F$\2\u031f\u0327\5N(\2\u0320\u0327")
        buf.write(u"\5P)\2\u0321\u0327\5n8\2\u0322\u0327\5<\37\2\u0323\u0327")
        buf.write(u"\5> \2\u0324\u0327\5(\25\2\u0325\u0327\5\u00eav\2\u0326")
        buf.write(u"\u0313\3\2\2\2\u0326\u0314\3\2\2\2\u0326\u0315\3\2\2")
        buf.write(u"\2\u0326\u0316\3\2\2\2\u0326\u0317\3\2\2\2\u0326\u0318")
        buf.write(u"\3\2\2\2\u0326\u0319\3\2\2\2\u0326\u031a\3\2\2\2\u0326")
        buf.write(u"\u031b\3\2\2\2\u0326\u031c\3\2\2\2\u0326\u031d\3\2\2")
        buf.write(u"\2\u0326\u031e\3\2\2\2\u0326\u031f\3\2\2\2\u0326\u0320")
        buf.write(u"\3\2\2\2\u0326\u0321\3\2\2\2\u0326\u0322\3\2\2\2\u0326")
        buf.write(u"\u0323\3\2\2\2\u0326\u0324\3\2\2\2\u0326\u0325\3\2\2")
        buf.write(u"\2\u0327\65\3\2\2\2\u0328\u0329\7i\2\2\u0329\67\3\2\2")
        buf.write(u"\2\u032a\u032b\7[\2\2\u032b\u0335\5\u00a4S\2\u032c\u032d")
        buf.write(u"\7\u0090\2\2\u032d\u0335\5\u00a4S\2\u032e\u032f\7[\2")
        buf.write(u"\2\u032f\u0330\5\u00a4S\2\u0330\u0331\7H\2\2\u0331\u0332")
        buf.write(u"\7\u0090\2\2\u0332\u0333\5\u00a4S\2\u0333\u0335\3\2\2")
        buf.write(u"\2\u0334\u032a\3\2\2\2\u0334\u032c\3\2\2\2\u0334\u032e")
        buf.write(u"\3\2\2\2\u03359\3\2\2\2\u0336\u0338\5Z.\2\u0337\u0339")
        buf.write(u"\5x=\2\u0338\u0337\3\2\2\2\u0338\u0339\3\2\2\2\u0339")
        buf.write(u"\u033c\3\2\2\2\u033a\u033c\5^\60\2\u033b\u0336\3\2\2")
        buf.write(u"\2\u033b\u033a\3\2\2\2\u033c;\3\2\2\2\u033d\u033e\7\u0098")
        buf.write(u"\2\2\u033e\u033f\5\u0118\u008d\2\u033f\u0340\7\23\2\2")
        buf.write(u"\u0340\u0341\7]\2\2\u0341\u0342\7\21\2\2\u0342\u0343")
        buf.write(u"\5\u0088E\2\u0343\u0344\5\u00f4{\2\u0344\u0345\5\u008a")
        buf.write(u"F\2\u0345=\3\2\2\2\u0346\u0347\7\u0098\2\2\u0347\u0348")
        buf.write(u"\5\u00c0a\2\u0348\u0349\7\23\2\2\u0349\u034a\7]\2\2\u034a")
        buf.write(u"\u034b\7\21\2\2\u034b\u034c\5\u0088E\2\u034c\u034d\5")
        buf.write(u"\u00f4{\2\u034d\u034e\5\u008aF\2\u034e?\3\2\2\2\u034f")
        buf.write(u"\u0350\7\u0091\2\2\u0350\u0351\7|\2\2\u0351\u0352\5X")
        buf.write(u"-\2\u0352\u0353\7\21\2\2\u0353\u0354\5\u0088E\2\u0354")
        buf.write(u"\u035c\5\u00f8}\2\u0355\u0356\5\u0086D\2\u0356\u0357")
        buf.write(u"\7\u0082\2\2\u0357\u0358\7\21\2\2\u0358\u0359\5\u0088")
        buf.write(u"E\2\u0359\u035a\5\u00f4{\2\u035a\u035b\5\u008aF\2\u035b")
        buf.write(u"\u035d\3\2\2\2\u035c\u0355\3\2\2\2\u035c\u035d\3\2\2")
        buf.write(u"\2\u035d\u035e\3\2\2\2\u035e\u035f\5\u008aF\2\u035fA")
        buf.write(u"\3\2\2\2\u0360\u0361\7\u0099\2\2\u0361\u0362\5\u00fe")
        buf.write(u"\u0080\2\u0362\u0363\7\21\2\2\u0363\u0364\5\u0088E\2")
        buf.write(u"\u0364\u0365\5\u00f4{\2\u0365\u0366\5\u008aF\2\u0366")
        buf.write(u"\u0370\3\2\2\2\u0367\u0368\7\u0099\2\2\u0368\u0369\7")
        buf.write(u"n\2\2\u0369\u036a\5\u00fc\177\2\u036a\u036b\7\21\2\2")
        buf.write(u"\u036b\u036c\5\u0088E\2\u036c\u036d\5\u00f4{\2\u036d")
        buf.write(u"\u036e\5\u008aF\2\u036e\u0370\3\2\2\2\u036f\u0360\3\2")
        buf.write(u"\2\2\u036f\u0367\3\2\2\2\u0370C\3\2\2\2\u0371\u0372\7")
        buf.write(u"j\2\2\u0372\u0373\7_\2\2\u0373\u0376\5\u00bc_\2\u0374")
        buf.write(u"\u0375\7\23\2\2\u0375\u0377\5\u00bc_\2\u0376\u0374\3")
        buf.write(u"\2\2\2\u0376\u0377\3\2\2\2\u0377\u0378\3\2\2\2\u0378")
        buf.write(u"\u0379\7n\2\2\u0379\u037a\5X-\2\u037a\u037b\7\21\2\2")
        buf.write(u"\u037b\u037c\5\u0088E\2\u037c\u037d\5\u00f4{\2\u037d")
        buf.write(u"\u037e\5\u008aF\2\u037eE\3\2\2\2\u037f\u0380\7]\2\2\u0380")
        buf.write(u"\u0381\7\21\2\2\u0381\u0382\5\u0088E\2\u0382\u0383\5")
        buf.write(u"\u00f4{\2\u0383\u0384\5\u008aF\2\u0384\u0385\5\u0086")
        buf.write(u"D\2\u0385\u0386\7\u009b\2\2\u0386\u0387\5X-\2\u0387G")
        buf.write(u"\3\2\2\2\u0388\u0389\7\u009b\2\2\u0389\u038a\5X-\2\u038a")
        buf.write(u"\u038b\7\21\2\2\u038b\u038c\5\u0088E\2\u038c\u038d\5")
        buf.write(u"\u00f4{\2\u038d\u038e\5\u008aF\2\u038eI\3\2\2\2\u038f")
        buf.write(u"\u0390\7m\2\2\u0390\u0391\5X-\2\u0391\u0392\7\21\2\2")
        buf.write(u"\u0392\u0393\5\u0088E\2\u0393\u0394\5\u00f4{\2\u0394")
        buf.write(u"\u0398\5\u008aF\2\u0395\u0396\5\u0086D\2\u0396\u0397")
        buf.write(u"\5L\'\2\u0397\u0399\3\2\2\2\u0398\u0395\3\2\2\2\u0398")
        buf.write(u"\u0399\3\2\2\2\u0399\u03a1\3\2\2\2\u039a\u039b\5\u0086")
        buf.write(u"D\2\u039b\u039c\7`\2\2\u039c\u039d\7\21\2\2\u039d\u039e")
        buf.write(u"\5\u0088E\2\u039e\u039f\5\u00f4{\2\u039f\u03a0\5\u008a")
        buf.write(u"F\2\u03a0\u03a2\3\2\2\2\u03a1\u039a\3\2\2\2\u03a1\u03a2")
        buf.write(u"\3\2\2\2\u03a2K\3\2\2\2\u03a3\u03a4\b\'\1\2\u03a4\u03a5")
        buf.write(u"\7`\2\2\u03a5\u03a6\7m\2\2\u03a6\u03a7\5X-\2\u03a7\u03a8")
        buf.write(u"\7\21\2\2\u03a8\u03a9\5\u0088E\2\u03a9\u03aa\5\u00f4")
        buf.write(u"{\2\u03aa\u03ab\5\u008aF\2\u03ab\u03b8\3\2\2\2\u03ac")
        buf.write(u"\u03ad\f\3\2\2\u03ad\u03ae\5\u0086D\2\u03ae\u03af\7`")
        buf.write(u"\2\2\u03af\u03b0\7m\2\2\u03b0\u03b1\5X-\2\u03b1\u03b2")
        buf.write(u"\7\21\2\2\u03b2\u03b3\5\u0088E\2\u03b3\u03b4\5\u00f4")
        buf.write(u"{\2\u03b4\u03b5\5\u008aF\2\u03b5\u03b7\3\2\2\2\u03b6")
        buf.write(u"\u03ac\3\2\2\2\u03b7\u03ba\3\2\2\2\u03b8\u03b6\3\2\2")
        buf.write(u"\2\u03b8\u03b9\3\2\2\2\u03b9M\3\2\2\2\u03ba\u03b8\3\2")
        buf.write(u"\2\2\u03bb\u03bc\7\u0084\2\2\u03bc\u03bd\5X-\2\u03bd")
        buf.write(u"O\3\2\2\2\u03be\u03bf\7\u0091\2\2\u03bf\u03c0\7|\2\2")
        buf.write(u"\u03c0\u03c1\5\u00bc_\2\u03c1\u03c2\7^\2\2\u03c2\u03c3")
        buf.write(u"\7\21\2\2\u03c3\u03c4\5\u0088E\2\u03c4\u03c5\5\u00f4")
        buf.write(u"{\2\u03c5\u03c6\5\u008aF\2\u03c6\u03c8\5\u0084C\2\u03c7")
        buf.write(u"\u03c9\5\u00fa~\2\u03c8\u03c7\3\2\2\2\u03c8\u03c9\3\2")
        buf.write(u"\2\2\u03c9\u03d5\3\2\2\2\u03ca\u03ce\7\u0082\2\2\u03cb")
        buf.write(u"\u03cc\7\u0099\2\2\u03cc\u03ce\7I\2\2\u03cd\u03ca\3\2")
        buf.write(u"\2\2\u03cd\u03cb\3\2\2\2\u03ce\u03cf\3\2\2\2\u03cf\u03d0")
        buf.write(u"\7\21\2\2\u03d0\u03d1\5\u0088E\2\u03d1\u03d2\5\u00f4")
        buf.write(u"{\2\u03d2\u03d3\5\u008aF\2\u03d3\u03d4\5\u0084C\2\u03d4")
        buf.write(u"\u03d6\3\2\2\2\u03d5\u03cd\3\2\2\2\u03d5\u03d6\3\2\2")
        buf.write(u"\2\u03d6\u03de\3\2\2\2\u03d7\u03d8\7G\2\2\u03d8\u03d9")
        buf.write(u"\7\21\2\2\u03d9\u03da\5\u0088E\2\u03da\u03db\5\u00f4")
        buf.write(u"{\2\u03db\u03dc\5\u008aF\2\u03dc\u03dd\5\u0084C\2\u03dd")
        buf.write(u"\u03df\3\2\2\2\u03de\u03d7\3\2\2\2\u03de\u03df\3\2\2")
        buf.write(u"\2\u03df\u03e0\3\2\2\2\u03e0\u03e1\5\u0084C\2\u03e1Q")
        buf.write(u"\3\2\2\2\u03e2\u03e3\7\u0099\2\2\u03e3\u03e4\5\u00c2")
        buf.write(u"b\2\u03e4\u03e5\7\21\2\2\u03e5\u03e6\5\u0088E\2\u03e6")
        buf.write(u"\u03e7\5\u00f4{\2\u03e7\u03e8\5\u008aF\2\u03e8\u03e9")
        buf.write(u"\5\u0084C\2\u03e9\u03f6\3\2\2\2\u03ea\u03eb\7\u0099\2")
        buf.write(u"\2\u03eb\u03ec\7n\2\2\u03ec\u03ed\7\30\2\2\u03ed\u03ee")
        buf.write(u"\5\u009cO\2\u03ee\u03ef\7\31\2\2\u03ef\u03f0\7\21\2\2")
        buf.write(u"\u03f0\u03f1\5\u0088E\2\u03f1\u03f2\5\u00f4{\2\u03f2")
        buf.write(u"\u03f3\5\u008aF\2\u03f3\u03f4\5\u0084C\2\u03f4\u03f6")
        buf.write(u"\3\2\2\2\u03f5\u03e2\3\2\2\2\u03f5\u03ea\3\2\2\2\u03f6")
        buf.write(u"S\3\2\2\2\u03f7\u03f8\7P\2\2\u03f8U\3\2\2\2\u03f9\u03fb")
        buf.write(u"\7\u0088\2\2\u03fa\u03fc\5X-\2\u03fb\u03fa\3\2\2\2\u03fb")
        buf.write(u"\u03fc\3\2\2\2\u03fcW\3\2\2\2\u03fd\u03fe\b-\1\2\u03fe")
        buf.write(u"\u03ff\7#\2\2\u03ff\u041a\5X-+\u0400\u0401\7y\2\2\u0401")
        buf.write(u"\u041a\5X-*\u0402\u0403\7>\2\2\u0403\u0404\7\21\2\2\u0404")
        buf.write(u"\u041a\5X-\17\u0405\u041a\5b\62\2\u0406\u041a\5Z.\2\u0407")
        buf.write(u"\u0408\5Z.\2\u0408\u0409\5x=\2\u0409\u041a\3\2\2\2\u040a")
        buf.write(u"\u040b\7d\2\2\u040b\u040c\7\21\2\2\u040c\u041a\5\u00bc")
        buf.write(u"_\2\u040d\u040e\7=\2\2\u040e\u040f\7\21\2\2\u040f\u041a")
        buf.write(u"\5\u00b8]\2\u0410\u041a\5h\65\2\u0411\u041a\5f\64\2\u0412")
        buf.write(u"\u041a\5j\66\2\u0413\u041a\5r:\2\u0414\u041a\5t;\2\u0415")
        buf.write(u"\u041a\5l\67\2\u0416\u041a\5v<\2\u0417\u041a\5p9\2\u0418")
        buf.write(u"\u041a\5^\60\2\u0419\u03fd\3\2\2\2\u0419\u0400\3\2\2")
        buf.write(u"\2\u0419\u0402\3\2\2\2\u0419\u0405\3\2\2\2\u0419\u0406")
        buf.write(u"\3\2\2\2\u0419\u0407\3\2\2\2\u0419\u040a\3\2\2\2\u0419")
        buf.write(u"\u040d\3\2\2\2\u0419\u0410\3\2\2\2\u0419\u0411\3\2\2")
        buf.write(u"\2\u0419\u0412\3\2\2\2\u0419\u0413\3\2\2\2\u0419\u0414")
        buf.write(u"\3\2\2\2\u0419\u0415\3\2\2\2\u0419\u0416\3\2\2\2\u0419")
        buf.write(u"\u0417\3\2\2\2\u0419\u0418\3\2\2\2\u041a\u0482\3\2\2")
        buf.write(u"\2\u041b\u041c\f)\2\2\u041c\u041d\5\u0130\u0099\2\u041d")
        buf.write(u"\u041e\5X-*\u041e\u0481\3\2\2\2\u041f\u0420\f(\2\2\u0420")
        buf.write(u"\u0421\5\u0132\u009a\2\u0421\u0422\5X-)\u0422\u0481\3")
        buf.write(u"\2\2\2\u0423\u0424\f\'\2\2\u0424\u0425\5\u0136\u009c")
        buf.write(u"\2\u0425\u0426\5X-(\u0426\u0481\3\2\2\2\u0427\u0428\f")
        buf.write(u"&\2\2\u0428\u0429\5\u0134\u009b\2\u0429\u042a\5X-\'\u042a")
        buf.write(u"\u0481\3\2\2\2\u042b\u042c\f%\2\2\u042c\u042d\t\2\2\2")
        buf.write(u"\u042d\u0481\5X-&\u042e\u042f\f$\2\2\u042f\u0430\7*\2")
        buf.write(u"\2\u0430\u0481\5X-%\u0431\u0432\f#\2\2\u0432\u0433\7")
        buf.write(u"+\2\2\u0433\u0481\5X-$\u0434\u0435\f\"\2\2\u0435\u0436")
        buf.write(u"\7(\2\2\u0436\u0481\5X-#\u0437\u0438\f!\2\2\u0438\u0439")
        buf.write(u"\7)\2\2\u0439\u0481\5X-\"\u043a\u043b\f\36\2\2\u043b")
        buf.write(u"\u043c\7-\2\2\u043c\u0481\5X-\37\u043d\u043e\f\35\2\2")
        buf.write(u"\u043e\u043f\7,\2\2\u043f\u0481\5X-\36\u0440\u0441\f")
        buf.write(u"\34\2\2\u0441\u0442\7\61\2\2\u0442\u0481\5X-\35\u0443")
        buf.write(u"\u0444\f\33\2\2\u0444\u0445\7\u0080\2\2\u0445\u0481\5")
        buf.write(u"X-\34\u0446\u0447\f\32\2\2\u0447\u0448\7H\2\2\u0448\u0481")
        buf.write(u"\5X-\33\u0449\u044a\f\31\2\2\u044a\u044b\7m\2\2\u044b")
        buf.write(u"\u044c\5X-\2\u044c\u044d\7`\2\2\u044d\u044e\5X-\32\u044e")
        buf.write(u"\u0481\3\2\2\2\u044f\u0450\f\27\2\2\u0450\u0451\7n\2")
        buf.write(u"\2\u0451\u0481\5X-\30\u0452\u0453\f\26\2\2\u0453\u0454")
        buf.write(u"\7W\2\2\u0454\u0481\5X-\27\u0455\u0456\f\25\2\2\u0456")
        buf.write(u"\u0457\7W\2\2\u0457\u0458\7F\2\2\u0458\u0481\5X-\26\u0459")
        buf.write(u"\u045a\f\24\2\2\u045a\u045b\7W\2\2\u045b\u045c\7I\2\2")
        buf.write(u"\u045c\u0481\5X-\25\u045d\u045e\f\23\2\2\u045e\u045f")
        buf.write(u"\7y\2\2\u045f\u0460\7n\2\2\u0460\u0481\5X-\24\u0461\u0462")
        buf.write(u"\f\22\2\2\u0462\u0463\7y\2\2\u0463\u0464\7W\2\2\u0464")
        buf.write(u"\u0481\5X-\23\u0465\u0466\f\21\2\2\u0466\u0467\7y\2\2")
        buf.write(u"\u0467\u0468\7W\2\2\u0468\u0469\7F\2\2\u0469\u0481\5")
        buf.write(u"X-\22\u046a\u046b\f\20\2\2\u046b\u046c\7y\2\2\u046c\u046d")
        buf.write(u"\7W\2\2\u046d\u046e\7I\2\2\u046e\u0481\5X-\21\u046f\u0470")
        buf.write(u"\f\3\2\2\u0470\u0471\7j\2\2\u0471\u0472\7_\2\2\u0472")
        buf.write(u"\u0473\5\u00bc_\2\u0473\u0474\7n\2\2\u0474\u0475\5X-")
        buf.write(u"\4\u0475\u0481\3\2\2\2\u0476\u0477\f \2\2\u0477\u0478")
        buf.write(u"\7q\2\2\u0478\u0479\7y\2\2\u0479\u0481\5\u011c\u008f")
        buf.write(u"\2\u047a\u047b\f\37\2\2\u047b\u047c\7q\2\2\u047c\u0481")
        buf.write(u"\5\u011c\u008f\2\u047d\u047e\f\30\2\2\u047e\u047f\7J")
        buf.write(u"\2\2\u047f\u0481\5\u00ceh\2\u0480\u041b\3\2\2\2\u0480")
        buf.write(u"\u041f\3\2\2\2\u0480\u0423\3\2\2\2\u0480\u0427\3\2\2")
        buf.write(u"\2\u0480\u042b\3\2\2\2\u0480\u042e\3\2\2\2\u0480\u0431")
        buf.write(u"\3\2\2\2\u0480\u0434\3\2\2\2\u0480\u0437\3\2\2\2\u0480")
        buf.write(u"\u043a\3\2\2\2\u0480\u043d\3\2\2\2\u0480\u0440\3\2\2")
        buf.write(u"\2\u0480\u0443\3\2\2\2\u0480\u0446\3\2\2\2\u0480\u0449")
        buf.write(u"\3\2\2\2\u0480\u044f\3\2\2\2\u0480\u0452\3\2\2\2\u0480")
        buf.write(u"\u0455\3\2\2\2\u0480\u0459\3\2\2\2\u0480\u045d\3\2\2")
        buf.write(u"\2\u0480\u0461\3\2\2\2\u0480\u0465\3\2\2\2\u0480\u046a")
        buf.write(u"\3\2\2\2\u0480\u046f\3\2\2\2\u0480\u0476\3\2\2\2\u0480")
        buf.write(u"\u047a\3\2\2\2\u0480\u047d\3\2\2\2\u0481\u0484\3\2\2")
        buf.write(u"\2\u0482\u0480\3\2\2\2\u0482\u0483\3\2\2\2\u0483Y\3\2")
        buf.write(u"\2\2\u0484\u0482\3\2\2\2\u0485\u0486\b.\1\2\u0486\u0487")
        buf.write(u"\5\u00ba^\2\u0487\u048c\3\2\2\2\u0488\u0489\f\3\2\2\u0489")
        buf.write(u"\u048b\5\\/\2\u048a\u0488\3\2\2\2\u048b\u048e\3\2\2\2")
        buf.write(u"\u048c\u048a\3\2\2\2\u048c\u048d\3\2\2\2\u048d[\3\2\2")
        buf.write(u"\2\u048e\u048c\3\2\2\2\u048f\u0490\6/ \3\u0490\u0491")
        buf.write(u"\7\25\2\2\u0491\u0492\5\u00ba^\2\u0492]\3\2\2\2\u0493")
        buf.write(u"\u0494\7p\2\2\u0494\u0495\7\21\2\2\u0495\u0496\5\u00bc")
        buf.write(u"_\2\u0496\u0497\5`\61\2\u0497_\3\2\2\2\u0498\u0499\6")
        buf.write(u"\61!\3\u0499a\3\2\2\2\u049a\u049b\b\62\1\2\u049b\u049c")
        buf.write(u"\5\u0102\u0082\2\u049c\u04a1\3\2\2\2\u049d\u049e\f\3")
        buf.write(u"\2\2\u049e\u04a0\5d\63\2\u049f\u049d\3\2\2\2\u04a0\u04a3")
        buf.write(u"\3\2\2\2\u04a1\u049f\3\2\2\2\u04a1\u04a2\3\2\2\2\u04a2")
        buf.write(u"c\3\2\2\2\u04a3\u04a1\3\2\2\2\u04a4\u04a5\6\63#\3\u04a5")
        buf.write(u"\u04a6\7\25\2\2\u04a6\u04b2\5\u00bc_\2\u04a7\u04a8\6")
        buf.write(u"\63$\3\u04a8\u04a9\7\30\2\2\u04a9\u04aa\5\u0116\u008c")
        buf.write(u"\2\u04aa\u04ab\7\31\2\2\u04ab\u04b2\3\2\2\2\u04ac\u04ad")
        buf.write(u"\6\63%\3\u04ad\u04ae\7\30\2\2\u04ae\u04af\5X-\2\u04af")
        buf.write(u"\u04b0\7\31\2\2\u04b0\u04b2\3\2\2\2\u04b1\u04a4\3\2\2")
        buf.write(u"\2\u04b1\u04a7\3\2\2\2\u04b1\u04ac\3\2\2\2\u04b2e\3\2")
        buf.write(u"\2\2\u04b3\u04b6\7?\2\2\u04b4\u04b5\7k\2\2\u04b5\u04b7")
        buf.write(u"\5X-\2\u04b6\u04b4\3\2\2\2\u04b6\u04b7\3\2\2\2\u04b7")
        buf.write(u"g\3\2\2\2\u04b8\u04b9\7@\2\2\u04b9\u04ba\7k\2\2\u04ba")
        buf.write(u"\u04bb\5X-\2\u04bbi\3\2\2\2\u04bc\u04bd\5\u00b0Y\2\u04bd")
        buf.write(u"\u04be\7k\2\2\u04be\u04c7\5X-\2\u04bf\u04c1\7\23\2\2")
        buf.write(u"\u04c0\u04bf\3\2\2\2\u04c0\u04c1\3\2\2\2\u04c1\u04c2")
        buf.write(u"\3\2\2\2\u04c2\u04c5\5z>\2\u04c3\u04c4\7H\2\2\u04c4\u04c6")
        buf.write(u"\5|?\2\u04c5\u04c3\3\2\2\2\u04c5\u04c6\3\2\2\2\u04c6")
        buf.write(u"\u04c8\3\2\2\2\u04c7\u04c0\3\2\2\2\u04c7\u04c8\3\2\2")
        buf.write(u"\2\u04c8\u04d2\3\2\2\2\u04c9\u04cf\5\u00b0Y\2\u04ca\u04cd")
        buf.write(u"\5z>\2\u04cb\u04cc\7H\2\2\u04cc\u04ce\5|?\2\u04cd\u04cb")
        buf.write(u"\3\2\2\2\u04cd\u04ce\3\2\2\2\u04ce\u04d0\3\2\2\2\u04cf")
        buf.write(u"\u04ca\3\2\2\2\u04cf\u04d0\3\2\2\2\u04d0\u04d2\3\2\2")
        buf.write(u"\2\u04d1\u04bc\3\2\2\2\u04d1\u04c9\3\2\2\2\u04d2k\3\2")
        buf.write(u"\2\2\u04d3\u04d4\7\u0085\2\2\u04d4\u04d5\7k\2\2\u04d5")
        buf.write(u"\u04d6\5X-\2\u04d6m\3\2\2\2\u04d7\u04d8\7\u009c\2\2\u04d8")
        buf.write(u"\u04d9\5X-\2\u04d9\u04da\7\u0095\2\2\u04da\u04db\5X-")
        buf.write(u"\2\u04dbo\3\2\2\2\u04dc\u04dd\5Z.\2\u04dd\u04de\7#\2")
        buf.write(u"\2\u04de\u04df\5X-\2\u04dfq\3\2\2\2\u04e0\u04e1\7g\2")
        buf.write(u"\2\u04e1\u04e2\7I\2\2\u04e2\u04e3\5\u00bc_\2\u04e3\u04e4")
        buf.write(u"\7k\2\2\u04e4\u04e5\5X-\2\u04e5\u04e6\7\u009a\2\2\u04e6")
        buf.write(u"\u04e7\5X-\2\u04e7s\3\2\2\2\u04e8\u04e9\7g\2\2\u04e9")
        buf.write(u"\u04eb\7}\2\2\u04ea\u04ec\5\u00b0Y\2\u04eb\u04ea\3\2")
        buf.write(u"\2\2\u04eb\u04ec\3\2\2\2\u04ec\u04ed\3\2\2\2\u04ed\u04ee")
        buf.write(u"\7\u009a\2\2\u04ee\u0507\5X-\2\u04ef\u04fb\7g\2\2\u04f0")
        buf.write(u"\u04f2\7F\2\2\u04f1\u04f3\5\u00b0Y\2\u04f2\u04f1\3\2")
        buf.write(u"\2\2\u04f2\u04f3\3\2\2\2\u04f3\u04fc\3\2\2\2\u04f4\u04f6")
        buf.write(u"\5\u00b0Y\2\u04f5\u04f4\3\2\2\2\u04f5\u04f6\3\2\2\2\u04f6")
        buf.write(u"\u04f7\3\2\2\2\u04f7\u04f8\5X-\2\u04f8\u04f9\7\u0095")
        buf.write(u"\2\2\u04f9\u04fa\5X-\2\u04fa\u04fc\3\2\2\2\u04fb\u04f0")
        buf.write(u"\3\2\2\2\u04fb\u04f5\3\2\2\2\u04fc\u04ff\3\2\2\2\u04fd")
        buf.write(u"\u04fe\7\u009a\2\2\u04fe\u0500\5X-\2\u04ff\u04fd\3\2")
        buf.write(u"\2\2\u04ff\u0500\3\2\2\2\u0500\u0504\3\2\2\2\u0501\u0502")
        buf.write(u"\7\u0081\2\2\u0502\u0503\7Q\2\2\u0503\u0505\5\u011e\u0090")
        buf.write(u"\2\u0504\u0501\3\2\2\2\u0504\u0505\3\2\2\2\u0505\u0507")
        buf.write(u"\3\2\2\2\u0506\u04e8\3\2\2\2\u0506\u04ef\3\2\2\2\u0507")
        buf.write(u"u\3\2\2\2\u0508\u050a\7\u008e\2\2\u0509\u050b\7\\\2\2")
        buf.write(u"\u050a\u0509\3\2\2\2\u050a\u050b\3\2\2\2\u050b\u050c")
        buf.write(u"\3\2\2\2\u050c\u0512\5b\62\2\u050d\u050e\7\u0098\2\2")
        buf.write(u"\u050e\u050f\5b\62\2\u050f\u0510\7J\2\2\u0510\u0511\5")
        buf.write(u"\u0126\u0094\2\u0511\u0513\3\2\2\2\u0512\u050d\3\2\2")
        buf.write(u"\2\u0512\u0513\3\2\2\2\u0513w\3\2\2\2\u0514\u0515\6=")
        buf.write(u"&\3\u0515\u051b\5X-\2\u0516\u0519\5z>\2\u0517\u0518\7")
        buf.write(u"H\2\2\u0518\u051a\5|?\2\u0519\u0517\3\2\2\2\u0519\u051a")
        buf.write(u"\3\2\2\2\u051a\u051c\3\2\2\2\u051b\u0516\3\2\2\2\u051b")
        buf.write(u"\u051c\3\2\2\2\u051c\u0523\3\2\2\2\u051d\u0520\5z>\2")
        buf.write(u"\u051e\u051f\7H\2\2\u051f\u0521\5|?\2\u0520\u051e\3\2")
        buf.write(u"\2\2\u0520\u0521\3\2\2\2\u0521\u0523\3\2\2\2\u0522\u0514")
        buf.write(u"\3\2\2\2\u0522\u051d\3\2\2\2\u0523y\3\2\2\2\u0524\u0525")
        buf.write(u"\b>\1\2\u0525\u0526\7\u0098\2\2\u0526\u0527\5|?\2\u0527")
        buf.write(u"\u052d\3\2\2\2\u0528\u0529\f\3\2\2\u0529\u052a\7\23\2")
        buf.write(u"\2\u052a\u052c\5|?\2\u052b\u0528\3\2\2\2\u052c\u052f")
        buf.write(u"\3\2\2\2\u052d\u052b\3\2\2\2\u052d\u052e\3\2\2\2\u052e")
        buf.write(u"{\3\2\2\2\u052f\u052d\3\2\2\2\u0530\u0531\5X-\2\u0531")
        buf.write(u"\u0532\7J\2\2\u0532\u0533\5\u00bc_\2\u0533}\3\2\2\2\u0534")
        buf.write(u"\u0535\5\u011a\u008e\2\u0535\u0536\5\u012e\u0098\2\u0536")
        buf.write(u"\u0537\5X-\2\u0537\177\3\2\2\2\u0538\u0539\6A(\3\u0539")
        buf.write(u"\u053a\7\25\2\2\u053a\u0541\5\u00bc_\2\u053b\u053c\6")
        buf.write(u"A)\3\u053c\u053d\7\30\2\2\u053d\u053e\5X-\2\u053e\u053f")
        buf.write(u"\7\31\2\2\u053f\u0541\3\2\2\2\u0540\u0538\3\2\2\2\u0540")
        buf.write(u"\u053b\3\2\2\2\u0541\u0081\3\2\2\2\u0542\u0543\5\u00e4")
        buf.write(u"s\2\u0543\u0544\5\u012e\u0098\2\u0544\u0545\5X-\2\u0545")
        buf.write(u"\u0083\3\2\2\2\u0546\u0548\7\7\2\2\u0547\u0546\3\2\2")
        buf.write(u"\2\u0548\u054b\3\2\2\2\u0549\u0547\3\2\2\2\u0549\u054a")
        buf.write(u"\3\2\2\2\u054a\u0085\3\2\2\2\u054b\u0549\3\2\2\2\u054c")
        buf.write(u"\u054e\7\7\2\2\u054d\u054c\3\2\2\2\u054e\u054f\3\2\2")
        buf.write(u"\2\u054f\u054d\3\2\2\2\u054f\u0550\3\2\2\2\u0550\u0087")
        buf.write(u"\3\2\2\2\u0551\u0553\7\7\2\2\u0552\u0551\3\2\2\2\u0553")
        buf.write(u"\u0554\3\2\2\2\u0554\u0552\3\2\2\2\u0554\u0555\3\2\2")
        buf.write(u"\2\u0555\u0556\3\2\2\2\u0556\u0557\7\3\2\2\u0557\u0089")
        buf.write(u"\3\2\2\2\u0558\u055a\7\7\2\2\u0559\u0558\3\2\2\2\u055a")
        buf.write(u"\u055d\3\2\2\2\u055b\u0559\3\2\2\2\u055b\u055c\3\2\2")
        buf.write(u"\2\u055c\u055e\3\2\2\2\u055d\u055b\3\2\2\2\u055e\u055f")
        buf.write(u"\7\4\2\2\u055f\u008b\3\2\2\2\u0560\u0561\7z\2\2\u0561")
        buf.write(u"\u008d\3\2\2\2\u0562\u0564\5\u0090I\2\u0563\u0562\3\2")
        buf.write(u"\2\2\u0563\u0564\3\2\2\2\u0564\u0565\3\2\2\2\u0565\u0566")
        buf.write(u"\5\u0084C\2\u0566\u0567\7\2\2\3\u0567\u008f\3\2\2\2\u0568")
        buf.write(u"\u056e\5\u0092J\2\u0569\u056a\5\u0086D\2\u056a\u056b")
        buf.write(u"\5\u0092J\2\u056b\u056d\3\2\2\2\u056c\u0569\3\2\2\2\u056d")
        buf.write(u"\u0570\3\2\2\2\u056e\u056c\3\2\2\2\u056e\u056f\3\2\2")
        buf.write(u"\2\u056f\u0091\3\2\2\2\u0570\u056e\3\2\2\2\u0571\u0572")
        buf.write(u"\5\u00eav\2\u0572\u0573\5\u0086D\2\u0573\u0575\3\2\2")
        buf.write(u"\2\u0574\u0571\3\2\2\2\u0575\u0578\3\2\2\2\u0576\u0574")
        buf.write(u"\3\2\2\2\u0576\u0577\3\2\2\2\u0577\u057e\3\2\2\2\u0578")
        buf.write(u"\u0576\3\2\2\2\u0579\u057f\5\n\6\2\u057a\u057f\5\u00b4")
        buf.write(u"[\2\u057b\u057f\5\u0094K\2\u057c\u057f\5\u0096L\2\u057d")
        buf.write(u"\u057f\5\u00e8u\2\u057e\u0579\3\2\2\2\u057e\u057a\3\2")
        buf.write(u"\2\2\u057e\u057b\3\2\2\2\u057e\u057c\3\2\2\2\u057e\u057d")
        buf.write(u"\3\2\2\2\u057f\u0093\3\2\2\2\u0580\u0581\5\36\20\2\u0581")
        buf.write(u"\u0095\3\2\2\2\u0582\u0585\5\2\2\2\u0583\u0585\5\4\3")
        buf.write(u"\2\u0584\u0582\3\2\2\2\u0584\u0583\3\2\2\2\u0585\u0097")
        buf.write(u"\3\2\2\2\u0586\u058c\5\6\4\2\u0587\u0588\5\u0086D\2\u0588")
        buf.write(u"\u0589\5\6\4\2\u0589\u058b\3\2\2\2\u058a\u0587\3\2\2")
        buf.write(u"\2\u058b\u058e\3\2\2\2\u058c\u058a\3\2\2\2\u058c\u058d")
        buf.write(u"\3\2\2\2\u058d\u0099\3\2\2\2\u058e\u058c\3\2\2\2\u058f")
        buf.write(u"\u0595\5\b\5\2\u0590\u0591\5\u0086D\2\u0591\u0592\5\b")
        buf.write(u"\5\2\u0592\u0594\3\2\2\2\u0593\u0590\3\2\2\2\u0594\u0597")
        buf.write(u"\3\2\2\2\u0595\u0593\3\2\2\2\u0595\u0596\3\2\2\2\u0596")
        buf.write(u"\u009b\3\2\2\2\u0597\u0595\3\2\2\2\u0598\u059d\5\u00c2")
        buf.write(u"b\2\u0599\u059a\7\23\2\2\u059a\u059c\5\u00c2b\2\u059b")
        buf.write(u"\u0599\3\2\2\2\u059c\u059f\3\2\2\2\u059d\u059b\3\2\2")
        buf.write(u"\2\u059d\u059e\3\2\2\2\u059e\u009d\3\2\2\2\u059f\u059d")
        buf.write(u"\3\2\2\2\u05a0\u05a1\7n\2\2\u05a1\u05ab\5\u00a0Q\2\u05a2")
        buf.write(u"\u05a3\7n\2\2\u05a3\u05ab\5\u00a2R\2\u05a4\u05a5\7n\2")
        buf.write(u"\2\u05a5\u05ab\5\u00a6T\2\u05a6\u05a7\7r\2\2\u05a7\u05ab")
        buf.write(u"\7\u00a6\2\2\u05a8\u05a9\7r\2\2\u05a9\u05ab\5X-\2\u05aa")
        buf.write(u"\u05a0\3\2\2\2\u05aa\u05a2\3\2\2\2\u05aa\u05a4\3\2\2")
        buf.write(u"\2\u05aa\u05a6\3\2\2\2\u05aa\u05a8\3\2\2\2\u05ab\u009f")
        buf.write(u"\3\2\2\2\u05ac\u05ae\7v\2\2\u05ad\u05ac\3\2\2\2\u05ad")
        buf.write(u"\u05ae\3\2\2\2\u05ae\u05af\3\2\2\2\u05af\u05b1\7\30\2")
        buf.write(u"\2\u05b0\u05b2\5\u00a4S\2\u05b1\u05b0\3\2\2\2\u05b1\u05b2")
        buf.write(u"\3\2\2\2\u05b2\u05b3\3\2\2\2\u05b3\u05b4\7\31\2\2\u05b4")
        buf.write(u"\u00a1\3\2\2\2\u05b5\u05b7\7v\2\2\u05b6\u05b5\3\2\2\2")
        buf.write(u"\u05b6\u05b7\3\2\2\2\u05b7\u05b8\3\2\2\2\u05b8\u05ba")
        buf.write(u"\7*\2\2\u05b9\u05bb\5\u00a4S\2\u05ba\u05b9\3\2\2\2\u05ba")
        buf.write(u"\u05bb\3\2\2\2\u05bb\u05bc\3\2\2\2\u05bc\u05bd\7(\2\2")
        buf.write(u"\u05bd\u00a3\3\2\2\2\u05be\u05c3\5X-\2\u05bf\u05c0\7")
        buf.write(u"\23\2\2\u05c0\u05c2\5X-\2\u05c1\u05bf\3\2\2\2\u05c2\u05c5")
        buf.write(u"\3\2\2\2\u05c3\u05c1\3\2\2\2\u05c3\u05c4\3\2\2\2\u05c4")
        buf.write(u"\u00a5\3\2\2\2\u05c5\u05c3\3\2\2\2\u05c6\u05c7\7\30\2")
        buf.write(u"\2\u05c7\u05c8\5X-\2\u05c8\u05c9\7\24\2\2\u05c9\u05ca")
        buf.write(u"\5X-\2\u05ca\u05cb\7\31\2\2\u05cb\u00a7\3\2\2\2\u05cc")
        buf.write(u"\u05cd\bU\1\2\u05cd\u05d9\5\u00aaV\2\u05ce\u05cf\7D\2")
        buf.write(u"\2\u05cf\u05d0\7*\2\2\u05d0\u05d1\5\u00a8U\2\u05d1\u05d2")
        buf.write(u"\7(\2\2\u05d2\u05d9\3\2\2\2\u05d3\u05d4\7C\2\2\u05d4")
        buf.write(u"\u05d5\7*\2\2\u05d5\u05d6\5\u00a8U\2\u05d6\u05d7\7(\2")
        buf.write(u"\2\u05d7\u05d9\3\2\2\2\u05d8\u05cc\3\2\2\2\u05d8\u05ce")
        buf.write(u"\3\2\2\2\u05d8\u05d3\3\2\2\2\u05d9\u05e4\3\2\2\2\u05da")
        buf.write(u"\u05db\f\7\2\2\u05db\u05e3\7,\2\2\u05dc\u05dd\f\6\2\2")
        buf.write(u"\u05dd\u05de\7\30\2\2\u05de\u05e3\7\31\2\2\u05df\u05e0")
        buf.write(u"\f\5\2\2\u05e0\u05e1\7\32\2\2\u05e1\u05e3\7\33\2\2\u05e2")
        buf.write(u"\u05da\3\2\2\2\u05e2\u05dc\3\2\2\2\u05e2\u05df\3\2\2")
        buf.write(u"\2\u05e3\u05e6\3\2\2\2\u05e4\u05e2\3\2\2\2\u05e4\u05e5")
        buf.write(u"\3\2\2\2\u05e5\u00a9\3\2\2\2\u05e6\u05e4\3\2\2\2\u05e7")
        buf.write(u"\u05ea\5\u00acW\2\u05e8\u05ea\5\u00aeX\2\u05e9\u05e7")
        buf.write(u"\3\2\2\2\u05e9\u05e8\3\2\2\2\u05ea\u00ab\3\2\2\2\u05eb")
        buf.write(u"\u05fa\7\64\2\2\u05ec\u05fa\7\65\2\2\u05ed\u05fa\7\66")
        buf.write(u"\2\2\u05ee\u05fa\7A\2\2\u05ef\u05fa\7\67\2\2\u05f0\u05fa")
        buf.write(u"\78\2\2\u05f1\u05fa\7?\2\2\u05f2\u05fa\79\2\2\u05f3\u05fa")
        buf.write(u"\7;\2\2\u05f4\u05fa\7:\2\2\u05f5\u05fa\7<\2\2\u05f6\u05fa")
        buf.write(u"\7>\2\2\u05f7\u05fa\7@\2\2\u05f8\u05fa\7B\2\2\u05f9\u05eb")
        buf.write(u"\3\2\2\2\u05f9\u05ec\3\2\2\2\u05f9\u05ed\3\2\2\2\u05f9")
        buf.write(u"\u05ee\3\2\2\2\u05f9\u05ef\3\2\2\2\u05f9\u05f0\3\2\2")
        buf.write(u"\2\u05f9\u05f1\3\2\2\2\u05f9\u05f2\3\2\2\2\u05f9\u05f3")
        buf.write(u"\3\2\2\2\u05f9\u05f4\3\2\2\2\u05f9\u05f5\3\2\2\2\u05f9")
        buf.write(u"\u05f6\3\2\2\2\u05f9\u05f7\3\2\2\2\u05f9\u05f8\3\2\2")
        buf.write(u"\2\u05fa\u00ad\3\2\2\2\u05fb\u05fc\7\u00a2\2\2\u05fc")
        buf.write(u"\u00af\3\2\2\2\u05fd\u05ff\7v\2\2\u05fe\u05fd\3\2\2\2")
        buf.write(u"\u05fe\u05ff\3\2\2\2\u05ff\u0600\3\2\2\2\u0600\u0601")
        buf.write(u"\5\u00aeX\2\u0601\u00b1\3\2\2\2\u0602\u0603\7>\2\2\u0603")
        buf.write(u"\u00b3\3\2\2\2\u0604\u0608\5\f\7\2\u0605\u0608\5\34\17")
        buf.write(u"\2\u0606\u0608\5\16\b\2\u0607\u0604\3\2\2\2\u0607\u0605")
        buf.write(u"\3\2\2\2\u0607\u0606\3\2\2\2\u0608\u00b5\3\2\2\2\u0609")
        buf.write(u"\u060e\5\u00c0a\2\u060a\u060b\7\23\2\2\u060b\u060d\5")
        buf.write(u"\u00c0a\2\u060c\u060a\3\2\2\2\u060d\u0610\3\2\2\2\u060e")
        buf.write(u"\u060c\3\2\2\2\u060e\u060f\3\2\2\2\u060f\u00b7\3\2\2")
        buf.write(u"\2\u0610\u060e\3\2\2\2\u0611\u0614\5\u00bc_\2\u0612\u0614")
        buf.write(u"\5\u00c0a\2\u0613\u0611\3\2\2\2\u0613\u0612\3\2\2\2\u0614")
        buf.write(u"\u00b9\3\2\2\2\u0615\u0619\5\u00bc_\2\u0616\u0619\5\u00c0")
        buf.write(u"a\2\u0617\u0619\5\u00c2b\2\u0618\u0615\3\2\2\2\u0618")
        buf.write(u"\u0616\3\2\2\2\u0618\u0617\3\2\2\2\u0619\u00bb\3\2\2")
        buf.write(u"\2\u061a\u061b\7\u00a3\2\2\u061b\u00bd\3\2\2\2\u061c")
        buf.write(u"\u061d\t\3\2\2\u061d\u00bf\3\2\2\2\u061e\u061f\7\u00a2")
        buf.write(u"\2\2\u061f\u00c1\3\2\2\2\u0620\u0621\7\u00a1\2\2\u0621")
        buf.write(u"\u00c3\3\2\2\2\u0622\u0627\5\u00c6d\2\u0623\u0624\7\23")
        buf.write(u"\2\2\u0624\u0626\5\u00c6d\2\u0625\u0623\3\2\2\2\u0626")
        buf.write(u"\u0629\3\2\2\2\u0627\u0625\3\2\2\2\u0627\u0628\3\2\2")
        buf.write(u"\2\u0628\u00c5\3\2\2\2\u0629\u0627\3\2\2\2\u062a\u0630")
        buf.write(u"\5\u00ccg\2\u062b\u062d\7v\2\2\u062c\u062b\3\2\2\2\u062c")
        buf.write(u"\u062d\3\2\2\2\u062d\u062e\3\2\2\2\u062e\u0630\5\u00c8")
        buf.write(u"e\2\u062f\u062a\3\2\2\2\u062f\u062c\3\2\2\2\u0630\u00c7")
        buf.write(u"\3\2\2\2\u0631\u0634\5\u00caf\2\u0632\u0634\5\62\32\2")
        buf.write(u"\u0633\u0631\3\2\2\2\u0633\u0632\3\2\2\2\u0634\u00c9")
        buf.write(u"\3\2\2\2\u0635\u0638\5\u00bc_\2\u0636\u0637\7-\2\2\u0637")
        buf.write(u"\u0639\5\u0108\u0085\2\u0638\u0636\3\2\2\2\u0638\u0639")
        buf.write(u"\3\2\2\2\u0639\u00cb\3\2\2\2\u063a\u063b\5\u00b2Z\2\u063b")
        buf.write(u"\u063c\5\u00bc_\2\u063c\u00cd\3\2\2\2\u063d\u0640\5\u00a8")
        buf.write(u"U\2\u063e\u0640\5\u00d0i\2\u063f\u063d\3\2\2\2\u063f")
        buf.write(u"\u063e\3\2\2\2\u0640\u00cf\3\2\2\2\u0641\u0642\bi\1\2")
        buf.write(u"\u0642\u0643\7I\2\2\u0643\u064c\3\2\2\2\u0644\u0645\f")
        buf.write(u"\4\2\2\u0645\u0646\7\30\2\2\u0646\u064b\7\31\2\2\u0647")
        buf.write(u"\u0648\f\3\2\2\u0648\u0649\7\32\2\2\u0649\u064b\7\33")
        buf.write(u"\2\2\u064a\u0644\3\2\2\2\u064a\u0647\3\2\2\2\u064b\u064e")
        buf.write(u"\3\2\2\2\u064c\u064a\3\2\2\2\u064c\u064d\3\2\2\2\u064d")
        buf.write(u"\u00d1\3\2\2\2\u064e\u064c\3\2\2\2\u064f\u0655\5\u00d4")
        buf.write(u"k\2\u0650\u0651\5\u0086D\2\u0651\u0652\5\u00d4k\2\u0652")
        buf.write(u"\u0654\3\2\2\2\u0653\u0650\3\2\2\2\u0654\u0657\3\2\2")
        buf.write(u"\2\u0655\u0653\3\2\2\2\u0655\u0656\3\2\2\2\u0656\u00d3")
        buf.write(u"\3\2\2\2\u0657\u0655\3\2\2\2\u0658\u065e\5\24\13\2\u0659")
        buf.write(u"\u065e\5\30\r\2\u065a\u065e\5(\25\2\u065b\u065e\5&\24")
        buf.write(u"\2\u065c\u065e\5\22\n\2\u065d\u0658\3\2\2\2\u065d\u0659")
        buf.write(u"\3\2\2\2\u065d\u065a\3\2\2\2\u065d\u065b\3\2\2\2\u065d")
        buf.write(u"\u065c\3\2\2\2\u065e\u00d5\3\2\2\2\u065f\u0665\5\u00d8")
        buf.write(u"m\2\u0660\u0661\5\u0086D\2\u0661\u0662\5\u00d8m\2\u0662")
        buf.write(u"\u0664\3\2\2\2\u0663\u0660\3\2\2\2\u0664\u0667\3\2\2")
        buf.write(u"\2\u0665\u0663\3\2\2\2\u0665\u0666\3\2\2\2\u0666\u00d7")
        buf.write(u"\3\2\2\2\u0667\u0665\3\2\2\2\u0668\u066c\5\32\16\2\u0669")
        buf.write(u"\u066c\5\26\f\2\u066a\u066c\5*\26\2\u066b\u0668\3\2\2")
        buf.write(u"\2\u066b\u0669\3\2\2\2\u066b\u066a\3\2\2\2\u066c\u00d9")
        buf.write(u"\3\2\2\2\u066d\u066e\7\13\2\2\u066e\u0678\5\u0180\u00c1")
        buf.write(u"\2\u066f\u0670\7\f\2\2\u0670\u0678\5\u019a\u00ce\2\u0671")
        buf.write(u"\u0672\7\r\2\2\u0672\u0678\5\u00dco\2\u0673\u0674\7\16")
        buf.write(u"\2\2\u0674\u0678\5\u00dco\2\u0675\u0676\7\17\2\2\u0676")
        buf.write(u"\u0678\5\u00e0q\2\u0677\u066d\3\2\2\2\u0677\u066f\3\2")
        buf.write(u"\2\2\u0677\u0671\3\2\2\2\u0677\u0673\3\2\2\2\u0677\u0675")
        buf.write(u"\3\2\2\2\u0678\u00db\3\2\2\2\u0679\u067b\5\u00ba^\2\u067a")
        buf.write(u"\u067c\5\u00dep\2\u067b\u067a\3\2\2\2\u067b\u067c\3\2")
        buf.write(u"\2\2\u067c\u00dd\3\2\2\2\u067d\u067e\7k\2\2\u067e\u067f")
        buf.write(u"\5\u0128\u0095\2\u067f\u0680\7\21\2\2\u0680\u0685\5\u00ba")
        buf.write(u"^\2\u0681\u0682\7\25\2\2\u0682\u0684\5\u00ba^\2\u0683")
        buf.write(u"\u0681\3\2\2\2\u0684\u0687\3\2\2\2\u0685\u0683\3\2\2")
        buf.write(u"\2\u0685\u0686\3\2\2\2\u0686\u00df\3\2\2\2\u0687\u0685")
        buf.write(u"\3\2\2\2\u0688\u068a\5\u00ba^\2\u0689\u068b\5\u00e2r")
        buf.write(u"\2\u068a\u0689\3\2\2\2\u068a\u068b\3\2\2\2\u068b\u00e1")
        buf.write(u"\3\2\2\2\u068c\u068d\7k\2\2\u068d\u068e\5\u0128\u0095")
        buf.write(u"\2\u068e\u0690\7\21\2\2\u068f\u0691\7%\2\2\u0690\u068f")
        buf.write(u"\3\2\2\2\u0690\u0691\3\2\2\2\u0691\u0692\3\2\2\2\u0692")
        buf.write(u"\u0697\5\u0150\u00a9\2\u0693\u0694\7%\2\2\u0694\u0696")
        buf.write(u"\5\u0150\u00a9\2\u0695\u0693\3\2\2\2\u0696\u0699\3\2")
        buf.write(u"\2\2\u0697\u0695\3\2\2\2\u0697\u0698\3\2\2\2\u0698\u069c")
        buf.write(u"\3\2\2\2\u0699\u0697\3\2\2\2\u069a\u069b\7\25\2\2\u069b")
        buf.write(u"\u069d\5\u0150\u00a9\2\u069c\u069a\3\2\2\2\u069c\u069d")
        buf.write(u"\3\2\2\2\u069d\u00e3\3\2\2\2\u069e\u06a3\5\u00bc_\2\u069f")
        buf.write(u"\u06a0\7\23\2\2\u06a0\u06a2\5\u00bc_\2\u06a1\u069f\3")
        buf.write(u"\2\2\2\u06a2\u06a5\3\2\2\2\u06a3\u06a1\3\2\2\2\u06a3")
        buf.write(u"\u06a4\3\2\2\2\u06a4\u00e5\3\2\2\2\u06a5\u06a3\3\2\2")
        buf.write(u"\2\u06a6\u06ab\5\u00be`\2\u06a7\u06a8\7\23\2\2\u06a8")
        buf.write(u"\u06aa\5\u00be`\2\u06a9\u06a7\3\2\2\2\u06aa\u06ad\3\2")
        buf.write(u"\2\2\u06ab\u06a9\3\2\2\2\u06ab\u06ac\3\2\2\2\u06ac\u00e7")
        buf.write(u"\3\2\2\2\u06ad\u06ab\3\2\2\2\u06ae\u06b3\5&\24\2\u06af")
        buf.write(u"\u06b3\5(\25\2\u06b0\u06b3\5*\26\2\u06b1\u06b3\5,\27")
        buf.write(u"\2\u06b2\u06ae\3\2\2\2\u06b2\u06af\3\2\2\2\u06b2\u06b0")
        buf.write(u"\3\2\2\2\u06b2\u06b1\3\2\2\2\u06b3\u00e9\3\2\2\2\u06b4")
        buf.write(u"\u06b5\7\n\2\2\u06b5\u00eb\3\2\2\2\u06b6\u06bc\5\u00ee")
        buf.write(u"x\2\u06b7\u06b8\5\u0086D\2\u06b8\u06b9\5\u00eex\2\u06b9")
        buf.write(u"\u06bb\3\2\2\2\u06ba\u06b7\3\2\2\2\u06bb\u06be\3\2\2")
        buf.write(u"\2\u06bc\u06ba\3\2\2\2\u06bc\u06bd\3\2\2\2\u06bd\u00ed")
        buf.write(u"\3\2\2\2\u06be\u06bc\3\2\2\2\u06bf\u06c0\7\13\2\2\u06c0")
        buf.write(u"\u06ca\5\u016a\u00b6\2\u06c1\u06c2\7\f\2\2\u06c2\u06ca")
        buf.write(u"\5\u0186\u00c4\2\u06c3\u06c4\7\r\2\2\u06c4\u06ca\5\u00f0")
        buf.write(u"y\2\u06c5\u06c6\7\16\2\2\u06c6\u06ca\5\u00f0y\2\u06c7")
        buf.write(u"\u06c8\7\17\2\2\u06c8\u06ca\5\u00f2z\2\u06c9\u06bf\3")
        buf.write(u"\2\2\2\u06c9\u06c1\3\2\2\2\u06c9\u06c3\3\2\2\2\u06c9")
        buf.write(u"\u06c5\3\2\2\2\u06c9\u06c7\3\2\2\2\u06ca\u00ef\3\2\2")
        buf.write(u"\2\u06cb\u06cd\5\u0152\u00aa\2\u06cc\u06ce\7\22\2\2\u06cd")
        buf.write(u"\u06cc\3\2\2\2\u06cd\u06ce\3\2\2\2\u06ce\u06d0\3\2\2")
        buf.write(u"\2\u06cf\u06d1\5\u00dep\2\u06d0\u06cf\3\2\2\2\u06d0\u06d1")
        buf.write(u"\3\2\2\2\u06d1\u00f1\3\2\2\2\u06d2\u06d4\5\u0138\u009d")
        buf.write(u"\2\u06d3\u06d5\7\22\2\2\u06d4\u06d3\3\2\2\2\u06d4\u06d5")
        buf.write(u"\3\2\2\2\u06d5\u06d7\3\2\2\2\u06d6\u06d8\5\u00e2r\2\u06d7")
        buf.write(u"\u06d6\3\2\2\2\u06d7\u06d8\3\2\2\2\u06d8\u00f3\3\2\2")
        buf.write(u"\2\u06d9\u06df\5\64\33\2\u06da\u06db\5\u0086D\2\u06db")
        buf.write(u"\u06dc\5\64\33\2\u06dc\u06de\3\2\2\2\u06dd\u06da\3\2")
        buf.write(u"\2\2\u06de\u06e1\3\2\2\2\u06df\u06dd\3\2\2\2\u06df\u06e0")
        buf.write(u"\3\2\2\2\u06e0\u00f5\3\2\2\2\u06e1\u06df\3\2\2\2\u06e2")
        buf.write(u"\u06e8\5.\30\2\u06e3\u06e4\5\u0086D\2\u06e4\u06e5\5.")
        buf.write(u"\30\2\u06e5\u06e7\3\2\2\2\u06e6\u06e3\3\2\2\2\u06e7\u06ea")
        buf.write(u"\3\2\2\2\u06e8\u06e6\3\2\2\2\u06e8\u06e9\3\2\2\2\u06e9")
        buf.write(u"\u00f7\3\2\2\2\u06ea\u06e8\3\2\2\2\u06eb\u06f1\5B\"\2")
        buf.write(u"\u06ec\u06ed\5\u0086D\2\u06ed\u06ee\5B\"\2\u06ee\u06f0")
        buf.write(u"\3\2\2\2\u06ef\u06ec\3\2\2\2\u06f0\u06f3\3\2\2\2\u06f1")
        buf.write(u"\u06ef\3\2\2\2\u06f1\u06f2\3\2\2\2\u06f2\u00f9\3\2\2")
        buf.write(u"\2\u06f3\u06f1\3\2\2\2\u06f4\u06fa\5R*\2\u06f5\u06f6")
        buf.write(u"\5\u0086D\2\u06f6\u06f7\5R*\2\u06f7\u06f9\3\2\2\2\u06f8")
        buf.write(u"\u06f5\3\2\2\2\u06f9\u06fc\3\2\2\2\u06fa\u06f8\3\2\2")
        buf.write(u"\2\u06fa\u06fb\3\2\2\2\u06fb\u00fb\3\2\2\2\u06fc\u06fa")
        buf.write(u"\3\2\2\2\u06fd\u06fe\7\30\2\2\u06fe\u06ff\5\u00fe\u0080")
        buf.write(u"\2\u06ff\u0700\7\24\2\2\u0700\u0701\5\u00fe\u0080\2\u0701")
        buf.write(u"\u0702\7\31\2\2\u0702\u070c\3\2\2\2\u0703\u0704\7\30")
        buf.write(u"\2\2\u0704\u0705\5\u0100\u0081\2\u0705\u0706\7\31\2\2")
        buf.write(u"\u0706\u070c\3\2\2\2\u0707\u0708\7*\2\2\u0708\u0709\5")
        buf.write(u"\u0100\u0081\2\u0709\u070a\7(\2\2\u070a\u070c\3\2\2\2")
        buf.write(u"\u070b\u06fd\3\2\2\2\u070b\u0703\3\2\2\2\u070b\u0707")
        buf.write(u"\3\2\2\2\u070c\u00fd\3\2\2\2\u070d\u071c\7\u009f\2\2")
        buf.write(u"\u070e\u071c\7\u00a0\2\2\u070f\u071c\7\u00a8\2\2\u0710")
        buf.write(u"\u071c\7\u00a9\2\2\u0711\u071c\7\u009e\2\2\u0712\u071c")
        buf.write(u"\7\u00ad\2\2\u0713\u071c\7\u00ac\2\2\u0714\u071c\7\u00a6")
        buf.write(u"\2\2\u0715\u071c\7\u00aa\2\2\u0716\u071c\7\u00ab\2\2")
        buf.write(u"\u0717\u071c\7\u009d\2\2\u0718\u071c\7\u00ae\2\2\u0719")
        buf.write(u"\u071c\7\u00a7\2\2\u071a\u071c\5\u008cG\2\u071b\u070d")
        buf.write(u"\3\2\2\2\u071b\u070e\3\2\2\2\u071b\u070f\3\2\2\2\u071b")
        buf.write(u"\u0710\3\2\2\2\u071b\u0711\3\2\2\2\u071b\u0712\3\2\2")
        buf.write(u"\2\u071b\u0713\3\2\2\2\u071b\u0714\3\2\2\2\u071b\u0715")
        buf.write(u"\3\2\2\2\u071b\u0716\3\2\2\2\u071b\u0717\3\2\2\2\u071b")
        buf.write(u"\u0718\3\2\2\2\u071b\u0719\3\2\2\2\u071b\u071a\3\2\2")
        buf.write(u"\2\u071c\u00ff\3\2\2\2\u071d\u0722\5\u00fe\u0080\2\u071e")
        buf.write(u"\u071f\7\23\2\2\u071f\u0721\5\u00fe\u0080\2\u0720\u071e")
        buf.write(u"\3\2\2\2\u0721\u0724\3\2\2\2\u0722\u0720\3\2\2\2\u0722")
        buf.write(u"\u0723\3\2\2\2\u0723\u0101\3\2\2\2\u0724\u0722\3\2\2")
        buf.write(u"\2\u0725\u072a\5\u0106\u0084\2\u0726\u072a\5\u0108\u0085")
        buf.write(u"\2\u0727\u072a\5\u00ba^\2\u0728\u072a\5\u0104\u0083\2")
        buf.write(u"\u0729\u0725\3\2\2\2\u0729\u0726\3\2\2\2\u0729\u0727")
        buf.write(u"\3\2\2\2\u0729\u0728\3\2\2\2\u072a\u0103\3\2\2\2\u072b")
        buf.write(u"\u072c\t\4\2\2\u072c\u0105\3\2\2\2\u072d\u072e\7\26\2")
        buf.write(u"\2\u072e\u072f\5X-\2\u072f\u0730\7\27\2\2\u0730\u0107")
        buf.write(u"\3\2\2\2\u0731\u0734\5\u00fe\u0080\2\u0732\u0734\5\u010a")
        buf.write(u"\u0086\2\u0733\u0731\3\2\2\2\u0733\u0732\3\2\2\2\u0734")
        buf.write(u"\u0109\3\2\2\2\u0735\u073b\5\u00a6T\2\u0736\u073b\5\u00a0")
        buf.write(u"Q\2\u0737\u073b\5\u00a2R\2\u0738\u073b\5\u010e\u0088")
        buf.write(u"\2\u0739\u073b\5\u010c\u0087\2\u073a\u0735\3\2\2\2\u073a")
        buf.write(u"\u0736\3\2\2\2\u073a\u0737\3\2\2\2\u073a\u0738\3\2\2")
        buf.write(u"\2\u073a\u0739\3\2\2\2\u073b\u010b\3\2\2\2\u073c\u073e")
        buf.write(u"\7v\2\2\u073d\u073c\3\2\2\2\u073d\u073e\3\2\2\2\u073e")
        buf.write(u"\u073f\3\2\2\2\u073f\u0741\7\26\2\2\u0740\u0742\5\u0110")
        buf.write(u"\u0089\2\u0741\u0740\3\2\2\2\u0741\u0742\3\2\2\2\u0742")
        buf.write(u"\u0743\3\2\2\2\u0743\u0744\7\27\2\2\u0744\u010d\3\2\2")
        buf.write(u"\2\u0745\u0747\7v\2\2\u0746\u0745\3\2\2\2\u0746\u0747")
        buf.write(u"\3\2\2\2\u0747\u0748\3\2\2\2\u0748\u074a\7\32\2\2\u0749")
        buf.write(u"\u074b\5\u0112\u008a\2\u074a\u0749\3\2\2\2\u074a\u074b")
        buf.write(u"\3\2\2\2\u074b\u074c\3\2\2\2\u074c\u074d\7\33\2\2\u074d")
        buf.write(u"\u010f\3\2\2\2\u074e\u074f\5X-\2\u074f\u0758\7\23\2\2")
        buf.write(u"\u0750\u0755\5X-\2\u0751\u0752\7\23\2\2\u0752\u0754\5")
        buf.write(u"X-\2\u0753\u0751\3\2\2\2\u0754\u0757\3\2\2\2\u0755\u0753")
        buf.write(u"\3\2\2\2\u0755\u0756\3\2\2\2\u0756\u0759\3\2\2\2\u0757")
        buf.write(u"\u0755\3\2\2\2\u0758\u0750\3\2\2\2\u0758\u0759\3\2\2")
        buf.write(u"\2\u0759\u0111\3\2\2\2\u075a\u075f\5\u0114\u008b\2\u075b")
        buf.write(u"\u075c\7\23\2\2\u075c\u075e\5\u0114\u008b\2\u075d\u075b")
        buf.write(u"\3\2\2\2\u075e\u0761\3\2\2\2\u075f\u075d\3\2\2\2\u075f")
        buf.write(u"\u0760\3\2\2\2\u0760\u0113\3\2\2\2\u0761\u075f\3\2\2")
        buf.write(u"\2\u0762\u0763\5X-\2\u0763\u0764\7\21\2\2\u0764\u0765")
        buf.write(u"\5X-\2\u0765\u0115\3\2\2\2\u0766\u0767\5X-\2\u0767\u0768")
        buf.write(u"\7\21\2\2\u0768\u0769\5X-\2\u0769\u0770\3\2\2\2\u076a")
        buf.write(u"\u076b\5X-\2\u076b\u076c\7\21\2\2\u076c\u0770\3\2\2\2")
        buf.write(u"\u076d\u076e\7\21\2\2\u076e\u0770\5X-\2\u076f\u0766\3")
        buf.write(u"\2\2\2\u076f\u076a\3\2\2\2\u076f\u076d\3\2\2\2\u0770")
        buf.write(u"\u0117\3\2\2\2\u0771\u0772\5\u00bc_\2\u0772\u0773\5\u012e")
        buf.write(u"\u0098\2\u0773\u0774\5X-\2\u0774\u0119\3\2\2\2\u0775")
        buf.write(u"\u0776\b\u008e\1\2\u0776\u0777\5\u00bc_\2\u0777\u077c")
        buf.write(u"\3\2\2\2\u0778\u0779\f\3\2\2\u0779\u077b\5\u0080A\2\u077a")
        buf.write(u"\u0778\3\2\2\2\u077b\u077e\3\2\2\2\u077c\u077a\3\2\2")
        buf.write(u"\2\u077c\u077d\3\2\2\2\u077d\u011b\3\2\2\2\u077e\u077c")
        buf.write(u"\3\2\2\2\u077f\u0780\6\u008f\60\3\u0780\u0781\7\u00a3")
        buf.write(u"\2\2\u0781\u0784\5\u00ceh\2\u0782\u0784\5X-\2\u0783\u077f")
        buf.write(u"\3\2\2\2\u0783\u0782\3\2\2\2\u0784\u011d\3\2\2\2\u0785")
        buf.write(u"\u078a\5\u0120\u0091\2\u0786\u0787\7\23\2\2\u0787\u0789")
        buf.write(u"\5\u0120\u0091\2\u0788\u0786\3\2\2\2\u0789\u078c\3\2")
        buf.write(u"\2\2\u078a\u0788\3\2\2\2\u078a\u078b\3\2\2\2\u078b\u011f")
        buf.write(u"\3\2\2\2\u078c\u078a\3\2\2\2\u078d\u0792\5\u00bc_\2\u078e")
        buf.write(u"\u078f\7\25\2\2\u078f\u0791\5\u00bc_\2\u0790\u078e\3")
        buf.write(u"\2\2\2\u0791\u0794\3\2\2\2\u0792\u0790\3\2\2\2\u0792")
        buf.write(u"\u0793\3\2\2\2\u0793\u0796\3\2\2\2\u0794\u0792\3\2\2")
        buf.write(u"\2\u0795\u0797\t\5\2\2\u0796\u0795\3\2\2\2\u0796\u0797")
        buf.write(u"\3\2\2\2\u0797\u0121\3\2\2\2\u0798\u079f\7\"\2\2\u0799")
        buf.write(u"\u079f\7#\2\2\u079a\u079f\5\u0130\u0099\2\u079b\u079f")
        buf.write(u"\5\u0132\u009a\2\u079c\u079f\5\u0134\u009b\2\u079d\u079f")
        buf.write(u"\5\u0136\u009c\2\u079e\u0798\3\2\2\2\u079e\u0799\3\2")
        buf.write(u"\2\2\u079e\u079a\3\2\2\2\u079e\u079b\3\2\2\2\u079e\u079c")
        buf.write(u"\3\2\2\2\u079e\u079d\3\2\2\2\u079f\u0123\3\2\2\2\u07a0")
        buf.write(u"\u07a1\7\u00a3\2\2\u07a1\u07a2\6\u0093\61\3\u07a2\u0125")
        buf.write(u"\3\2\2\2\u07a3\u07a4\7\u00a3\2\2\u07a4\u07a5\6\u0094")
        buf.write(u"\62\3\u07a5\u0127\3\2\2\2\u07a6\u07a7\7\u00a3\2\2\u07a7")
        buf.write(u"\u07a8\6\u0095\63\3\u07a8\u0129\3\2\2\2\u07a9\u07aa\7")
        buf.write(u"\u00a3\2\2\u07aa\u07ab\6\u0096\64\3\u07ab\u012b\3\2\2")
        buf.write(u"\2\u07ac\u07ad\7\u00a3\2\2\u07ad\u07ae\6\u0097\65\3\u07ae")
        buf.write(u"\u012d\3\2\2\2\u07af\u07b0\7-\2\2\u07b0\u012f\3\2\2\2")
        buf.write(u"\u07b1\u07b2\7$\2\2\u07b2\u0131\3\2\2\2\u07b3\u07b4\7")
        buf.write(u"%\2\2\u07b4\u0133\3\2\2\2\u07b5\u07b6\7&\2\2\u07b6\u0135")
        buf.write(u"\3\2\2\2\u07b7\u07b8\t\6\2\2\u07b8\u0137\3\2\2\2\u07b9")
        buf.write(u"\u07ba\7\u0088\2\2\u07ba\u07bb\5\u013a\u009e\2\u07bb")
        buf.write(u"\u07bc\7\22\2\2\u07bc\u07c1\3\2\2\2\u07bd\u07be\5\u013a")
        buf.write(u"\u009e\2\u07be\u07bf\7\22\2\2\u07bf\u07c1\3\2\2\2\u07c0")
        buf.write(u"\u07b9\3\2\2\2\u07c0\u07bd\3\2\2\2\u07c1\u0139\3\2\2")
        buf.write(u"\2\u07c2\u07c3\b\u009e\1\2\u07c3\u07c4\5\u013c\u009f")
        buf.write(u"\2\u07c4\u07c9\3\2\2\2\u07c5\u07c6\f\3\2\2\u07c6\u07c8")
        buf.write(u"\5\u0142\u00a2\2\u07c7\u07c5\3\2\2\2\u07c8\u07cb\3\2")
        buf.write(u"\2\2\u07c9\u07c7\3\2\2\2\u07c9\u07ca\3\2\2\2\u07ca\u013b")
        buf.write(u"\3\2\2\2\u07cb\u07c9\3\2\2\2\u07cc\u07d4\5\u013e\u00a0")
        buf.write(u"\2\u07cd\u07d4\5\u0140\u00a1\2\u07ce\u07d4\5\u014a\u00a6")
        buf.write(u"\2\u07cf\u07d4\5\u014c\u00a7\2\u07d0\u07d4\5\u014e\u00a8")
        buf.write(u"\2\u07d1\u07d4\5\u0144\u00a3\2\u07d2\u07d4\5\u0148\u00a5")
        buf.write(u"\2\u07d3\u07cc\3\2\2\2\u07d3\u07cd\3\2\2\2\u07d3\u07ce")
        buf.write(u"\3\2\2\2\u07d3\u07cf\3\2\2\2\u07d3\u07d0\3\2\2\2\u07d3")
        buf.write(u"\u07d1\3\2\2\2\u07d3\u07d2\3\2\2\2\u07d4\u013d\3\2\2")
        buf.write(u"\2\u07d5\u07d6\5\u0104\u0083\2\u07d6\u013f\3\2\2\2\u07d7")
        buf.write(u"\u07d8\5\u0124\u0093\2\u07d8\u07d9\5\u0144\u00a3\2\u07d9")
        buf.write(u"\u0141\3\2\2\2\u07da\u07db\7\25\2\2\u07db\u07e0\5\u0144")
        buf.write(u"\u00a3\2\u07dc\u07dd\7\25\2\2\u07dd\u07e0\5\u0150\u00a9")
        buf.write(u"\2\u07de\u07e0\5\u0148\u00a5\2\u07df\u07da\3\2\2\2\u07df")
        buf.write(u"\u07dc\3\2\2\2\u07df\u07de\3\2\2\2\u07e0\u0143\3\2\2")
        buf.write(u"\2\u07e1\u07e2\5\u0150\u00a9\2\u07e2\u07e4\7\26\2\2\u07e3")
        buf.write(u"\u07e5\5\u0146\u00a4\2\u07e4\u07e3\3\2\2\2\u07e4\u07e5")
        buf.write(u"\3\2\2\2\u07e5\u07e6\3\2\2\2\u07e6\u07e7\7\27\2\2\u07e7")
        buf.write(u"\u0145\3\2\2\2\u07e8\u07e9\b\u00a4\1\2\u07e9\u07ea\5")
        buf.write(u"\u013a\u009e\2\u07ea\u07f0\3\2\2\2\u07eb\u07ec\f\3\2")
        buf.write(u"\2\u07ec\u07ed\7\23\2\2\u07ed\u07ef\5\u013a\u009e\2\u07ee")
        buf.write(u"\u07eb\3\2\2\2\u07ef\u07f2\3\2\2\2\u07f0\u07ee\3\2\2")
        buf.write(u"\2\u07f0\u07f1\3\2\2\2\u07f1\u0147\3\2\2\2\u07f2\u07f0")
        buf.write(u"\3\2\2\2\u07f3\u07f4\7\30\2\2\u07f4\u07f5\5\u013a\u009e")
        buf.write(u"\2\u07f5\u07f6\7\31\2\2\u07f6\u0149\3\2\2\2\u07f7\u07f8")
        buf.write(u"\7\26\2\2\u07f8\u07f9\5\u013a\u009e\2\u07f9\u07fa\7\27")
        buf.write(u"\2\2\u07fa\u014b\3\2\2\2\u07fb\u07fc\5\u0150\u00a9\2")
        buf.write(u"\u07fc\u014d\3\2\2\2\u07fd\u0803\7\u00a8\2\2\u07fe\u0803")
        buf.write(u"\7\u00aa\2\2\u07ff\u0803\7\u00a6\2\2\u0800\u0803\7\u009d")
        buf.write(u"\2\2\u0801\u0803\7\u009e\2\2\u0802\u07fd\3\2\2\2\u0802")
        buf.write(u"\u07fe\3\2\2\2\u0802\u07ff\3\2\2\2\u0802\u0800\3\2\2")
        buf.write(u"\2\u0802\u0801\3\2\2\2\u0803\u014f\3\2\2\2\u0804\u0805")
        buf.write(u"\t\7\2\2\u0805\u0151\3\2\2\2\u0806\u0807\7\u0088\2\2")
        buf.write(u"\u0807\u080a\5\u0154\u00ab\2\u0808\u080a\5\u0154\u00ab")
        buf.write(u"\2\u0809\u0806\3\2\2\2\u0809\u0808\3\2\2\2\u080a\u0153")
        buf.write(u"\3\2\2\2\u080b\u080c\b\u00ab\1\2\u080c\u080d\5\u0156")
        buf.write(u"\u00ac\2\u080d\u0812\3\2\2\2\u080e\u080f\f\3\2\2\u080f")
        buf.write(u"\u0811\5\u0158\u00ad\2\u0810\u080e\3\2\2\2\u0811\u0814")
        buf.write(u"\3\2\2\2\u0812\u0810\3\2\2\2\u0812\u0813\3\2\2\2\u0813")
        buf.write(u"\u0155\3\2\2\2\u0814\u0812\3\2\2\2\u0815\u081a\5\u0162")
        buf.write(u"\u00b2\2\u0816\u081a\5\u0164\u00b3\2\u0817\u081a\5\u0166")
        buf.write(u"\u00b4\2\u0818\u081a\5\u015a\u00ae\2\u0819\u0815\3\2")
        buf.write(u"\2\2\u0819\u0816\3\2\2\2\u0819\u0817\3\2\2\2\u0819\u0818")
        buf.write(u"\3\2\2\2\u081a\u0157\3\2\2\2\u081b\u081c\7\25\2\2\u081c")
        buf.write(u"\u0822\5\u015a\u00ae\2\u081d\u081e\7\30\2\2\u081e\u081f")
        buf.write(u"\5\u0154\u00ab\2\u081f\u0820\7\31\2\2\u0820\u0822\3\2")
        buf.write(u"\2\2\u0821\u081b\3\2\2\2\u0821\u081d\3\2\2\2\u0822\u0159")
        buf.write(u"\3\2\2\2\u0823\u0824\5\u0168\u00b5\2\u0824\u0826\7\26")
        buf.write(u"\2\2\u0825\u0827\5\u015c\u00af\2\u0826\u0825\3\2\2\2")
        buf.write(u"\u0826\u0827\3\2\2\2\u0827\u0828\3\2\2\2\u0828\u0829")
        buf.write(u"\7\27\2\2\u0829\u015b\3\2\2\2\u082a\u0831\5\u015e\u00b0")
        buf.write(u"\2\u082b\u0831\5\u0160\u00b1\2\u082c\u082d\5\u015e\u00b0")
        buf.write(u"\2\u082d\u082e\7\23\2\2\u082e\u082f\5\u0160\u00b1\2\u082f")
        buf.write(u"\u0831\3\2\2\2\u0830\u082a\3\2\2\2\u0830\u082b\3\2\2")
        buf.write(u"\2\u0830\u082c\3\2\2\2\u0831\u015d\3\2\2\2\u0832\u0833")
        buf.write(u"\b\u00b0\1\2\u0833\u0834\5\u0154\u00ab\2\u0834\u083a")
        buf.write(u"\3\2\2\2\u0835\u0836\f\3\2\2\u0836\u0837\7\23\2\2\u0837")
        buf.write(u"\u0839\5\u0154\u00ab\2\u0838\u0835\3\2\2\2\u0839\u083c")
        buf.write(u"\3\2\2\2\u083a\u0838\3\2\2\2\u083a\u083b\3\2\2\2\u083b")
        buf.write(u"\u015f\3\2\2\2\u083c\u083a\3\2\2\2\u083d\u083e\b\u00b1")
        buf.write(u"\1\2\u083e\u083f\5\u0168\u00b5\2\u083f\u0840\7-\2\2\u0840")
        buf.write(u"\u0841\5\u0154\u00ab\2\u0841\u084a\3\2\2\2\u0842\u0843")
        buf.write(u"\f\3\2\2\u0843\u0844\7\23\2\2\u0844\u0845\5\u0168\u00b5")
        buf.write(u"\2\u0845\u0846\7-\2\2\u0846\u0847\5\u0154\u00ab\2\u0847")
        buf.write(u"\u0849\3\2\2\2\u0848\u0842\3\2\2\2\u0849\u084c\3\2\2")
        buf.write(u"\2\u084a\u0848\3\2\2\2\u084a\u084b\3\2\2\2\u084b\u0161")
        buf.write(u"\3\2\2\2\u084c\u084a\3\2\2\2\u084d\u084e\7\26\2\2\u084e")
        buf.write(u"\u084f\5\u0154\u00ab\2\u084f\u0850\7\27\2\2\u0850\u0163")
        buf.write(u"\3\2\2\2\u0851\u0852\b\u00b3\1\2\u0852\u0855\7\u00a5")
        buf.write(u"\2\2\u0853\u0855\5\u0168\u00b5\2\u0854\u0851\3\2\2\2")
        buf.write(u"\u0854\u0853\3\2\2\2\u0855\u085b\3\2\2\2\u0856\u0857")
        buf.write(u"\f\3\2\2\u0857\u0858\7\25\2\2\u0858\u085a\5\u0168\u00b5")
        buf.write(u"\2\u0859\u0856\3\2\2\2\u085a\u085d\3\2\2\2\u085b\u0859")
        buf.write(u"\3\2\2\2\u085b\u085c\3\2\2\2\u085c\u0165\3\2\2\2\u085d")
        buf.write(u"\u085b\3\2\2\2\u085e\u0864\7\u00a8\2\2\u085f\u0864\7")
        buf.write(u"\u00aa\2\2\u0860\u0864\7\u00a6\2\2\u0861\u0864\7\u009d")
        buf.write(u"\2\2\u0862\u0864\7\u009e\2\2\u0863\u085e\3\2\2\2\u0863")
        buf.write(u"\u085f\3\2\2\2\u0863\u0860\3\2\2\2\u0863\u0861\3\2\2")
        buf.write(u"\2\u0863\u0862\3\2\2\2\u0864\u0167\3\2\2\2\u0865\u0866")
        buf.write(u"\t\b\2\2\u0866\u0169\3\2\2\2\u0867\u0868\7\u0088\2\2")
        buf.write(u"\u0868\u0869\5\u016c\u00b7\2\u0869\u086a\7\22\2\2\u086a")
        buf.write(u"\u086f\3\2\2\2\u086b\u086c\5\u016c\u00b7\2\u086c\u086d")
        buf.write(u"\7\22\2\2\u086d\u086f\3\2\2\2\u086e\u0867\3\2\2\2\u086e")
        buf.write(u"\u086b\3\2\2\2\u086f\u016b\3\2\2\2\u0870\u0871\b\u00b7")
        buf.write(u"\1\2\u0871\u0872\5\u016e\u00b8\2\u0872\u0877\3\2\2\2")
        buf.write(u"\u0873\u0874\f\3\2\2\u0874\u0876\5\u0174\u00bb\2\u0875")
        buf.write(u"\u0873\3\2\2\2\u0876\u0879\3\2\2\2\u0877\u0875\3\2\2")
        buf.write(u"\2\u0877\u0878\3\2\2\2\u0878\u016d\3\2\2\2\u0879\u0877")
        buf.write(u"\3\2\2\2\u087a\u0880\5\u0170\u00b9\2\u087b\u0880\5\u0172")
        buf.write(u"\u00ba\2\u087c\u0880\5\u017c\u00bf\2\u087d\u0880\5\u017e")
        buf.write(u"\u00c0\2\u087e\u0880\5\u0182\u00c2\2\u087f\u087a\3\2")
        buf.write(u"\2\2\u087f\u087b\3\2\2\2\u087f\u087c\3\2\2\2\u087f\u087d")
        buf.write(u"\3\2\2\2\u087f\u087e\3\2\2\2\u0880\u016f\3\2\2\2\u0881")
        buf.write(u"\u0882\5\u0104\u0083\2\u0882\u0171\3\2\2\2\u0883\u0884")
        buf.write(u"\5\u0124\u0093\2\u0884\u0885\5\u0176\u00bc\2\u0885\u0173")
        buf.write(u"\3\2\2\2\u0886\u0887\7\25\2\2\u0887\u088a\5\u0176\u00bc")
        buf.write(u"\2\u0888\u088a\5\u017a\u00be\2\u0889\u0886\3\2\2\2\u0889")
        buf.write(u"\u0888\3\2\2\2\u088a\u0175\3\2\2\2\u088b\u088c\5\u0184")
        buf.write(u"\u00c3\2\u088c\u088e\7\26\2\2\u088d\u088f\5\u0178\u00bd")
        buf.write(u"\2\u088e\u088d\3\2\2\2\u088e\u088f\3\2\2\2\u088f\u0890")
        buf.write(u"\3\2\2\2\u0890\u0891\7\27\2\2\u0891\u0177\3\2\2\2\u0892")
        buf.write(u"\u0893\b\u00bd\1\2\u0893\u0894\5\u016c\u00b7\2\u0894")
        buf.write(u"\u089a\3\2\2\2\u0895\u0896\f\3\2\2\u0896\u0897\7\23\2")
        buf.write(u"\2\u0897\u0899\5\u016c\u00b7\2\u0898\u0895\3\2\2\2\u0899")
        buf.write(u"\u089c\3\2\2\2\u089a\u0898\3\2\2\2\u089a\u089b\3\2\2")
        buf.write(u"\2\u089b\u0179\3\2\2\2\u089c\u089a\3\2\2\2\u089d\u089e")
        buf.write(u"\7\30\2\2\u089e\u089f\5\u016c\u00b7\2\u089f\u08a0\7\31")
        buf.write(u"\2\2\u08a0\u017b\3\2\2\2\u08a1\u08a2\7\26\2\2\u08a2\u08a3")
        buf.write(u"\5\u016c\u00b7\2\u08a3\u08a4\7\27\2\2\u08a4\u017d\3\2")
        buf.write(u"\2\2\u08a5\u08a6\b\u00c0\1\2\u08a6\u08a7\5\u0184\u00c3")
        buf.write(u"\2\u08a7\u08ad\3\2\2\2\u08a8\u08a9\f\3\2\2\u08a9\u08aa")
        buf.write(u"\7\25\2\2\u08aa\u08ac\5\u0184\u00c3\2\u08ab\u08a8\3\2")
        buf.write(u"\2\2\u08ac\u08af\3\2\2\2\u08ad\u08ab\3\2\2\2\u08ad\u08ae")
        buf.write(u"\3\2\2\2\u08ae\u017f\3\2\2\2\u08af\u08ad\3\2\2\2\u08b0")
        buf.write(u"\u08b1\b\u00c1\1\2\u08b1\u08b2\5\u017e\u00c0\2\u08b2")
        buf.write(u"\u08b7\3\2\2\2\u08b3\u08b4\f\3\2\2\u08b4\u08b6\7\u00a5")
        buf.write(u"\2\2\u08b5\u08b3\3\2\2\2\u08b6\u08b9\3\2\2\2\u08b7\u08b5")
        buf.write(u"\3\2\2\2\u08b7\u08b8\3\2\2\2\u08b8\u0181\3\2\2\2\u08b9")
        buf.write(u"\u08b7\3\2\2\2\u08ba\u08c0\7\u00a8\2\2\u08bb\u08c0\7")
        buf.write(u"\u00aa\2\2\u08bc\u08c0\7\u00a6\2\2\u08bd\u08c0\7\u009d")
        buf.write(u"\2\2\u08be\u08c0\7\u009e\2\2\u08bf\u08ba\3\2\2\2\u08bf")
        buf.write(u"\u08bb\3\2\2\2\u08bf\u08bc\3\2\2\2\u08bf\u08bd\3\2\2")
        buf.write(u"\2\u08bf\u08be\3\2\2\2\u08c0\u0183\3\2\2\2\u08c1\u08c2")
        buf.write(u"\t\t\2\2\u08c2\u0185\3\2\2\2\u08c3\u08c4\7\u0088\2\2")
        buf.write(u"\u08c4\u08c5\5\u0188\u00c5\2\u08c5\u08c6\7\22\2\2\u08c6")
        buf.write(u"\u08cb\3\2\2\2\u08c7\u08c8\5\u0188\u00c5\2\u08c8\u08c9")
        buf.write(u"\7\22\2\2\u08c9\u08cb\3\2\2\2\u08ca\u08c3\3\2\2\2\u08ca")
        buf.write(u"\u08c7\3\2\2\2\u08cb\u0187\3\2\2\2\u08cc\u08cd\b\u00c5")
        buf.write(u"\1\2\u08cd\u08ce\5\u018a\u00c6\2\u08ce\u08d3\3\2\2\2")
        buf.write(u"\u08cf\u08d0\f\3\2\2\u08d0\u08d2\5\u0190\u00c9\2\u08d1")
        buf.write(u"\u08cf\3\2\2\2\u08d2\u08d5\3\2\2\2\u08d3\u08d1\3\2\2")
        buf.write(u"\2\u08d3\u08d4\3\2\2\2\u08d4\u0189\3\2\2\2\u08d5\u08d3")
        buf.write(u"\3\2\2\2\u08d6\u08dc\5\u018c\u00c7\2\u08d7\u08dc\5\u018e")
        buf.write(u"\u00c8\2\u08d8\u08dc\5\u0198\u00cd\2\u08d9\u08dc\5\u019a")
        buf.write(u"\u00ce\2\u08da\u08dc\5\u019c\u00cf\2\u08db\u08d6\3\2")
        buf.write(u"\2\2\u08db\u08d7\3\2\2\2\u08db\u08d8\3\2\2\2\u08db\u08d9")
        buf.write(u"\3\2\2\2\u08db\u08da\3\2\2\2\u08dc\u018b\3\2\2\2\u08dd")
        buf.write(u"\u08de\5\u0104\u0083\2\u08de\u018d\3\2\2\2\u08df\u08e0")
        buf.write(u"\5\u0124\u0093\2\u08e0\u08e1\5\u0192\u00ca\2\u08e1\u018f")
        buf.write(u"\3\2\2\2\u08e2\u08e3\7\25\2\2\u08e3\u08e6\5\u0192\u00ca")
        buf.write(u"\2\u08e4\u08e6\5\u0196\u00cc\2\u08e5\u08e2\3\2\2\2\u08e5")
        buf.write(u"\u08e4\3\2\2\2\u08e6\u0191\3\2\2\2\u08e7\u08e8\5\u019e")
        buf.write(u"\u00d0\2\u08e8\u08ea\7\26\2\2\u08e9\u08eb\5\u0194\u00cb")
        buf.write(u"\2\u08ea\u08e9\3\2\2\2\u08ea\u08eb\3\2\2\2\u08eb\u08ec")
        buf.write(u"\3\2\2\2\u08ec\u08ed\7\27\2\2\u08ed\u0193\3\2\2\2\u08ee")
        buf.write(u"\u08ef\b\u00cb\1\2\u08ef\u08f0\5\u0188\u00c5\2\u08f0")
        buf.write(u"\u08f6\3\2\2\2\u08f1\u08f2\f\3\2\2\u08f2\u08f3\7\23\2")
        buf.write(u"\2\u08f3\u08f5\5\u0188\u00c5\2\u08f4\u08f1\3\2\2\2\u08f5")
        buf.write(u"\u08f8\3\2\2\2\u08f6\u08f4\3\2\2\2\u08f6\u08f7\3\2\2")
        buf.write(u"\2\u08f7\u0195\3\2\2\2\u08f8\u08f6\3\2\2\2\u08f9\u08fa")
        buf.write(u"\7\30\2\2\u08fa\u08fb\5\u0188\u00c5\2\u08fb\u08fc\7\31")
        buf.write(u"\2\2\u08fc\u0197\3\2\2\2\u08fd\u08fe\7\26\2\2\u08fe\u08ff")
        buf.write(u"\5\u0188\u00c5\2\u08ff\u0900\7\27\2\2\u0900\u0199\3\2")
        buf.write(u"\2\2\u0901\u0902\b\u00ce\1\2\u0902\u0905\7\u00a5\2\2")
        buf.write(u"\u0903\u0905\5\u019e\u00d0\2\u0904\u0901\3\2\2\2\u0904")
        buf.write(u"\u0903\3\2\2\2\u0905\u090b\3\2\2\2\u0906\u0907\f\3\2")
        buf.write(u"\2\u0907\u0908\7\25\2\2\u0908\u090a\5\u019e\u00d0\2\u0909")
        buf.write(u"\u0906\3\2\2\2\u090a\u090d\3\2\2\2\u090b\u0909\3\2\2")
        buf.write(u"\2\u090b\u090c\3\2\2\2\u090c\u019b\3\2\2\2\u090d\u090b")
        buf.write(u"\3\2\2\2\u090e\u0914\7\u00a8\2\2\u090f\u0914\7\u00aa")
        buf.write(u"\2\2\u0910\u0914\7\u00a6\2\2\u0911\u0914\7\u009d\2\2")
        buf.write(u"\u0912\u0914\7\u009e\2\2\u0913\u090e\3\2\2\2\u0913\u090f")
        buf.write(u"\3\2\2\2\u0913\u0910\3\2\2\2\u0913\u0911\3\2\2\2\u0913")
        buf.write(u"\u0912\3\2\2\2\u0914\u019d\3\2\2\2\u0915\u0916\t\n\2")
        buf.write(u"\2\u0916\u019f\3\2\2\2\u00c7\u01a6\u01ad\u01cb\u01d1")
        buf.write(u"\u01d6\u01dc\u01de\u01e1\u01e7\u01eb\u01f6\u01ff\u020e")
        buf.write(u"\u0217\u021e\u0228\u023e\u0255\u0262\u026d\u027b\u0289")
        buf.write(u"\u0297\u02ab\u02b6\u02b8\u02c1\u02c5\u02cd\u02d1\u02dd")
        buf.write(u"\u02e2\u02e6\u0301\u0308\u030d\u0311\u0326\u0334\u0338")
        buf.write(u"\u033b\u035c\u036f\u0376\u0398\u03a1\u03b8\u03c8\u03cd")
        buf.write(u"\u03d5\u03de\u03f5\u03fb\u0419\u0480\u0482\u048c\u04a1")
        buf.write(u"\u04b1\u04b6\u04c0\u04c5\u04c7\u04cd\u04cf\u04d1\u04eb")
        buf.write(u"\u04f2\u04f5\u04fb\u04ff\u0504\u0506\u050a\u0512\u0519")
        buf.write(u"\u051b\u0520\u0522\u052d\u0540\u0549\u054f\u0554\u055b")
        buf.write(u"\u0563\u056e\u0576\u057e\u0584\u058c\u0595\u059d\u05aa")
        buf.write(u"\u05ad\u05b1\u05b6\u05ba\u05c3\u05d8\u05e2\u05e4\u05e9")
        buf.write(u"\u05f9\u05fe\u0607\u060e\u0613\u0618\u0627\u062c\u062f")
        buf.write(u"\u0633\u0638\u063f\u064a\u064c\u0655\u065d\u0665\u066b")
        buf.write(u"\u0677\u067b\u0685\u068a\u0690\u0697\u069c\u06a3\u06ab")
        buf.write(u"\u06b2\u06bc\u06c9\u06cd\u06d0\u06d4\u06d7\u06df\u06e8")
        buf.write(u"\u06f1\u06fa\u070b\u071b\u0722\u0729\u0733\u073a\u073d")
        buf.write(u"\u0741\u0746\u074a\u0755\u0758\u075f\u076f\u077c\u0783")
        buf.write(u"\u078a\u0792\u0796\u079e\u07c0\u07c9\u07d3\u07df\u07e4")
        buf.write(u"\u07f0\u0802\u0809\u0812\u0819\u0821\u0826\u0830\u083a")
        buf.write(u"\u084a\u0854\u085b\u0863\u086e\u0877\u087f\u0889\u088e")
        buf.write(u"\u089a\u08ad\u08b7\u08bf\u08ca\u08d3\u08db\u08e5\u08ea")
        buf.write(u"\u08f6\u0904\u090b\u0913")
        return buf.getvalue()
		

class EParser ( AbstractParser ):

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
    RULE_concrete_category_declaration = 5
    RULE_singleton_category_declaration = 6
    RULE_derived_list = 7
    RULE_operator_method_declaration = 8
    RULE_setter_method_declaration = 9
    RULE_native_setter_declaration = 10
    RULE_getter_method_declaration = 11
    RULE_native_getter_declaration = 12
    RULE_native_category_declaration = 13
    RULE_native_resource_declaration = 14
    RULE_native_category_bindings = 15
    RULE_native_category_binding_list = 16
    RULE_attribute_list = 17
    RULE_abstract_method_declaration = 18
    RULE_concrete_method_declaration = 19
    RULE_native_method_declaration = 20
    RULE_test_method_declaration = 21
    RULE_assertion = 22
    RULE_full_argument_list = 23
    RULE_typed_argument = 24
    RULE_statement = 25
    RULE_flush_statement = 26
    RULE_store_statement = 27
    RULE_method_call_statement = 28
    RULE_with_resource_statement = 29
    RULE_with_singleton_statement = 30
    RULE_switch_statement = 31
    RULE_switch_case_statement = 32
    RULE_for_each_statement = 33
    RULE_do_while_statement = 34
    RULE_while_statement = 35
    RULE_if_statement = 36
    RULE_else_if_statement_list = 37
    RULE_raise_statement = 38
    RULE_try_statement = 39
    RULE_catch_statement = 40
    RULE_break_statement = 41
    RULE_return_statement = 42
    RULE_expression = 43
    RULE_unresolved_expression = 44
    RULE_unresolved_selector = 45
    RULE_invocation_expression = 46
    RULE_invocation_trailer = 47
    RULE_instance_expression = 48
    RULE_instance_selector = 49
    RULE_document_expression = 50
    RULE_blob_expression = 51
    RULE_constructor_expression = 52
    RULE_read_expression = 53
    RULE_write_statement = 54
    RULE_ambiguous_expression = 55
    RULE_fetch_list_expression = 56
    RULE_fetch_store_expression = 57
    RULE_sorted_expression = 58
    RULE_argument_assignment_list = 59
    RULE_with_argument_assignment_list = 60
    RULE_argument_assignment = 61
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
    RULE_type_identifier_list = 90
    RULE_method_identifier = 91
    RULE_identifier = 92
    RULE_variable_identifier = 93
    RULE_attribute_identifier = 94
    RULE_type_identifier = 95
    RULE_symbol_identifier = 96
    RULE_argument_list = 97
    RULE_argument = 98
    RULE_operator_argument = 99
    RULE_named_argument = 100
    RULE_code_argument = 101
    RULE_category_or_any_type = 102
    RULE_any_type = 103
    RULE_member_method_declaration_list = 104
    RULE_member_method_declaration = 105
    RULE_native_member_method_declaration_list = 106
    RULE_native_member_method_declaration = 107
    RULE_native_category_binding = 108
    RULE_python_category_binding = 109
    RULE_python_module = 110
    RULE_javascript_category_binding = 111
    RULE_javascript_module = 112
    RULE_variable_identifier_list = 113
    RULE_attribute_identifier_list = 114
    RULE_method_declaration = 115
    RULE_comment_statement = 116
    RULE_native_statement_list = 117
    RULE_native_statement = 118
    RULE_python_native_statement = 119
    RULE_javascript_native_statement = 120
    RULE_statement_list = 121
    RULE_assertion_list = 122
    RULE_switch_case_statement_list = 123
    RULE_catch_statement_list = 124
    RULE_literal_collection = 125
    RULE_atomic_literal = 126
    RULE_literal_list_literal = 127
    RULE_selectable_expression = 128
    RULE_this_expression = 129
    RULE_parenthesis_expression = 130
    RULE_literal_expression = 131
    RULE_collection_literal = 132
    RULE_tuple_literal = 133
    RULE_dict_literal = 134
    RULE_expression_tuple = 135
    RULE_dict_entry_list = 136
    RULE_dict_entry = 137
    RULE_slice_arguments = 138
    RULE_assign_variable_statement = 139
    RULE_assignable_instance = 140
    RULE_is_expression = 141
    RULE_order_by_list = 142
    RULE_order_by = 143
    RULE_operator = 144
    RULE_new_token = 145
    RULE_key_token = 146
    RULE_module_token = 147
    RULE_value_token = 148
    RULE_symbols_token = 149
    RULE_assign = 150
    RULE_multiply = 151
    RULE_divide = 152
    RULE_idivide = 153
    RULE_modulo = 154
    RULE_javascript_statement = 155
    RULE_javascript_expression = 156
    RULE_javascript_primary_expression = 157
    RULE_javascript_this_expression = 158
    RULE_javascript_new_expression = 159
    RULE_javascript_selector_expression = 160
    RULE_javascript_method_expression = 161
    RULE_javascript_arguments = 162
    RULE_javascript_item_expression = 163
    RULE_javascript_parenthesis_expression = 164
    RULE_javascript_identifier_expression = 165
    RULE_javascript_literal_expression = 166
    RULE_javascript_identifier = 167
    RULE_python_statement = 168
    RULE_python_expression = 169
    RULE_python_primary_expression = 170
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
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"operator_method_declaration", u"setter_method_declaration", 
                   u"native_setter_declaration", u"getter_method_declaration", 
                   u"native_getter_declaration", u"native_category_declaration", 
                   u"native_resource_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"attribute_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"full_argument_list", 
                   u"typed_argument", u"statement", u"flush_statement", 
                   u"store_statement", u"method_call_statement", u"with_resource_statement", 
                   u"with_singleton_statement", u"switch_statement", u"switch_case_statement", 
                   u"for_each_statement", u"do_while_statement", u"while_statement", 
                   u"if_statement", u"else_if_statement_list", u"raise_statement", 
                   u"try_statement", u"catch_statement", u"break_statement", 
                   u"return_statement", u"expression", u"unresolved_expression", 
                   u"unresolved_selector", u"invocation_expression", u"invocation_trailer", 
                   u"instance_expression", u"instance_selector", u"document_expression", 
                   u"blob_expression", u"constructor_expression", u"read_expression", 
                   u"write_statement", u"ambiguous_expression", u"fetch_list_expression", 
                   u"fetch_store_expression", u"sorted_expression", u"argument_assignment_list", 
                   u"with_argument_assignment_list", u"argument_assignment", 
                   u"assign_instance_statement", u"child_instance", u"assign_tuple_statement", 
                   u"lfs", u"lfp", u"indent", u"dedent", u"null_literal", 
                   u"declaration_list", u"declarations", u"declaration", 
                   u"resource_declaration", u"enum_declaration", u"native_symbol_list", 
                   u"category_symbol_list", u"symbol_list", u"attribute_constraint", 
                   u"list_literal", u"set_literal", u"expression_list", 
                   u"range_literal", u"typedef", u"primary_type", u"native_type", 
                   u"category_type", u"mutable_category_type", u"code_type", 
                   u"category_declaration", u"type_identifier_list", u"method_identifier", 
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
        super(EParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Enum_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Enum_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.symbols = None # Category_symbol_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def ENUMERATED(self):
            return self.getToken(EParser.ENUMERATED, 0)

        def symbols_token(self):
            return self.getTypedRuleContext(EParser.Symbols_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Type_identifierContext,i)


        def category_symbol_list(self):
            return self.getTypedRuleContext(EParser.Category_symbol_listContext,0)


        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_enum_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = EParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(EParser.DEFINE)
            self.state = 415 
            localctx.name = self.type_identifier()
            self.state = 416
            self.match(EParser.AS)
            self.state = 417
            self.match(EParser.ENUMERATED)
            self.state = 420
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 418
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 419 
                localctx.derived = self.type_identifier()

            else:
                raise NoViableAltException(self)

            self.state = 427
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 422 
                localctx.attrs = self.attribute_list()
                self.state = 423
                self.match(EParser.COMMA)
                self.state = 424
                self.match(EParser.AND)
                pass

            elif la_ == 2:
                self.state = 426
                self.match(EParser.WITH)
                pass


            self.state = 429 
            self.symbols_token()
            self.state = 430
            self.match(EParser.COLON)
            self.state = 431 
            self.indent()
            self.state = 432 
            localctx.symbols = self.category_symbol_list()
            self.state = 433 
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
            super(EParser.Enum_native_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.typ = None # Native_typeContext
            self.symbols = None # Native_symbol_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def ENUMERATED(self):
            return self.getToken(EParser.ENUMERATED, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def symbols_token(self):
            return self.getTypedRuleContext(EParser.Symbols_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def native_type(self):
            return self.getTypedRuleContext(EParser.Native_typeContext,0)


        def native_symbol_list(self):
            return self.getTypedRuleContext(EParser.Native_symbol_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_enum_native_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = EParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(EParser.DEFINE)
            self.state = 436 
            localctx.name = self.type_identifier()
            self.state = 437
            self.match(EParser.AS)
            self.state = 438
            self.match(EParser.ENUMERATED)
            self.state = 439 
            localctx.typ = self.native_type()
            self.state = 440
            self.match(EParser.WITH)
            self.state = 441 
            self.symbols_token()
            self.state = 442
            self.match(EParser.COLON)
            self.state = 443 
            self.indent()
            self.state = 444 
            localctx.symbols = self.native_symbol_list()
            self.state = 445 
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
            super(EParser.Native_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.exp = None # ExpressionContext

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def value_token(self):
            return self.getTypedRuleContext(EParser.Value_tokenContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_symbol

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = EParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447 
            localctx.name = self.symbol_identifier()
            self.state = 448
            self.match(EParser.WITH)
            self.state = 449 
            localctx.exp = self.expression(0)
            self.state = 450
            self.match(EParser.AS)
            self.state = 451 
            self.value_token()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def getRuleIndex(self):
            return EParser.RULE_category_symbol

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = EParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_category_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453 
            localctx.name = self.symbol_identifier()
            self.state = 454 
            localctx.args = self.with_argument_assignment_list(0)
            self.state = 457
            _la = self._input.LA(1)
            if _la==EParser.AND:
                self.state = 455
                self.match(EParser.AND)
                self.state = 456 
                localctx.arg = self.argument_assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Attribute_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext
            self.indices = None # Variable_identifier_listContext
            self.index = None # Variable_identifierContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)

        def attribute_identifier(self):
            return self.getTypedRuleContext(EParser.Attribute_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def INDEX(self):
            return self.getToken(EParser.INDEX, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(EParser.Attribute_constraintContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(EParser.Variable_identifier_listContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = EParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(EParser.DEFINE)
            self.state = 460 
            localctx.name = self.attribute_identifier()
            self.state = 461
            self.match(EParser.AS)
            self.state = 463
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 462
                self.match(EParser.STORABLE)


            self.state = 465 
            localctx.typ = self.typedef(0)
            self.state = 466
            self.match(EParser.ATTRIBUTE)
            self.state = 468
            _la = self._input.LA(1)
            if _la==EParser.IN or _la==EParser.MATCHING:
                self.state = 467 
                localctx.match = self.attribute_constraint()


            self.state = 479
            _la = self._input.LA(1)
            if _la==EParser.WITH:
                self.state = 470
                self.match(EParser.WITH)
                self.state = 476
                _la = self._input.LA(1)
                if _la==EParser.VARIABLE_IDENTIFIER:
                    self.state = 471 
                    localctx.indices = self.variable_identifier_list()
                    self.state = 474
                    _la = self._input.LA(1)
                    if _la==EParser.AND:
                        self.state = 472
                        self.match(EParser.AND)
                        self.state = 473 
                        localctx.index = self.variable_identifier()




                self.state = 478
                self.match(EParser.INDEX)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Concrete_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Derived_listContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def derived_list(self):
            return self.getTypedRuleContext(EParser.Derived_listContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Member_method_declaration_listContext,0)


        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def getRuleIndex(self):
            return EParser.RULE_concrete_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = EParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(EParser.DEFINE)
            self.state = 482 
            localctx.name = self.type_identifier()
            self.state = 483
            self.match(EParser.AS)
            self.state = 485
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 484
                self.match(EParser.STORABLE)


            self.state = 489
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 487
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 488 
                localctx.derived = self.derived_list()

            else:
                raise NoViableAltException(self)

            self.state = 509
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 491 
                localctx.attrs = self.attribute_list()
                self.state = 500
                _la = self._input.LA(1)
                if _la==EParser.COMMA:
                    self.state = 492
                    self.match(EParser.COMMA)
                    self.state = 493
                    self.match(EParser.AND)
                    self.state = 494
                    self.match(EParser.METHODS)
                    self.state = 495
                    self.match(EParser.COLON)
                    self.state = 496 
                    self.indent()
                    self.state = 497 
                    localctx.methods = self.member_method_declaration_list()
                    self.state = 498 
                    self.dedent()



            elif la_ == 2:
                self.state = 502
                self.match(EParser.WITH)
                self.state = 503
                self.match(EParser.METHODS)
                self.state = 504
                self.match(EParser.COLON)
                self.state = 505 
                self.indent()
                self.state = 506 
                localctx.methods = self.member_method_declaration_list()
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
            super(EParser.Singleton_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def SINGLETON(self):
            return self.getToken(EParser.SINGLETON, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Member_method_declaration_listContext,0)


        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def getRuleIndex(self):
            return EParser.RULE_singleton_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = EParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_singleton_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(EParser.DEFINE)
            self.state = 512 
            localctx.name = self.type_identifier()
            self.state = 513
            self.match(EParser.AS)
            self.state = 514
            self.match(EParser.SINGLETON)
            self.state = 533
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 515 
                localctx.attrs = self.attribute_list()
                self.state = 524
                _la = self._input.LA(1)
                if _la==EParser.COMMA:
                    self.state = 516
                    self.match(EParser.COMMA)
                    self.state = 517
                    self.match(EParser.AND)
                    self.state = 518
                    self.match(EParser.METHODS)
                    self.state = 519
                    self.match(EParser.COLON)
                    self.state = 520 
                    self.indent()
                    self.state = 521 
                    localctx.methods = self.member_method_declaration_list()
                    self.state = 522 
                    self.dedent()



            elif la_ == 2:
                self.state = 526
                self.match(EParser.WITH)
                self.state = 527
                self.match(EParser.METHODS)
                self.state = 528
                self.match(EParser.COLON)
                self.state = 529 
                self.indent()
                self.state = 530 
                localctx.methods = self.member_method_declaration_list()
                self.state = 531 
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
            super(EParser.Derived_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_derived_list

     
        def copyFrom(self, ctx):
            super(EParser.Derived_listContext, self).copyFrom(ctx)



    class DerivedListItemContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Derived_listContext)
            super(EParser.DerivedListItemContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def type_identifier_list(self):
            return self.getTypedRuleContext(EParser.Type_identifier_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDerivedListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDerivedListItem(self)


    class DerivedListContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Derived_listContext)
            super(EParser.DerivedListContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.copyFrom(ctx)

        def type_identifier_list(self):
            return self.getTypedRuleContext(EParser.Type_identifier_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDerivedList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDerivedList(self)



    def derived_list(self):

        localctx = EParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_derived_list)
        try:
            self.state = 540
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = EParser.DerivedListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 535 
                localctx.items = self.type_identifier_list()
                pass

            elif la_ == 2:
                localctx = EParser.DerivedListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 536 
                localctx.items = self.type_identifier_list()
                self.state = 537
                self.match(EParser.AND)
                self.state = 538 
                localctx.item = self.type_identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Operator_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # OperatorContext
            self.arg = None # Operator_argumentContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def OPERATOR(self):
            return self.getToken(EParser.OPERATOR, 0)

        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def operator(self):
            return self.getTypedRuleContext(EParser.OperatorContext,0)


        def operator_argument(self):
            return self.getTypedRuleContext(EParser.Operator_argumentContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_operator_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = EParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(EParser.DEFINE)
            self.state = 543 
            localctx.op = self.operator()
            self.state = 544
            self.match(EParser.AS)
            self.state = 545
            self.match(EParser.OPERATOR)
            self.state = 546
            self.match(EParser.RECEIVING)
            self.state = 547 
            localctx.arg = self.operator_argument()
            self.state = 550
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 548
                self.match(EParser.RETURNING)
                self.state = 549 
                localctx.typ = self.typedef(0)


            self.state = 552
            self.match(EParser.DOING)
            self.state = 553
            self.match(EParser.COLON)
            self.state = 554 
            self.indent()
            self.state = 555 
            localctx.stmts = self.statement_list()
            self.state = 556 
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
            super(EParser.Setter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def SETTER(self):
            return self.getToken(EParser.SETTER, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_setter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = EParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(EParser.DEFINE)
            self.state = 559 
            localctx.name = self.variable_identifier()
            self.state = 560
            self.match(EParser.AS)
            self.state = 561
            self.match(EParser.SETTER)
            self.state = 562
            self.match(EParser.DOING)
            self.state = 563
            self.match(EParser.COLON)
            self.state = 564 
            self.indent()
            self.state = 565 
            localctx.stmts = self.statement_list()
            self.state = 566 
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
            super(EParser.Native_setter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def SETTER(self):
            return self.getToken(EParser.SETTER, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def getRuleIndex(self):
            return EParser.RULE_native_setter_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = EParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(EParser.DEFINE)
            self.state = 569 
            localctx.name = self.variable_identifier()
            self.state = 570
            self.match(EParser.AS)
            self.state = 572
            _la = self._input.LA(1)
            if _la==EParser.NATIVE:
                self.state = 571
                self.match(EParser.NATIVE)


            self.state = 574
            self.match(EParser.SETTER)
            self.state = 575
            self.match(EParser.DOING)
            self.state = 576
            self.match(EParser.COLON)
            self.state = 577 
            self.indent()
            self.state = 578 
            localctx.stmts = self.native_statement_list()
            self.state = 579 
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
            super(EParser.Getter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def GETTER(self):
            return self.getToken(EParser.GETTER, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_getter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = EParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(EParser.DEFINE)
            self.state = 582 
            localctx.name = self.variable_identifier()
            self.state = 583
            self.match(EParser.AS)
            self.state = 584
            self.match(EParser.GETTER)
            self.state = 585
            self.match(EParser.DOING)
            self.state = 586
            self.match(EParser.COLON)
            self.state = 587 
            self.indent()
            self.state = 588 
            localctx.stmts = self.statement_list()
            self.state = 589 
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
            super(EParser.Native_getter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def GETTER(self):
            return self.getToken(EParser.GETTER, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def getRuleIndex(self):
            return EParser.RULE_native_getter_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = EParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(EParser.DEFINE)
            self.state = 592 
            localctx.name = self.variable_identifier()
            self.state = 593
            self.match(EParser.AS)
            self.state = 595
            _la = self._input.LA(1)
            if _la==EParser.NATIVE:
                self.state = 594
                self.match(EParser.NATIVE)


            self.state = 597
            self.match(EParser.GETTER)
            self.state = 598
            self.match(EParser.DOING)
            self.state = 599
            self.match(EParser.COLON)
            self.state = 600 
            self.indent()
            self.state = 601 
            localctx.stmts = self.native_statement_list()
            self.state = 602 
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
            super(EParser.Native_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingsContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def BINDINGS(self):
            return self.getToken(EParser.BINDINGS, 0)

        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def AND(self, i=None):
            if i is None:
                return self.getTokens(EParser.AND)
            else:
                return self.getToken(EParser.AND, i)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declaration_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = EParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(EParser.DEFINE)
            self.state = 605 
            localctx.name = self.type_identifier()
            self.state = 606
            self.match(EParser.AS)
            self.state = 608
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 607
                self.match(EParser.STORABLE)


            self.state = 610
            self.match(EParser.NATIVE)
            self.state = 611
            self.match(EParser.CATEGORY)
            self.state = 619
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 612 
                localctx.attrs = self.attribute_list()
                self.state = 613
                self.match(EParser.COMMA)
                self.state = 614
                self.match(EParser.AND)
                self.state = 615
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 617
                self.match(EParser.WITH)
                self.state = 618
                self.match(EParser.BINDINGS)
                pass


            self.state = 621
            self.match(EParser.COLON)
            self.state = 622 
            self.indent()
            self.state = 623 
            localctx.bindings = self.native_category_bindings()
            self.state = 624 
            self.dedent()
            self.state = 633
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 625 
                self.lfp()
                self.state = 626
                self.match(EParser.AND)
                self.state = 627
                self.match(EParser.METHODS)
                self.state = 628
                self.match(EParser.COLON)
                self.state = 629 
                self.indent()
                self.state = 630 
                localctx.methods = self.native_member_method_declaration_list()
                self.state = 631 
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
            super(EParser.Native_resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(EParser.RESOURCE, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingsContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def BINDINGS(self):
            return self.getToken(EParser.BINDINGS, 0)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def AND(self, i=None):
            if i is None:
                return self.getTokens(EParser.AND)
            else:
                return self.getToken(EParser.AND, i)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declaration_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = EParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_native_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.match(EParser.DEFINE)
            self.state = 636 
            localctx.name = self.type_identifier()
            self.state = 637
            self.match(EParser.AS)
            self.state = 638
            self.match(EParser.NATIVE)
            self.state = 639
            self.match(EParser.RESOURCE)
            self.state = 647
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 640 
                localctx.attrs = self.attribute_list()
                self.state = 641
                self.match(EParser.COMMA)
                self.state = 642
                self.match(EParser.AND)
                self.state = 643
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 645
                self.match(EParser.WITH)
                self.state = 646
                self.match(EParser.BINDINGS)
                pass


            self.state = 649
            self.match(EParser.COLON)
            self.state = 650 
            self.indent()
            self.state = 651 
            localctx.bindings = self.native_category_bindings()
            self.state = 652 
            self.dedent()
            self.state = 661
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 653 
                self.lfp()
                self.state = 654
                self.match(EParser.AND)
                self.state = 655
                self.match(EParser.METHODS)
                self.state = 656
                self.match(EParser.COLON)
                self.state = 657 
                self.indent()
                self.state = 658 
                localctx.methods = self.native_member_method_declaration_list()
                self.state = 659 
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
            super(EParser.Native_category_bindingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_binding_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def BINDINGS(self):
            return self.getToken(EParser.BINDINGS, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def native_category_binding_list(self):
            return self.getTypedRuleContext(EParser.Native_category_binding_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_category_bindings

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = EParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_native_category_bindings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 663
            self.match(EParser.DEFINE)
            self.state = 664
            self.match(EParser.CATEGORY)
            self.state = 665
            self.match(EParser.BINDINGS)
            self.state = 666
            self.match(EParser.AS)
            self.state = 667
            self.match(EParser.COLON)
            self.state = 668 
            self.indent()
            self.state = 669 
            localctx.items = self.native_category_binding_list(0)
            self.state = 670 
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
            super(EParser.Native_category_binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_category_binding_list

     
        def copyFrom(self, ctx):
            super(EParser.Native_category_binding_listContext, self).copyFrom(ctx)


    class NativeCategoryBindingListItemContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_binding_listContext)
            super(EParser.NativeCategoryBindingListItemContext, self).__init__(parser)
            self.items = None # Native_category_binding_listContext
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(EParser.Native_category_binding_listContext,0)

        def native_category_binding(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_binding_listContext)
            super(EParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def native_category_binding(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 673 
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 681
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeCategoryBindingListItemContext(self, EParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 675
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 676 
                    self.lfp()
                    self.state = 677 
                    localctx.item = self.native_category_binding() 
                self.state = 683
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_attribute_list

     
        def copyFrom(self, ctx):
            super(EParser.Attribute_listContext, self).copyFrom(ctx)



    class AttributeListContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_listContext)
            super(EParser.AttributeListContext, self).__init__(parser)
            self.item = None # Attribute_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)
        def attribute_identifier(self):
            return self.getTypedRuleContext(EParser.Attribute_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeList(self)


    class AttributeListItemContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_listContext)
            super(EParser.AttributeListItemContext, self).__init__(parser)
            self.items = None # Attribute_identifier_listContext
            self.item = None # Attribute_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTES(self):
            return self.getToken(EParser.ATTRIBUTES, 0)
        def attribute_identifier_list(self):
            return self.getTypedRuleContext(EParser.Attribute_identifier_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def attribute_identifier(self):
            return self.getTypedRuleContext(EParser.Attribute_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeListItem(self)



    def attribute_list(self):

        localctx = EParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_attribute_list)
        try:
            self.state = 694
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = EParser.AttributeListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 684
                self.match(EParser.WITH)
                self.state = 685
                self.match(EParser.ATTRIBUTE)
                self.state = 686 
                localctx.item = self.attribute_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.AttributeListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 687
                self.match(EParser.WITH)
                self.state = 688
                self.match(EParser.ATTRIBUTES)
                self.state = 689 
                localctx.items = self.attribute_identifier_list()
                self.state = 692
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 690
                    self.match(EParser.AND)
                    self.state = 691 
                    localctx.item = self.attribute_identifier()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Abstract_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Abstract_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Full_argument_listContext
            self.typ = None # TypedefContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def ABSTRACT(self):
            return self.getToken(EParser.ABSTRACT, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def full_argument_list(self):
            return self.getTypedRuleContext(EParser.Full_argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_abstract_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = EParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 696
            self.match(EParser.DEFINE)
            self.state = 697 
            localctx.name = self.method_identifier()
            self.state = 698
            self.match(EParser.AS)
            self.state = 699
            self.match(EParser.ABSTRACT)
            self.state = 700
            self.match(EParser.METHOD)
            self.state = 703
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 701
                self.match(EParser.RECEIVING)
                self.state = 702 
                localctx.args = self.full_argument_list()


            self.state = 707
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 705
                self.match(EParser.RETURNING)
                self.state = 706 
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
            super(EParser.Concrete_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Full_argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def full_argument_list(self):
            return self.getTypedRuleContext(EParser.Full_argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_concrete_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = EParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self.match(EParser.DEFINE)
            self.state = 710 
            localctx.name = self.method_identifier()
            self.state = 711
            self.match(EParser.AS)
            self.state = 712
            self.match(EParser.METHOD)
            self.state = 715
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 713
                self.match(EParser.RECEIVING)
                self.state = 714 
                localctx.args = self.full_argument_list()


            self.state = 719
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 717
                self.match(EParser.RETURNING)
                self.state = 718 
                localctx.typ = self.typedef(0)


            self.state = 721
            self.match(EParser.DOING)
            self.state = 722
            self.match(EParser.COLON)
            self.state = 723 
            self.indent()
            self.state = 724 
            localctx.stmts = self.statement_list()
            self.state = 725 
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
            super(EParser.Native_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Full_argument_listContext
            self.typ = None # Category_or_any_typeContext
            self.stmts = None # Native_statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def full_argument_list(self):
            return self.getTypedRuleContext(EParser.Full_argument_listContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = EParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
            self.match(EParser.DEFINE)
            self.state = 728 
            localctx.name = self.method_identifier()
            self.state = 729
            self.match(EParser.AS)
            self.state = 731
            _la = self._input.LA(1)
            if _la==EParser.NATIVE:
                self.state = 730
                self.match(EParser.NATIVE)


            self.state = 733
            self.match(EParser.METHOD)
            self.state = 736
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 734
                self.match(EParser.RECEIVING)
                self.state = 735 
                localctx.args = self.full_argument_list()


            self.state = 740
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 738
                self.match(EParser.RETURNING)
                self.state = 739 
                localctx.typ = self.category_or_any_type()


            self.state = 742
            self.match(EParser.DOING)
            self.state = 743
            self.match(EParser.COLON)
            self.state = 744 
            self.indent()
            self.state = 745 
            localctx.stmts = self.native_statement_list()
            self.state = 746 
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
            super(EParser.Test_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.stmts = None # Statement_listContext
            self.exps = None # Assertion_listContext
            self.error = None # Symbol_identifierContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def VERIFYING(self):
            return self.getToken(EParser.VERIFYING, 0)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def assertion_list(self):
            return self.getTypedRuleContext(EParser.Assertion_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_test_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = EParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 748
            self.match(EParser.DEFINE)
            self.state = 749
            localctx.name = self.match(EParser.TEXT_LITERAL)
            self.state = 750
            self.match(EParser.AS)
            self.state = 751
            self.match(EParser.TEST)
            self.state = 752
            self.match(EParser.METHOD)
            self.state = 753
            self.match(EParser.DOING)
            self.state = 754
            self.match(EParser.COLON)
            self.state = 755 
            self.indent()
            self.state = 756 
            localctx.stmts = self.statement_list()
            self.state = 757 
            self.dedent()
            self.state = 758 
            self.lfp()
            self.state = 759
            self.match(EParser.AND)
            self.state = 760
            self.match(EParser.VERIFYING)
            self.state = 767
            token = self._input.LA(1)
            if token in [EParser.COLON]:
                self.state = 761
                self.match(EParser.COLON)
                self.state = 762 
                self.indent()
                self.state = 763 
                localctx.exps = self.assertion_list()
                self.state = 764 
                self.dedent()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                self.state = 766 
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
            super(EParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assertion

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = EParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 769 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Full_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Full_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Argument_listContext
            self.item = None # ArgumentContext

        def argument_list(self):
            return self.getTypedRuleContext(EParser.Argument_listContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def argument(self):
            return self.getTypedRuleContext(EParser.ArgumentContext,0)


        def getRuleIndex(self):
            return EParser.RULE_full_argument_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFull_argument_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFull_argument_list(self)




    def full_argument_list(self):

        localctx = EParser.Full_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_full_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 771 
            localctx.items = self.argument_list()
            self.state = 774
            _la = self._input.LA(1)
            if _la==EParser.AND:
                self.state = 772
                self.match(EParser.AND)
                self.state = 773 
                localctx.item = self.argument()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typed_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Typed_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_or_any_typeContext
            self.name = None # Variable_identifierContext
            self.attrs = None # Attribute_listContext
            self.value = None # Literal_expressionContext

        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(EParser.EQ, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_typed_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = EParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 776 
            localctx.typ = self.category_or_any_type()
            self.state = 777 
            localctx.name = self.variable_identifier()
            self.state = 779
            _la = self._input.LA(1)
            if _la==EParser.WITH:
                self.state = 778 
                localctx.attrs = self.attribute_list()


            self.state = 783
            _la = self._input.LA(1)
            if _la==EParser.EQ:
                self.state = 781
                self.match(EParser.EQ)
                self.state = 782 
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
            super(EParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(EParser.StatementContext, self).copyFrom(ctx)



    class CommentStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.CommentStatementContext, self).__init__(parser)
            self.decl = None # Comment_statementContext
            self.copyFrom(ctx)

        def comment_statement(self):
            return self.getTypedRuleContext(EParser.Comment_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(EParser.Store_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(EParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(EParser.Write_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(EParser.While_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(EParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(EParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRaiseStatement(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.BreakStatementContext, self).__init__(parser)
            self.stmt = None # Break_statementContext
            self.copyFrom(ctx)

        def break_statement(self):
            return self.getTypedRuleContext(EParser.Break_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBreakStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(EParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(EParser.If_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(EParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(EParser.Try_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTryStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_call_statementContext
            self.copyFrom(ctx)

        def method_call_statement(self):
            return self.getTypedRuleContext(EParser.Method_call_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(EParser.Return_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(EParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitClosureStatement(self)


    class FlushStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.FlushStatementContext, self).__init__(parser)
            self.stmt = None # Flush_statementContext
            self.copyFrom(ctx)

        def flush_statement(self):
            return self.getTypedRuleContext(EParser.Flush_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFlushStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFlushStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(EParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(EParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = EParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 804
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                localctx = EParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 785 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 2:
                localctx = EParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 786 
                localctx.stmt = self.method_call_statement()
                pass

            elif la_ == 3:
                localctx = EParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 787 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = EParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 788 
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = EParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 789 
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = EParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 790 
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = EParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 791 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = EParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 792 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = EParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 793 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = EParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 794 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = EParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 795 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = EParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 796 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = EParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 797 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 14:
                localctx = EParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 798 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 15:
                localctx = EParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 799 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = EParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 800 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = EParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 801 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = EParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 802 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = EParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 803 
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
            super(EParser.Flush_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLUSH(self):
            return self.getToken(EParser.FLUSH, 0)

        def getRuleIndex(self):
            return EParser.RULE_flush_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFlush_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFlush_statement(self)




    def flush_statement(self):

        localctx = EParser.Flush_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_flush_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 806
            self.match(EParser.FLUSH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Store_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Store_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.to_del = None # Expression_listContext
            self.to_add = None # Expression_listContext

        def DELETE(self):
            return self.getToken(EParser.DELETE, 0)

        def expression_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Expression_listContext)
            else:
                return self.getTypedRuleContext(EParser.Expression_listContext,i)


        def STORE(self):
            return self.getToken(EParser.STORE, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def getRuleIndex(self):
            return EParser.RULE_store_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = EParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_store_statement)
        try:
            self.state = 818
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 808
                self.match(EParser.DELETE)
                self.state = 809 
                localctx.to_del = self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 810
                self.match(EParser.STORE)
                self.state = 811 
                localctx.to_add = self.expression_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 812
                self.match(EParser.DELETE)
                self.state = 813 
                localctx.to_del = self.expression_list()
                self.state = 814
                self.match(EParser.AND)
                self.state = 815
                self.match(EParser.STORE)
                self.state = 816 
                localctx.to_add = self.expression_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_call_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_call_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_method_call_statement

     
        def copyFrom(self, ctx):
            super(EParser.Method_call_statementContext, self).copyFrom(ctx)



    class InvokeStatementContext(Method_call_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_call_statementContext)
            super(EParser.InvokeStatementContext, self).__init__(parser)
            self.exp = None # Invocation_expressionContext
            self.copyFrom(ctx)

        def invocation_expression(self):
            return self.getTypedRuleContext(EParser.Invocation_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvokeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvokeStatement(self)


    class UnresolvedWithArgsStatementContext(Method_call_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_call_statementContext)
            super(EParser.UnresolvedWithArgsStatementContext, self).__init__(parser)
            self.exp = None # Unresolved_expressionContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedWithArgsStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedWithArgsStatement(self)



    def method_call_statement(self):

        localctx = EParser.Method_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_method_call_statement)
        try:
            self.state = 825
            token = self._input.LA(1)
            if token in [EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.UnresolvedWithArgsStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 820 
                localctx.exp = self.unresolved_expression(0)
                self.state = 822
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 821 
                    localctx.args = self.argument_assignment_list()



            elif token in [EParser.INVOKE]:
                localctx = EParser.InvokeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 824 
                localctx.exp = self.invocation_expression()

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
            super(EParser.With_resource_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Assign_variable_statementContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def DO(self):
            return self.getToken(EParser.DO, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def assign_variable_statement(self):
            return self.getTypedRuleContext(EParser.Assign_variable_statementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_with_resource_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = EParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 827
            self.match(EParser.WITH)
            self.state = 828 
            localctx.stmt = self.assign_variable_statement()
            self.state = 829
            self.match(EParser.COMMA)
            self.state = 830
            self.match(EParser.DO)
            self.state = 831
            self.match(EParser.COLON)
            self.state = 832 
            self.indent()
            self.state = 833 
            localctx.stmts = self.statement_list()
            self.state = 834 
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
            super(EParser.With_singleton_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Type_identifierContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def DO(self):
            return self.getToken(EParser.DO, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_with_singleton_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = EParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 836
            self.match(EParser.WITH)
            self.state = 837 
            localctx.typ = self.type_identifier()
            self.state = 838
            self.match(EParser.COMMA)
            self.state = 839
            self.match(EParser.DO)
            self.state = 840
            self.match(EParser.COLON)
            self.state = 841 
            self.indent()
            self.state = 842 
            localctx.stmts = self.statement_list()
            self.state = 843 
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
            super(EParser.Switch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.cases = None # Switch_case_statement_listContext
            self.stmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(EParser.SWITCH, 0)

        def ON(self):
            return self.getToken(EParser.ON, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def switch_case_statement_list(self):
            return self.getTypedRuleContext(EParser.Switch_case_statement_listContext,0)


        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def OTHERWISE(self):
            return self.getToken(EParser.OTHERWISE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_switch_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = EParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 845
            self.match(EParser.SWITCH)
            self.state = 846
            self.match(EParser.ON)
            self.state = 847 
            localctx.exp = self.expression(0)
            self.state = 848
            self.match(EParser.COLON)
            self.state = 849 
            self.indent()
            self.state = 850 
            localctx.cases = self.switch_case_statement_list()
            self.state = 858
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 851 
                self.lfp()
                self.state = 852
                self.match(EParser.OTHERWISE)
                self.state = 853
                self.match(EParser.COLON)
                self.state = 854 
                self.indent()
                self.state = 855 
                localctx.stmts = self.statement_list()
                self.state = 856 
                self.dedent()


            self.state = 860 
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
            super(EParser.Switch_case_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_switch_case_statement

     
        def copyFrom(self, ctx):
            super(EParser.Switch_case_statementContext, self).copyFrom(ctx)



    class AtomicSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Switch_case_statementContext)
            super(EParser.AtomicSwitchCaseContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAtomicSwitchCase(self)


    class CollectionSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Switch_case_statementContext)
            super(EParser.CollectionSwitchCaseContext, self).__init__(parser)
            self.exp = None # Literal_collectionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def literal_collection(self):
            return self.getTypedRuleContext(EParser.Literal_collectionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = EParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_switch_case_statement)
        try:
            self.state = 877
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = EParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 862
                self.match(EParser.WHEN)
                self.state = 863 
                localctx.exp = self.atomic_literal()
                self.state = 864
                self.match(EParser.COLON)
                self.state = 865 
                self.indent()
                self.state = 866 
                localctx.stmts = self.statement_list()
                self.state = 867 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = EParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 869
                self.match(EParser.WHEN)
                self.state = 870
                self.match(EParser.IN)
                self.state = 871 
                localctx.exp = self.literal_collection()
                self.state = 872
                self.match(EParser.COLON)
                self.state = 873 
                self.indent()
                self.state = 874 
                localctx.stmts = self.statement_list()
                self.state = 875 
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
            super(EParser.For_each_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name1 = None # Variable_identifierContext
            self.name2 = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def FOR(self):
            return self.getToken(EParser.FOR, 0)

        def EACH(self):
            return self.getToken(EParser.EACH, 0)

        def IN(self):
            return self.getToken(EParser.IN, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Variable_identifierContext,i)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def getRuleIndex(self):
            return EParser.RULE_for_each_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = EParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 879
            self.match(EParser.FOR)
            self.state = 880
            self.match(EParser.EACH)
            self.state = 881 
            localctx.name1 = self.variable_identifier()
            self.state = 884
            _la = self._input.LA(1)
            if _la==EParser.COMMA:
                self.state = 882
                self.match(EParser.COMMA)
                self.state = 883 
                localctx.name2 = self.variable_identifier()


            self.state = 886
            self.match(EParser.IN)
            self.state = 887 
            localctx.source = self.expression(0)
            self.state = 888
            self.match(EParser.COLON)
            self.state = 889 
            self.indent()
            self.state = 890 
            localctx.stmts = self.statement_list()
            self.state = 891 
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
            super(EParser.Do_while_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # Statement_listContext
            self.exp = None # ExpressionContext

        def DO(self):
            return self.getToken(EParser.DO, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def WHILE(self):
            return self.getToken(EParser.WHILE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_do_while_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = EParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 893
            self.match(EParser.DO)
            self.state = 894
            self.match(EParser.COLON)
            self.state = 895 
            self.indent()
            self.state = 896 
            localctx.stmts = self.statement_list()
            self.state = 897 
            self.dedent()
            self.state = 898 
            self.lfp()
            self.state = 899
            self.match(EParser.WHILE)
            self.state = 900 
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
            super(EParser.While_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def WHILE(self):
            return self.getToken(EParser.WHILE, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_while_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = EParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 902
            self.match(EParser.WHILE)
            self.state = 903 
            localctx.exp = self.expression(0)
            self.state = 904
            self.match(EParser.COLON)
            self.state = 905 
            self.indent()
            self.state = 906 
            localctx.stmts = self.statement_list()
            self.state = 907 
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
            super(EParser.If_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.elseIfs = None # Else_if_statement_listContext
            self.elseStmts = None # Statement_listContext

        def IF(self):
            return self.getToken(EParser.IF, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(EParser.Statement_listContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(EParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_if_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = EParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 909
            self.match(EParser.IF)
            self.state = 910 
            localctx.exp = self.expression(0)
            self.state = 911
            self.match(EParser.COLON)
            self.state = 912 
            self.indent()
            self.state = 913 
            localctx.stmts = self.statement_list()
            self.state = 914 
            self.dedent()
            self.state = 918
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 915 
                self.lfp()
                self.state = 916 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 927
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 920 
                self.lfp()
                self.state = 921
                self.match(EParser.ELSE)
                self.state = 922
                self.match(EParser.COLON)
                self.state = 923 
                self.indent()
                self.state = 924 
                localctx.elseStmts = self.statement_list()
                self.state = 925 
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
            super(EParser.Else_if_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_else_if_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Else_if_statement_listContext, self).copyFrom(ctx)


    class ElseIfStatementListContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Else_if_statement_listContext)
            super(EParser.ElseIfStatementListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)
        def IF(self):
            return self.getToken(EParser.IF, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitElseIfStatementList(self)


    class ElseIfStatementListItemContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Else_if_statement_listContext)
            super(EParser.ElseIfStatementListItemContext, self).__init__(parser)
            self.items = None # Else_if_statement_listContext
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)
        def IF(self):
            return self.getToken(EParser.IF, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(EParser.Else_if_statement_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 930
            self.match(EParser.ELSE)
            self.state = 931
            self.match(EParser.IF)
            self.state = 932 
            localctx.exp = self.expression(0)
            self.state = 933
            self.match(EParser.COLON)
            self.state = 934 
            self.indent()
            self.state = 935 
            localctx.stmts = self.statement_list()
            self.state = 936 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 950
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ElseIfStatementListItemContext(self, EParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 938
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 939 
                    self.lfp()
                    self.state = 940
                    self.match(EParser.ELSE)
                    self.state = 941
                    self.match(EParser.IF)
                    self.state = 942 
                    localctx.exp = self.expression(0)
                    self.state = 943
                    self.match(EParser.COLON)
                    self.state = 944 
                    self.indent()
                    self.state = 945 
                    localctx.stmts = self.statement_list()
                    self.state = 946 
                    self.dedent() 
                self.state = 952
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
            super(EParser.Raise_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RAISE(self):
            return self.getToken(EParser.RAISE, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_raise_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = EParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 953
            self.match(EParser.RAISE)
            self.state = 954 
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
            super(EParser.Try_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext
            self.handlers = None # Catch_statement_listContext
            self.anyStmts = None # Statement_listContext
            self.finalStmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(EParser.SWITCH, 0)

        def ON(self):
            return self.getToken(EParser.ON, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def lfs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfsContext)
            else:
                return self.getTypedRuleContext(EParser.LfsContext,i)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(EParser.Statement_listContext,i)


        def ALWAYS(self):
            return self.getToken(EParser.ALWAYS, 0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(EParser.Catch_statement_listContext,0)


        def OTHERWISE(self):
            return self.getToken(EParser.OTHERWISE, 0)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)

        def ANY(self):
            return self.getToken(EParser.ANY, 0)

        def getRuleIndex(self):
            return EParser.RULE_try_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = EParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 956
            self.match(EParser.SWITCH)
            self.state = 957
            self.match(EParser.ON)
            self.state = 958 
            localctx.name = self.variable_identifier()
            self.state = 959
            self.match(EParser.DOING)
            self.state = 960
            self.match(EParser.COLON)
            self.state = 961 
            self.indent()
            self.state = 962 
            localctx.stmts = self.statement_list()
            self.state = 963 
            self.dedent()
            self.state = 964 
            self.lfs()
            self.state = 966
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 965 
                localctx.handlers = self.catch_statement_list()


            self.state = 979
            _la = self._input.LA(1)
            if _la==EParser.OTHERWISE or _la==EParser.WHEN:
                self.state = 971
                token = self._input.LA(1)
                if token in [EParser.OTHERWISE]:
                    self.state = 968
                    self.match(EParser.OTHERWISE)

                elif token in [EParser.WHEN]:
                    self.state = 969
                    self.match(EParser.WHEN)
                    self.state = 970
                    self.match(EParser.ANY)

                else:
                    raise NoViableAltException(self)

                self.state = 973
                self.match(EParser.COLON)
                self.state = 974 
                self.indent()
                self.state = 975 
                localctx.anyStmts = self.statement_list()
                self.state = 976 
                self.dedent()
                self.state = 977 
                self.lfs()


            self.state = 988
            _la = self._input.LA(1)
            if _la==EParser.ALWAYS:
                self.state = 981
                self.match(EParser.ALWAYS)
                self.state = 982
                self.match(EParser.COLON)
                self.state = 983 
                self.indent()
                self.state = 984 
                localctx.finalStmts = self.statement_list()
                self.state = 985 
                self.dedent()
                self.state = 986 
                self.lfs()


            self.state = 990 
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
            super(EParser.Catch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_catch_statement

     
        def copyFrom(self, ctx):
            super(EParser.Catch_statementContext, self).copyFrom(ctx)



    class CatchAtomicStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Catch_statementContext)
            super(EParser.CatchAtomicStatementContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(EParser.LfsContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatchAtomicStatement(self)


    class CatchCollectionStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Catch_statementContext)
            super(EParser.CatchCollectionStatementContext, self).__init__(parser)
            self.exp = None # Symbol_listContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(EParser.LfsContext,0)

        def symbol_list(self):
            return self.getTypedRuleContext(EParser.Symbol_listContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = EParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_catch_statement)
        try:
            self.state = 1011
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                localctx = EParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 992
                self.match(EParser.WHEN)
                self.state = 993 
                localctx.name = self.symbol_identifier()
                self.state = 994
                self.match(EParser.COLON)
                self.state = 995 
                self.indent()
                self.state = 996 
                localctx.stmts = self.statement_list()
                self.state = 997 
                self.dedent()
                self.state = 998 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = EParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1000
                self.match(EParser.WHEN)
                self.state = 1001
                self.match(EParser.IN)
                self.state = 1002
                self.match(EParser.LBRAK)
                self.state = 1003 
                localctx.exp = self.symbol_list()
                self.state = 1004
                self.match(EParser.RBRAK)
                self.state = 1005
                self.match(EParser.COLON)
                self.state = 1006 
                self.indent()
                self.state = 1007 
                localctx.stmts = self.statement_list()
                self.state = 1008 
                self.dedent()
                self.state = 1009 
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
            super(EParser.Break_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(EParser.BREAK, 0)

        def getRuleIndex(self):
            return EParser.RULE_break_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = EParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1013
            self.match(EParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Return_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_return_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = EParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1015
            self.match(EParser.RETURN)
            self.state = 1017
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)) | (1 << (EParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (EParser.TEXT_LITERAL - 164)) | (1 << (EParser.UUID_LITERAL - 164)) | (1 << (EParser.INTEGER_LITERAL - 164)) | (1 << (EParser.HEXA_LITERAL - 164)) | (1 << (EParser.DECIMAL_LITERAL - 164)) | (1 << (EParser.DATETIME_LITERAL - 164)) | (1 << (EParser.TIME_LITERAL - 164)) | (1 << (EParser.DATE_LITERAL - 164)) | (1 << (EParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1016 
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
            super(EParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(EParser.ExpressionContext, self).copyFrom(ctx)


    class IntDivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IntDivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(EParser.IdivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntDivideExpression(self)


    class ReadExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ReadExpressionContext, self).__init__(parser)
            self.exp = None # Read_expressionContext
            self.copyFrom(ctx)

        def read_expression(self):
            return self.getTypedRuleContext(EParser.Read_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReadExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReadExpression(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.TernaryExpressionContext, self).__init__(parser)
            self.ifTrue = None # ExpressionContext
            self.test = None # ExpressionContext
            self.ifFalse = None # ExpressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(EParser.IF, 0)
        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTernaryExpression(self)


    class FetchStoreExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.FetchStoreExpressionContext, self).__init__(parser)
            self.exp = None # Fetch_store_expressionContext
            self.copyFrom(ctx)

        def fetch_store_expression(self):
            return self.getTypedRuleContext(EParser.Fetch_store_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchStoreExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchStoreExpression(self)


    class ContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitContainsAllExpression(self)


    class NotEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(EParser.LTGT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInExpression(self)


    class DocumentExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.DocumentExpressionContext, self).__init__(parser)
            self.exp = None # Document_expressionContext
            self.copyFrom(ctx)

        def document_expression(self):
            return self.getTypedRuleContext(EParser.Document_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocumentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocumentExpression(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotExpression(self)


    class GreaterThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.GreaterThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(EParser.GT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitGreaterThanExpression(self)


    class InvocationExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InvocationExpressionContext, self).__init__(parser)
            self.exp = None # Invocation_expressionContext
            self.copyFrom(ctx)

        def invocation_expression(self):
            return self.getTypedRuleContext(EParser.Invocation_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvocationExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvocationExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.OrExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(EParser.OR, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOrExpression(self)


    class CodeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.CodeExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(EParser.CODE, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeExpression(self)


    class AmbiguousExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.AmbiguousExpressionContext, self).__init__(parser)
            self.exp = None # Ambiguous_expressionContext
            self.copyFrom(ctx)

        def ambiguous_expression(self):
            return self.getTypedRuleContext(EParser.Ambiguous_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAmbiguousExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAmbiguousExpression(self)


    class LessThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.LessThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTE(self):
            return self.getToken(EParser.LTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLessThanOrEqualExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.AndExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAndExpression(self)


    class MethodCallExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.MethodCallExpressionContext, self).__init__(parser)
            self.exp = None # Unresolved_expressionContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodCallExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodCallExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ClosureExpressionContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def METHOD_T(self):
            return self.getToken(EParser.METHOD_T, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitClosureExpression(self)


    class SortedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.SortedExpressionContext, self).__init__(parser)
            self.exp = None # Sorted_expressionContext
            self.copyFrom(ctx)

        def sorted_expression(self):
            return self.getTypedRuleContext(EParser.Sorted_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSortedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSortedExpression(self)


    class BlobExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.BlobExpressionContext, self).__init__(parser)
            self.exp = None # Blob_expressionContext
            self.copyFrom(ctx)

        def blob_expression(self):
            return self.getTypedRuleContext(EParser.Blob_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBlobExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBlobExpression(self)


    class NotContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(EParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotContainsAnyExpression(self)


    class ContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitContainsExpression(self)


    class ConstructorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ConstructorExpressionContext, self).__init__(parser)
            self.exp = None # Constructor_expressionContext
            self.copyFrom(ctx)

        def constructor_expression(self):
            return self.getTypedRuleContext(EParser.Constructor_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConstructorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConstructorExpression(self)


    class NotContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotContainsExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.MultiplyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(EParser.MultiplyContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMultiplyExpression(self)


    class RoughlyEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.RoughlyEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def TILDE(self):
            return self.getToken(EParser.TILDE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRoughlyEqualsExpression(self)


    class ExecuteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ExecuteExpressionContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def EXECUTE(self):
            return self.getToken(EParser.EXECUTE, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitExecuteExpression(self)


    class FetchListExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.FetchListExpressionContext, self).__init__(parser)
            self.exp = None # Fetch_list_expressionContext
            self.copyFrom(ctx)

        def fetch_list_expression(self):
            return self.getTypedRuleContext(EParser.Fetch_list_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchListExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchListExpression(self)


    class GreaterThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.GreaterThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GTE(self):
            return self.getToken(EParser.GTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitGreaterThanOrEqualExpression(self)


    class NotInExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotInExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotInExpression(self)


    class IteratorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IteratorExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(EParser.FOR, 0)
        def EACH(self):
            return self.getToken(EParser.EACH, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIteratorExpression(self)


    class UnresolvedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.UnresolvedExpressionContext, self).__init__(parser)
            self.exp = None # Unresolved_expressionContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedExpression(self)


    class IsNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IsNotExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(EParser.IS, 0)
        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(EParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsNotExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.DivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(EParser.DivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDivideExpression(self)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(EParser.IS, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(EParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.MinusExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMinusExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.AddExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(EParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAddExpression(self)


    class NotContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotContainsAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(EParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInstanceExpression(self)


    class ContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(EParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitContainsAnyExpression(self)


    class CastExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.CastExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def AS(self):
            return self.getToken(EParser.AS, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCastExpression(self)


    class ModuloExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ModuloExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(EParser.ModuloContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitModuloExpression(self)


    class LessThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.LessThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(EParser.LT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLessThanExpression(self)


    class EqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.EqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(EParser.EQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEqualsExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1047
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                localctx = EParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1020
                self.match(EParser.MINUS)
                self.state = 1021 
                localctx.exp = self.expression(41)
                pass

            elif la_ == 2:
                localctx = EParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1022
                self.match(EParser.NOT)
                self.state = 1023 
                localctx.exp = self.expression(40)
                pass

            elif la_ == 3:
                localctx = EParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1024
                self.match(EParser.CODE)
                self.state = 1025
                self.match(EParser.COLON)
                self.state = 1026 
                localctx.exp = self.expression(13)
                pass

            elif la_ == 4:
                localctx = EParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1027 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 5:
                localctx = EParser.UnresolvedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1028 
                localctx.exp = self.unresolved_expression(0)
                pass

            elif la_ == 6:
                localctx = EParser.MethodCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1029 
                localctx.exp = self.unresolved_expression(0)
                self.state = 1030 
                localctx.args = self.argument_assignment_list()
                pass

            elif la_ == 7:
                localctx = EParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1032
                self.match(EParser.EXECUTE)
                self.state = 1033
                self.match(EParser.COLON)
                self.state = 1034 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 8:
                localctx = EParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1035
                self.match(EParser.METHOD_T)
                self.state = 1036
                self.match(EParser.COLON)
                self.state = 1037 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 9:
                localctx = EParser.BlobExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1038 
                localctx.exp = self.blob_expression()
                pass

            elif la_ == 10:
                localctx = EParser.DocumentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1039 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 11:
                localctx = EParser.ConstructorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1040 
                localctx.exp = self.constructor_expression()
                pass

            elif la_ == 12:
                localctx = EParser.FetchListExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1041 
                localctx.exp = self.fetch_list_expression()
                pass

            elif la_ == 13:
                localctx = EParser.FetchStoreExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1042 
                localctx.exp = self.fetch_store_expression()
                pass

            elif la_ == 14:
                localctx = EParser.ReadExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1043 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 15:
                localctx = EParser.SortedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1044 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 16:
                localctx = EParser.AmbiguousExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1045 
                localctx.exp = self.ambiguous_expression()
                pass

            elif la_ == 17:
                localctx = EParser.InvocationExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1046 
                localctx.exp = self.invocation_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1150
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        localctx = EParser.MultiplyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1049
                        if not self.precpred(self._ctx, 39):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 39)")
                        self.state = 1050 
                        self.multiply()
                        self.state = 1051 
                        localctx.right = self.expression(40)
                        pass

                    elif la_ == 2:
                        localctx = EParser.DivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1053
                        if not self.precpred(self._ctx, 38):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 38)")
                        self.state = 1054 
                        self.divide()
                        self.state = 1055 
                        localctx.right = self.expression(39)
                        pass

                    elif la_ == 3:
                        localctx = EParser.ModuloExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1057
                        if not self.precpred(self._ctx, 37):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 37)")
                        self.state = 1058 
                        self.modulo()
                        self.state = 1059 
                        localctx.right = self.expression(38)
                        pass

                    elif la_ == 4:
                        localctx = EParser.IntDivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1061
                        if not self.precpred(self._ctx, 36):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 1062 
                        self.idivide()
                        self.state = 1063 
                        localctx.right = self.expression(37)
                        pass

                    elif la_ == 5:
                        localctx = EParser.AddExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1065
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 1066
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==EParser.PLUS or _la==EParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 1067 
                        localctx.right = self.expression(36)
                        pass

                    elif la_ == 6:
                        localctx = EParser.LessThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1068
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 1069
                        self.match(EParser.LT)
                        self.state = 1070 
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 7:
                        localctx = EParser.LessThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1071
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 1072
                        self.match(EParser.LTE)
                        self.state = 1073 
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 8:
                        localctx = EParser.GreaterThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1074
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 1075
                        self.match(EParser.GT)
                        self.state = 1076 
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 9:
                        localctx = EParser.GreaterThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1077
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 1078
                        self.match(EParser.GTE)
                        self.state = 1079 
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 10:
                        localctx = EParser.EqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1080
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1081
                        self.match(EParser.EQ)
                        self.state = 1082 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 11:
                        localctx = EParser.NotEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1083
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1084
                        self.match(EParser.LTGT)
                        self.state = 1085 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 12:
                        localctx = EParser.RoughlyEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1086
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1087
                        self.match(EParser.TILDE)
                        self.state = 1088 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 13:
                        localctx = EParser.OrExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1089
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1090
                        self.match(EParser.OR)
                        self.state = 1091 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 14:
                        localctx = EParser.AndExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1092
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1093
                        self.match(EParser.AND)
                        self.state = 1094 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 15:
                        localctx = EParser.TernaryExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1095
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1096
                        self.match(EParser.IF)
                        self.state = 1097 
                        localctx.test = self.expression(0)
                        self.state = 1098
                        self.match(EParser.ELSE)
                        self.state = 1099 
                        localctx.ifFalse = self.expression(24)
                        pass

                    elif la_ == 16:
                        localctx = EParser.InExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1101
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1102
                        self.match(EParser.IN)
                        self.state = 1103 
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 17:
                        localctx = EParser.ContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1104
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1105
                        self.match(EParser.CONTAINS)
                        self.state = 1106 
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 18:
                        localctx = EParser.ContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1107
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1108
                        self.match(EParser.CONTAINS)
                        self.state = 1109
                        self.match(EParser.ALL)
                        self.state = 1110 
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 19:
                        localctx = EParser.ContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1111
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1112
                        self.match(EParser.CONTAINS)
                        self.state = 1113
                        self.match(EParser.ANY)
                        self.state = 1114 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 20:
                        localctx = EParser.NotInExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1115
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1116
                        self.match(EParser.NOT)
                        self.state = 1117
                        self.match(EParser.IN)
                        self.state = 1118 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 21:
                        localctx = EParser.NotContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1119
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1120
                        self.match(EParser.NOT)
                        self.state = 1121
                        self.match(EParser.CONTAINS)
                        self.state = 1122 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 22:
                        localctx = EParser.NotContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1123
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1124
                        self.match(EParser.NOT)
                        self.state = 1125
                        self.match(EParser.CONTAINS)
                        self.state = 1126
                        self.match(EParser.ALL)
                        self.state = 1127 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 23:
                        localctx = EParser.NotContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1128
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1129
                        self.match(EParser.NOT)
                        self.state = 1130
                        self.match(EParser.CONTAINS)
                        self.state = 1131
                        self.match(EParser.ANY)
                        self.state = 1132 
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 24:
                        localctx = EParser.IteratorExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1133
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1134
                        self.match(EParser.FOR)
                        self.state = 1135
                        self.match(EParser.EACH)
                        self.state = 1136 
                        localctx.name = self.variable_identifier()
                        self.state = 1137
                        self.match(EParser.IN)
                        self.state = 1138 
                        localctx.source = self.expression(2)
                        pass

                    elif la_ == 25:
                        localctx = EParser.IsNotExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1140
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1141
                        self.match(EParser.IS)
                        self.state = 1142
                        self.match(EParser.NOT)
                        self.state = 1143 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = EParser.IsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1144
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 1145
                        self.match(EParser.IS)
                        self.state = 1146 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 27:
                        localctx = EParser.CastExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1147
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1148
                        self.match(EParser.AS)
                        self.state = 1149 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 1154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Unresolved_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Unresolved_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_unresolved_expression

     
        def copyFrom(self, ctx):
            super(EParser.Unresolved_expressionContext, self).copyFrom(ctx)


    class UnresolvedSelectorContext(Unresolved_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Unresolved_expressionContext)
            super(EParser.UnresolvedSelectorContext, self).__init__(parser)
            self.parent = None # Unresolved_expressionContext
            self.selector = None # Unresolved_selectorContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)

        def unresolved_selector(self):
            return self.getTypedRuleContext(EParser.Unresolved_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedSelector(self)


    class UnresolvedIdentifierContext(Unresolved_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Unresolved_expressionContext)
            super(EParser.UnresolvedIdentifierContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedIdentifier(self)



    def unresolved_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Unresolved_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_unresolved_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.UnresolvedIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1156 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.UnresolvedSelectorContext(self, EParser.Unresolved_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unresolved_expression)
                    self.state = 1158
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1159 
                    localctx.selector = self.unresolved_selector() 
                self.state = 1164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Unresolved_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Unresolved_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentifierContext

        def DOT(self):
            return self.getToken(EParser.DOT, 0)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_unresolved_selector

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolved_selector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolved_selector(self)




    def unresolved_selector(self):

        localctx = EParser.Unresolved_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_unresolved_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1165
            if not self.wasNot(EParser.WS):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
            self.state = 1166
            self.match(EParser.DOT)
            self.state = 1167 
            localctx.name = self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Invocation_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Invocation_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def INVOKE(self):
            return self.getToken(EParser.INVOKE, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def invocation_trailer(self):
            return self.getTypedRuleContext(EParser.Invocation_trailerContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_invocation_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvocation_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvocation_expression(self)




    def invocation_expression(self):

        localctx = EParser.Invocation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_invocation_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1169
            self.match(EParser.INVOKE)
            self.state = 1170
            self.match(EParser.COLON)
            self.state = 1171 
            localctx.name = self.variable_identifier()
            self.state = 1172 
            self.invocation_trailer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Invocation_trailerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Invocation_trailerContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_invocation_trailer

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvocation_trailer(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvocation_trailer(self)




    def invocation_trailer(self):

        localctx = EParser.Invocation_trailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_invocation_trailer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1174
            if not self.willBe(EParser.LF):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willBe(EParser.LF)")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Instance_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_instance_expression

     
        def copyFrom(self, ctx):
            super(EParser.Instance_expressionContext, self).copyFrom(ctx)


    class SelectorExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_expressionContext)
            super(EParser.SelectorExpressionContext, self).__init__(parser)
            self.parent = None # Instance_expressionContext
            self.selector = None # Instance_selectorContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(EParser.Instance_expressionContext,0)

        def instance_selector(self):
            return self.getTypedRuleContext(EParser.Instance_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_expressionContext)
            super(EParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(EParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSelectableExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1177 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SelectorExpressionContext(self, EParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1179
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1180 
                    localctx.selector = self.instance_selector() 
                self.state = 1185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Instance_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Instance_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_instance_selector

     
        def copyFrom(self, ctx):
            super(EParser.Instance_selectorContext, self).copyFrom(ctx)



    class SliceSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_selectorContext)
            super(EParser.SliceSelectorContext, self).__init__(parser)
            self.xslice = None # Slice_argumentsContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def slice_arguments(self):
            return self.getTypedRuleContext(EParser.Slice_argumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceSelector(self)


    class MemberSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_selectorContext)
            super(EParser.MemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMemberSelector(self)


    class ItemSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_selectorContext)
            super(EParser.ItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitItemSelector(self)



    def instance_selector(self):

        localctx = EParser.Instance_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_instance_selector)
        try:
            self.state = 1199
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1186
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1187
                self.match(EParser.DOT)
                self.state = 1188 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1189
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1190
                self.match(EParser.LBRAK)
                self.state = 1191 
                localctx.xslice = self.slice_arguments()
                self.state = 1192
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1194
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1195
                self.match(EParser.LBRAK)
                self.state = 1196 
                localctx.exp = self.expression(0)
                self.state = 1197
                self.match(EParser.RBRAK)
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
            super(EParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DOCUMENT(self):
            return self.getToken(EParser.DOCUMENT, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_document_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = EParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1201
            self.match(EParser.DOCUMENT)
            self.state = 1204
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 1202
                self.match(EParser.FROM)
                self.state = 1203 
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Blob_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Blob_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLOB(self):
            return self.getToken(EParser.BLOB, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_blob_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = EParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_blob_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1206
            self.match(EParser.BLOB)
            self.state = 1207
            self.match(EParser.FROM)
            self.state = 1208 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constructor_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Constructor_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_constructor_expression

     
        def copyFrom(self, ctx):
            super(EParser.Constructor_expressionContext, self).copyFrom(ctx)



    class ConstructorFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Constructor_expressionContext)
            super(EParser.ConstructorFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.firstArg = None # ExpressionContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConstructorFrom(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConstructorFrom(self)


    class ConstructorNoFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Constructor_expressionContext)
            super(EParser.ConstructorNoFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConstructorNoFrom(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConstructorNoFrom(self)



    def constructor_expression(self):

        localctx = EParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1231
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                localctx = EParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1210 
                localctx.typ = self.mutable_category_type()
                self.state = 1211
                self.match(EParser.FROM)
                self.state = 1212 
                localctx.firstArg = self.expression(0)
                self.state = 1221
                la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
                if la_ == 1:
                    self.state = 1214
                    _la = self._input.LA(1)
                    if _la==EParser.COMMA:
                        self.state = 1213
                        self.match(EParser.COMMA)


                    self.state = 1216 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1219
                    la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                    if la_ == 1:
                        self.state = 1217
                        self.match(EParser.AND)
                        self.state = 1218 
                        localctx.arg = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1223 
                localctx.typ = self.mutable_category_type()
                self.state = 1229
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 1224 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1227
                    la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                    if la_ == 1:
                        self.state = 1225
                        self.match(EParser.AND)
                        self.state = 1226 
                        localctx.arg = self.argument_assignment()




                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Read_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_read_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRead_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRead_expression(self)




    def read_expression(self):

        localctx = EParser.Read_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1233
            self.match(EParser.READ)
            self.state = 1234
            self.match(EParser.FROM)
            self.state = 1235 
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
            super(EParser.Write_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.what = None # ExpressionContext
            self.target = None # ExpressionContext

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TO(self):
            return self.getToken(EParser.TO, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_write_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = EParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1237
            self.match(EParser.WRITE)
            self.state = 1238 
            localctx.what = self.expression(0)
            self.state = 1239
            self.match(EParser.TO)
            self.state = 1240 
            localctx.target = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ambiguous_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Ambiguous_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Unresolved_expressionContext
            self.exp = None # ExpressionContext

        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_ambiguous_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAmbiguous_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAmbiguous_expression(self)




    def ambiguous_expression(self):

        localctx = EParser.Ambiguous_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_ambiguous_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1242 
            localctx.method = self.unresolved_expression(0)
            self.state = 1243
            self.match(EParser.MINUS)
            self.state = 1244 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_list_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Fetch_list_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.predicate = None # ExpressionContext

        def FETCH(self):
            return self.getToken(EParser.FETCH, 0)

        def ANY(self):
            return self.getToken(EParser.ANY, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_fetch_list_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetch_list_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetch_list_expression(self)




    def fetch_list_expression(self):

        localctx = EParser.Fetch_list_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_fetch_list_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1246
            self.match(EParser.FETCH)
            self.state = 1247
            self.match(EParser.ANY)
            self.state = 1248 
            localctx.name = self.variable_identifier()
            self.state = 1249
            self.match(EParser.FROM)
            self.state = 1250 
            localctx.source = self.expression(0)
            self.state = 1251
            self.match(EParser.WHERE)
            self.state = 1252 
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
            super(EParser.Fetch_store_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_fetch_store_expression

     
        def copyFrom(self, ctx):
            super(EParser.Fetch_store_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Fetch_store_expressionContext)
            super(EParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(EParser.FETCH, 0)
        def ONE(self):
            return self.getToken(EParser.ONE, 0)
        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchOne(self)


    class FetchManyContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Fetch_store_expressionContext)
            super(EParser.FetchManyContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.predicate = None # ExpressionContext
            self.orderby = None # Order_by_listContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(EParser.FETCH, 0)
        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)
        def ORDER(self):
            return self.getToken(EParser.ORDER, 0)
        def BY(self):
            return self.getToken(EParser.BY, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def TO(self):
            return self.getToken(EParser.TO, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)

        def order_by_list(self):
            return self.getTypedRuleContext(EParser.Order_by_listContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchMany(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchMany(self)



    def fetch_store_expression(self):

        localctx = EParser.Fetch_store_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_fetch_store_expression)
        self._la = 0 # Token type
        try:
            self.state = 1284
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                localctx = EParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1254
                self.match(EParser.FETCH)
                self.state = 1255
                self.match(EParser.ONE)

                self.state = 1257
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE or _la==EParser.TYPE_IDENTIFIER:
                    self.state = 1256 
                    localctx.typ = self.mutable_category_type()


                self.state = 1259
                self.match(EParser.WHERE)
                self.state = 1260 
                localctx.predicate = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1261
                self.match(EParser.FETCH)
                self.state = 1273
                token = self._input.LA(1)
                if token in [EParser.ALL]:
                    self.state = 1262
                    self.match(EParser.ALL)
                    self.state = 1264
                    la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                    if la_ == 1:
                        self.state = 1263 
                        localctx.typ = self.mutable_category_type()



                elif token in [EParser.LPAR, EParser.LBRAK, EParser.LCURL, EParser.MINUS, EParser.LT, EParser.METHOD_T, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.EXECUTE, EParser.FETCH, EParser.INVOKE, EParser.MUTABLE, EParser.NOT, EParser.NOTHING, EParser.READ, EParser.SELF, EParser.SORTED, EParser.THIS, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.MIN_INTEGER, EParser.MAX_INTEGER, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.TEXT_LITERAL, EParser.UUID_LITERAL, EParser.INTEGER_LITERAL, EParser.HEXA_LITERAL, EParser.DECIMAL_LITERAL, EParser.DATETIME_LITERAL, EParser.TIME_LITERAL, EParser.DATE_LITERAL, EParser.PERIOD_LITERAL]:
                    self.state = 1267
                    la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                    if la_ == 1:
                        self.state = 1266 
                        localctx.typ = self.mutable_category_type()


                    self.state = 1269 
                    localctx.xstart = self.expression(0)
                    self.state = 1270
                    self.match(EParser.TO)
                    self.state = 1271 
                    localctx.xstop = self.expression(0)

                else:
                    raise NoViableAltException(self)

                self.state = 1277
                la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
                if la_ == 1:
                    self.state = 1275
                    self.match(EParser.WHERE)
                    self.state = 1276 
                    localctx.predicate = self.expression(0)


                self.state = 1282
                la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
                if la_ == 1:
                    self.state = 1279
                    self.match(EParser.ORDER)
                    self.state = 1280
                    self.match(EParser.BY)
                    self.state = 1281 
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
            super(EParser.Sorted_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # Instance_expressionContext
            self.key = None # Instance_expressionContext

        def SORTED(self):
            return self.getToken(EParser.SORTED, 0)

        def instance_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Instance_expressionContext)
            else:
                return self.getTypedRuleContext(EParser.Instance_expressionContext,i)


        def DESC(self):
            return self.getToken(EParser.DESC, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def key_token(self):
            return self.getTypedRuleContext(EParser.Key_tokenContext,0)


        def getRuleIndex(self):
            return EParser.RULE_sorted_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = EParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1286
            self.match(EParser.SORTED)
            self.state = 1288
            _la = self._input.LA(1)
            if _la==EParser.DESC:
                self.state = 1287
                self.match(EParser.DESC)


            self.state = 1290 
            localctx.source = self.instance_expression(0)
            self.state = 1296
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.state = 1291
                self.match(EParser.WITH)
                self.state = 1292 
                localctx.key = self.instance_expression(0)
                self.state = 1293
                self.match(EParser.AS)
                self.state = 1294 
                self.key_token()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(EParser.Argument_assignment_listContext, self).copyFrom(ctx)



    class ArgumentAssignmentListExpressionContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.items = None # With_argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentListExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentListExpression(self)


    class ArgumentAssignmentListNoExpressionContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListNoExpressionContext, self).__init__(parser)
            self.items = None # With_argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentListNoExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentListNoExpression(self)



    def argument_assignment_list(self):

        localctx = EParser.Argument_assignment_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_argument_assignment_list)
        try:
            self.state = 1312
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                localctx = EParser.ArgumentAssignmentListExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1298
                if not self.was(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.was(EParser.WS)")
                self.state = 1299 
                localctx.exp = self.expression(0)
                self.state = 1305
                la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                if la_ == 1:
                    self.state = 1300 
                    localctx.items = self.with_argument_assignment_list(0)
                    self.state = 1303
                    la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
                    if la_ == 1:
                        self.state = 1301
                        self.match(EParser.AND)
                        self.state = 1302 
                        localctx.item = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ArgumentAssignmentListNoExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1307 
                localctx.items = self.with_argument_assignment_list(0)
                self.state = 1310
                la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
                if la_ == 1:
                    self.state = 1308
                    self.match(EParser.AND)
                    self.state = 1309 
                    localctx.item = self.argument_assignment()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.With_argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_with_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(EParser.With_argument_assignment_listContext, self).copyFrom(ctx)


    class ArgumentAssignmentListContext(With_argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.With_argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentList(self)


    class ArgumentAssignmentListItemContext(With_argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.With_argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListItemContext, self).__init__(parser)
            self.items = None # With_argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentListItem(self)



    def with_argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.With_argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_with_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentAssignmentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1315
            self.match(EParser.WITH)
            self.state = 1316 
            localctx.item = self.argument_assignment()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentAssignmentListItemContext(self, EParser.With_argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_with_argument_assignment_list)
                    self.state = 1318
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1319
                    self.match(EParser.COMMA)
                    self.state = 1320 
                    localctx.item = self.argument_assignment() 
                self.state = 1325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Argument_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Argument_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_argument_assignment

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = EParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1326 
            localctx.exp = self.expression(0)
            self.state = 1327
            self.match(EParser.AS)
            self.state = 1328 
            localctx.name = self.variable_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_instance_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assign_instance_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.inst = None # Assignable_instanceContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def assignable_instance(self):
            return self.getTypedRuleContext(EParser.Assignable_instanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assign_instance_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = EParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1330 
            localctx.inst = self.assignable_instance(0)
            self.state = 1331 
            self.assign()
            self.state = 1332 
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
            super(EParser.Child_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_child_instance

     
        def copyFrom(self, ctx):
            super(EParser.Child_instanceContext, self).copyFrom(ctx)



    class MemberInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Child_instanceContext)
            super(EParser.MemberInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMemberInstance(self)


    class ItemInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Child_instanceContext)
            super(EParser.ItemInstanceContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = EParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_child_instance)
        try:
            self.state = 1342
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1334
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1335
                self.match(EParser.DOT)
                self.state = 1336 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1337
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1338
                self.match(EParser.LBRAK)
                self.state = 1339 
                localctx.exp = self.expression(0)
                self.state = 1340
                self.match(EParser.RBRAK)
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
            super(EParser.Assign_tuple_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(EParser.Variable_identifier_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assign_tuple_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = EParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1344 
            localctx.items = self.variable_identifier_list()
            self.state = 1345 
            self.assign()
            self.state = 1346 
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
            super(EParser.LfsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_lfs

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLfs(self)




    def lfs(self):

        localctx = EParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1348
                    self.match(EParser.LF) 
                self.state = 1353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.LfpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_lfp

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLfp(self)




    def lfp(self):

        localctx = EParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1355 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1354
                self.match(EParser.LF)
                self.state = 1357 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EParser.LF):
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
            super(EParser.IndentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(EParser.INDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_indent

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIndent(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIndent(self)




    def indent(self):

        localctx = EParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1360 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1359
                self.match(EParser.LF)
                self.state = 1362 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EParser.LF):
                    break

            self.state = 1364
            self.match(EParser.INDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DedentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DedentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DEDENT(self):
            return self.getToken(EParser.DEDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_dedent

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDedent(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDedent(self)




    def dedent(self):

        localctx = EParser.DedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.LF:
                self.state = 1366
                self.match(EParser.LF)
                self.state = 1371
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1372
            self.match(EParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Null_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NOTHING(self):
            return self.getToken(EParser.NOTHING, 0)

        def getRuleIndex(self):
            return EParser.RULE_null_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = EParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1374
            self.match(EParser.NOTHING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_declaration_list

     
        def copyFrom(self, ctx):
            super(EParser.Declaration_listContext, self).copyFrom(ctx)



    class FullDeclarationListContext(Declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Declaration_listContext)
            super(EParser.FullDeclarationListContext, self).__init__(parser)
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(EParser.LfsContext,0)

        def EOF(self):
            return self.getToken(EParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(EParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = EParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = EParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1377
            _la = self._input.LA(1)
            if _la==EParser.COMMENT or _la==EParser.DEFINE:
                self.state = 1376 
                self.declarations()


            self.state = 1379 
            self.lfs()
            self.state = 1380
            self.match(EParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DeclarationsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(EParser.DeclarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_declarations

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDeclarations(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = EParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1382 
            self.declaration()
            self.state = 1388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1383 
                    self.lfp()
                    self.state = 1384 
                    self.declaration() 
                self.state = 1390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(EParser.Attribute_declarationContext,0)


        def category_declaration(self):
            return self.getTypedRuleContext(EParser.Category_declarationContext,0)


        def resource_declaration(self):
            return self.getTypedRuleContext(EParser.Resource_declarationContext,0)


        def enum_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(EParser.Method_declarationContext,0)


        def comment_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Comment_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Comment_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = EParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMENT:
                self.state = 1391 
                self.comment_statement()
                self.state = 1392 
                self.lfp()
                self.state = 1398
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1404
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.state = 1399 
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1400 
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1401 
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1402 
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1403 
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
            super(EParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_resource_declaration(self):
            return self.getTypedRuleContext(EParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = EParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1406 
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
            super(EParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enum_category_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_category_declarationContext,0)


        def enum_native_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_native_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_enum_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnum_declaration(self)




    def enum_declaration(self):

        localctx = EParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_enum_declaration)
        try:
            self.state = 1410
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1408 
                self.enum_category_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1409 
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
            super(EParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Native_symbolContext)
            else:
                return self.getTypedRuleContext(EParser.Native_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_native_symbol_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_symbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_symbol_list(self)




    def native_symbol_list(self):

        localctx = EParser.Native_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_native_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1412 
            self.native_symbol()
            self.state = 1418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,90,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1413 
                    self.lfp()
                    self.state = 1414 
                    self.native_symbol() 
                self.state = 1420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,90,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Category_symbolContext)
            else:
                return self.getTypedRuleContext(EParser.Category_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_category_symbol_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategory_symbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategory_symbol_list(self)




    def category_symbol_list(self):

        localctx = EParser.Category_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_category_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1421 
            self.category_symbol()
            self.state = 1427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,91,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1422 
                    self.lfp()
                    self.state = 1423 
                    self.category_symbol() 
                self.state = 1429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,91,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def symbol_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Symbol_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Symbol_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_symbol_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbol_list(self)




    def symbol_list(self):

        localctx = EParser.Symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1430 
            self.symbol_identifier()
            self.state = 1435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1431
                self.match(EParser.COMMA)
                self.state = 1432 
                self.symbol_identifier()
                self.state = 1437
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
            super(EParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(EParser.Attribute_constraintContext, self).copyFrom(ctx)



    class MatchingSetContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingSetContext, self).__init__(parser)
            self.source = None # Set_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def set_literal(self):
            return self.getTypedRuleContext(EParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingSet(self)


    class MatchingPatternContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingPatternContext, self).__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(EParser.MATCHING, 0)
        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingPattern(self)


    class MatchingListContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingListContext, self).__init__(parser)
            self.source = None # List_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def list_literal(self):
            return self.getTypedRuleContext(EParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingList(self)


    class MatchingRangeContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingRangeContext, self).__init__(parser)
            self.source = None # Range_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def range_literal(self):
            return self.getTypedRuleContext(EParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingRange(self)


    class MatchingExpressionContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(EParser.MATCHING, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = EParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_attribute_constraint)
        try:
            self.state = 1448
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                localctx = EParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1438
                self.match(EParser.IN)
                self.state = 1439 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = EParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1440
                self.match(EParser.IN)
                self.state = 1441 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = EParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1442
                self.match(EParser.IN)
                self.state = 1443 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = EParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1444
                self.match(EParser.MATCHING)
                self.state = 1445
                localctx.text = self.match(EParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = EParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1446
                self.match(EParser.MATCHING)
                self.state = 1447 
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
            super(EParser.List_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_list_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = EParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1451
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1450
                self.match(EParser.MUTABLE)


            self.state = 1453
            self.match(EParser.LBRAK)
            self.state = 1455
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)) | (1 << (EParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (EParser.TEXT_LITERAL - 164)) | (1 << (EParser.UUID_LITERAL - 164)) | (1 << (EParser.INTEGER_LITERAL - 164)) | (1 << (EParser.HEXA_LITERAL - 164)) | (1 << (EParser.DECIMAL_LITERAL - 164)) | (1 << (EParser.DATETIME_LITERAL - 164)) | (1 << (EParser.TIME_LITERAL - 164)) | (1 << (EParser.DATE_LITERAL - 164)) | (1 << (EParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1454 
                self.expression_list()


            self.state = 1457
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Set_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(EParser.LT, 0)

        def GT(self):
            return self.getToken(EParser.GT, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_set_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = EParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1460
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1459
                self.match(EParser.MUTABLE)


            self.state = 1462
            self.match(EParser.LT)
            self.state = 1464
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)) | (1 << (EParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (EParser.TEXT_LITERAL - 164)) | (1 << (EParser.UUID_LITERAL - 164)) | (1 << (EParser.INTEGER_LITERAL - 164)) | (1 << (EParser.HEXA_LITERAL - 164)) | (1 << (EParser.DECIMAL_LITERAL - 164)) | (1 << (EParser.DATETIME_LITERAL - 164)) | (1 << (EParser.TIME_LITERAL - 164)) | (1 << (EParser.DATE_LITERAL - 164)) | (1 << (EParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1463 
                self.expression_list()


            self.state = 1466
            self.match(EParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_expression_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterExpression_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = EParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1468 
            self.expression(0)
            self.state = 1473
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1469
                self.match(EParser.COMMA)
                self.state = 1470 
                self.expression(0)
                self.state = 1475
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
            super(EParser.Range_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.low = None # ExpressionContext
            self.high = None # ExpressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RANGE(self):
            return self.getToken(EParser.RANGE, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_range_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = EParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1476
            self.match(EParser.LBRAK)
            self.state = 1477 
            localctx.low = self.expression(0)
            self.state = 1478
            self.match(EParser.RANGE)
            self.state = 1479 
            localctx.high = self.expression(0)
            self.state = 1480
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.TypedefContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_typedef

     
        def copyFrom(self, ctx):
            super(EParser.TypedefContext, self).copyFrom(ctx)


    class IteratorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.IteratorTypeContext, self).__init__(parser)
            self.i = None # TypedefContext
            self.copyFrom(ctx)

        def ITERATOR(self):
            return self.getToken(EParser.ITERATOR, 0)
        def LT(self):
            return self.getToken(EParser.LT, 0)
        def GT(self):
            return self.getToken(EParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIteratorType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIteratorType(self)


    class SetTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.SetTypeContext, self).__init__(parser)
            self.s = None # TypedefContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(EParser.LTGT, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSetType(self)


    class ListTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.ListTypeContext, self).__init__(parser)
            self.l = None # TypedefContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterListType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitListType(self)


    class DictTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.DictTypeContext, self).__init__(parser)
            self.d = None # TypedefContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDictType(self)


    class CursorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.CursorTypeContext, self).__init__(parser)
            self.c = None # TypedefContext
            self.copyFrom(ctx)

        def CURSOR(self):
            return self.getToken(EParser.CURSOR, 0)
        def LT(self):
            return self.getToken(EParser.LT, 0)
        def GT(self):
            return self.getToken(EParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCursorType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCursorType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(EParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPrimaryType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 166
        self.enterRecursionRule(localctx, 166, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1494
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1483 
                localctx.p = self.primary_type()

            elif token in [EParser.CURSOR]:
                localctx = EParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1484
                self.match(EParser.CURSOR)
                self.state = 1485
                self.match(EParser.LT)
                self.state = 1486 
                localctx.c = self.typedef(0)
                self.state = 1487
                self.match(EParser.GT)

            elif token in [EParser.ITERATOR]:
                localctx = EParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1489
                self.match(EParser.ITERATOR)
                self.state = 1490
                self.match(EParser.LT)
                self.state = 1491 
                localctx.i = self.typedef(0)
                self.state = 1492
                self.match(EParser.GT)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1506
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,101,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1504
                    la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
                    if la_ == 1:
                        localctx = EParser.SetTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1496
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1497
                        self.match(EParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = EParser.ListTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1498
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1499
                        self.match(EParser.LBRAK)
                        self.state = 1500
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = EParser.DictTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1501
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1502
                        self.match(EParser.LCURL)
                        self.state = 1503
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1508
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,101,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(EParser.Primary_typeContext, self).copyFrom(ctx)



    class NativeTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Primary_typeContext)
            super(EParser.NativeTypeContext, self).__init__(parser)
            self.n = None # Native_typeContext
            self.copyFrom(ctx)

        def native_type(self):
            return self.getTypedRuleContext(EParser.Native_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Primary_typeContext)
            super(EParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = EParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_primary_type)
        try:
            self.state = 1511
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID]:
                localctx = EParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1509 
                localctx.n = self.native_type()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1510 
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
            super(EParser.Native_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_type

     
        def copyFrom(self, ctx):
            super(EParser.Native_typeContext, self).copyFrom(ctx)



    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.PeriodTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPeriodType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(EParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCharacterType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(EParser.IMAGE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(EParser.BLOB, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(EParser.UUID, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(EParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateType(self)



    def native_type(self):

        localctx = EParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_native_type)
        try:
            self.state = 1527
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN]:
                localctx = EParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1513
                self.match(EParser.BOOLEAN)

            elif token in [EParser.CHARACTER]:
                localctx = EParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1514
                self.match(EParser.CHARACTER)

            elif token in [EParser.TEXT]:
                localctx = EParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1515
                self.match(EParser.TEXT)

            elif token in [EParser.IMAGE]:
                localctx = EParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1516
                self.match(EParser.IMAGE)

            elif token in [EParser.INTEGER]:
                localctx = EParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1517
                self.match(EParser.INTEGER)

            elif token in [EParser.DECIMAL]:
                localctx = EParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1518
                self.match(EParser.DECIMAL)

            elif token in [EParser.DOCUMENT]:
                localctx = EParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1519
                self.match(EParser.DOCUMENT)

            elif token in [EParser.DATE]:
                localctx = EParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1520
                self.match(EParser.DATE)

            elif token in [EParser.DATETIME]:
                localctx = EParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1521
                self.match(EParser.DATETIME)

            elif token in [EParser.TIME]:
                localctx = EParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1522
                self.match(EParser.TIME)

            elif token in [EParser.PERIOD]:
                localctx = EParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1523
                self.match(EParser.PERIOD)

            elif token in [EParser.CODE]:
                localctx = EParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1524
                self.match(EParser.CODE)

            elif token in [EParser.BLOB]:
                localctx = EParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1525
                self.match(EParser.BLOB)

            elif token in [EParser.UUID]:
                localctx = EParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1526
                self.match(EParser.UUID)

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
            super(EParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_category_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = EParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1529
            localctx.t1 = self.match(EParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutable_category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Mutable_category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def getRuleIndex(self):
            return EParser.RULE_mutable_category_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = EParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1532
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1531
                self.match(EParser.MUTABLE)


            self.state = 1534 
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
            super(EParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(EParser.CODE, 0)

        def getRuleIndex(self):
            return EParser.RULE_code_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = EParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1536
            localctx.t1 = self.match(EParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_category_declaration

     
        def copyFrom(self, ctx):
            super(EParser.Category_declarationContext, self).copyFrom(ctx)



    class ConcreteCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.ConcreteCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_category_declarationContext
            self.copyFrom(ctx)

        def concrete_category_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(EParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(EParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = EParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_category_declaration)
        try:
            self.state = 1541
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                localctx = EParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1538 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1539 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1540 
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
            super(EParser.Type_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Type_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_type_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterType_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitType_identifier_list(self)




    def type_identifier_list(self):

        localctx = EParser.Type_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_type_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1543 
            self.type_identifier()
            self.state = 1548
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1544
                self.match(EParser.COMMA)
                self.state = 1545 
                self.type_identifier()
                self.state = 1550
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
            super(EParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_method_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethod_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethod_identifier(self)




    def method_identifier(self):

        localctx = EParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_method_identifier)
        try:
            self.state = 1553
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1551 
                self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1552 
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
            super(EParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(EParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.TypeIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.SymbolIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.VariableIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = EParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_identifier)
        try:
            self.state = 1558
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1555 
                self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1556 
                self.type_identifier()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                localctx = EParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1557 
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
            super(EParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_variable_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = EParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1560
            self.match(EParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def getRuleIndex(self):
            return EParser.RULE_attribute_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = EParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1562
            _la = self._input.LA(1)
            if not(_la==EParser.STORABLE or _la==EParser.VARIABLE_IDENTIFIER):
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
            super(EParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_type_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = EParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1564
            self.match(EParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Symbol_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_symbol_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = EParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1566
            self.match(EParser.SYMBOL_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(EParser.ArgumentContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_argument_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = EParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1568 
            self.argument()
            self.state = 1573
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1569
                self.match(EParser.COMMA)
                self.state = 1570 
                self.argument()
                self.state = 1575
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
            super(EParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_argument

     
        def copyFrom(self, ctx):
            super(EParser.ArgumentContext, self).copyFrom(ctx)



    class OperatorArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a EParser.ArgumentContext)
            super(EParser.OperatorArgumentContext, self).__init__(parser)
            self.arg = None # Operator_argumentContext
            self.copyFrom(ctx)

        def operator_argument(self):
            return self.getTypedRuleContext(EParser.Operator_argumentContext,0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a EParser.ArgumentContext)
            super(EParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(EParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = EParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1581
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                localctx = EParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1576 
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = EParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1578
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE:
                    self.state = 1577
                    self.match(EParser.MUTABLE)


                self.state = 1580 
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
            super(EParser.Operator_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def named_argument(self):
            return self.getTypedRuleContext(EParser.Named_argumentContext,0)


        def typed_argument(self):
            return self.getTypedRuleContext(EParser.Typed_argumentContext,0)


        def getRuleIndex(self):
            return EParser.RULE_operator_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperator_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperator_argument(self)




    def operator_argument(self):

        localctx = EParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_operator_argument)
        try:
            self.state = 1585
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1583 
                self.named_argument()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.ITERATOR, EParser.CURSOR, EParser.ANY, EParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1584 
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
            super(EParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(EParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_named_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = EParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1587 
            self.variable_identifier()
            self.state = 1590
            _la = self._input.LA(1)
            if _la==EParser.EQ:
                self.state = 1588
                self.match(EParser.EQ)
                self.state = 1589 
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
            super(EParser.Code_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def code_type(self):
            return self.getTypedRuleContext(EParser.Code_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_code_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = EParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1592 
            self.code_type()
            self.state = 1593 
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
            super(EParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)


        def getRuleIndex(self):
            return EParser.RULE_category_or_any_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategory_or_any_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategory_or_any_type(self)




    def category_or_any_type(self):

        localctx = EParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_category_or_any_type)
        try:
            self.state = 1597
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.ITERATOR, EParser.CURSOR, EParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1595 
                self.typedef(0)

            elif token in [EParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1596 
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
            super(EParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(EParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyListTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(EParser.ANY, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyDictTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 206
        self.enterRecursionRule(localctx, 206, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1600
            self.match(EParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1610
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,116,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1608
                    la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
                    if la_ == 1:
                        localctx = EParser.AnyListTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1602
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1603
                        self.match(EParser.LBRAK)
                        self.state = 1604
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = EParser.AnyDictTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1605
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1606
                        self.match(EParser.LCURL)
                        self.state = 1607
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1612
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,116,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Member_method_declarationContext)
            else:
                return self.getTypedRuleContext(EParser.Member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_member_method_declaration_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMember_method_declaration_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMember_method_declaration_list(self)




    def member_method_declaration_list(self):

        localctx = EParser.Member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1613 
            self.member_method_declaration()
            self.state = 1619
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1614 
                    self.lfp()
                    self.state = 1615 
                    self.member_method_declaration() 
                self.state = 1621
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,117,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def setter_method_declaration(self):
            return self.getTypedRuleContext(EParser.Setter_method_declarationContext,0)


        def getter_method_declaration(self):
            return self.getTypedRuleContext(EParser.Getter_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def abstract_method_declaration(self):
            return self.getTypedRuleContext(EParser.Abstract_method_declarationContext,0)


        def operator_method_declaration(self):
            return self.getTypedRuleContext(EParser.Operator_method_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = EParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_member_method_declaration)
        try:
            self.state = 1627
            la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1622 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1623 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1624 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1625 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1626 
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
            super(EParser.Native_member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Native_member_method_declarationContext)
            else:
                return self.getTypedRuleContext(EParser.Native_member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_native_member_method_declaration_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_member_method_declaration_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_member_method_declaration_list(self)




    def native_member_method_declaration_list(self):

        localctx = EParser.Native_member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_native_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1629 
            self.native_member_method_declaration()
            self.state = 1635
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,119,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1630 
                    self.lfp()
                    self.state = 1631 
                    self.native_member_method_declaration() 
                self.state = 1637
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,119,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_getter_declaration(self):
            return self.getTypedRuleContext(EParser.Native_getter_declarationContext,0)


        def native_setter_declaration(self):
            return self.getTypedRuleContext(EParser.Native_setter_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_method_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = EParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_native_member_method_declaration)
        try:
            self.state = 1641
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1638 
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1639 
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1640 
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
            super(EParser.Native_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_category_binding

     
        def copyFrom(self, ctx):
            super(EParser.Native_category_bindingContext, self).copyFrom(ctx)



    class Python2CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.Python2CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(EParser.PYTHON2, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(EParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython2CategoryBinding(self)


    class Python3CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.Python3CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(EParser.PYTHON3, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(EParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython3CategoryBinding(self)


    class JavaCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.JavaCategoryBindingContext, self).__init__(parser)
            self.binding = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(EParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaCategoryBinding(self)


    class CSharpCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.CSharpCategoryBindingContext, self).__init__(parser)
            self.binding = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(EParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpCategoryBinding(self)


    class JavaScriptCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.JavaScriptCategoryBindingContext, self).__init__(parser)
            self.binding = None # Javascript_category_bindingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(EParser.JAVASCRIPT, 0)
        def javascript_category_binding(self):
            return self.getTypedRuleContext(EParser.Javascript_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = EParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_native_category_binding)
        try:
            self.state = 1653
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1643
                self.match(EParser.JAVA)
                self.state = 1644 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1645
                self.match(EParser.CSHARP)
                self.state = 1646 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1647
                self.match(EParser.PYTHON2)
                self.state = 1648 
                localctx.binding = self.python_category_binding()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1649
                self.match(EParser.PYTHON3)
                self.state = 1650 
                localctx.binding = self.python_category_binding()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1651
                self.match(EParser.JAVASCRIPT)
                self.state = 1652 
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
            super(EParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(EParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_category_binding

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = EParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1655 
            self.identifier()
            self.state = 1657
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                self.state = 1656 
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
            super(EParser.Python_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(EParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(EParser.DOT)
            else:
                return self.getToken(EParser.DOT, i)

        def getRuleIndex(self):
            return EParser.RULE_python_module

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = EParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1659
            self.match(EParser.FROM)
            self.state = 1660 
            self.module_token()
            self.state = 1661
            self.match(EParser.COLON)
            self.state = 1662 
            self.identifier()
            self.state = 1667
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,123,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1663
                    self.match(EParser.DOT)
                    self.state = 1664 
                    self.identifier() 
                self.state = 1669
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,123,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(EParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_category_binding

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = EParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1670 
            self.identifier()
            self.state = 1672
            la_ = self._interp.adaptivePredict(self._input,124,self._ctx)
            if la_ == 1:
                self.state = 1671 
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
            super(EParser.Javascript_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(EParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def javascript_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Javascript_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Javascript_identifierContext,i)


        def SLASH(self, i=None):
            if i is None:
                return self.getTokens(EParser.SLASH)
            else:
                return self.getToken(EParser.SLASH, i)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)

        def getRuleIndex(self):
            return EParser.RULE_javascript_module

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = EParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1674
            self.match(EParser.FROM)
            self.state = 1675 
            self.module_token()
            self.state = 1676
            self.match(EParser.COLON)
            self.state = 1678
            _la = self._input.LA(1)
            if _la==EParser.SLASH:
                self.state = 1677
                self.match(EParser.SLASH)


            self.state = 1680 
            self.javascript_identifier()
            self.state = 1685
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1681
                    self.match(EParser.SLASH)
                    self.state = 1682 
                    self.javascript_identifier() 
                self.state = 1687
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

            self.state = 1690
            la_ = self._interp.adaptivePredict(self._input,127,self._ctx)
            if la_ == 1:
                self.state = 1688
                self.match(EParser.DOT)
                self.state = 1689 
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
            super(EParser.Variable_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Variable_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_variable_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = EParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1692 
            self.variable_identifier()
            self.state = 1697
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1693
                self.match(EParser.COMMA)
                self.state = 1694 
                self.variable_identifier()
                self.state = 1699
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
            super(EParser.Attribute_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Attribute_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Attribute_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_attribute_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = EParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_attribute_identifier_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1700 
            self.attribute_identifier()
            self.state = 1705
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1701
                    self.match(EParser.COMMA)
                    self.state = 1702 
                    self.attribute_identifier() 
                self.state = 1707
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(EParser.Abstract_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_method_declarationContext,0)


        def test_method_declaration(self):
            return self.getTypedRuleContext(EParser.Test_method_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = EParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_method_declaration)
        try:
            self.state = 1712
            la_ = self._interp.adaptivePredict(self._input,130,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1708 
                self.abstract_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1709 
                self.concrete_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1710 
                self.native_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1711 
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
            super(EParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(EParser.COMMENT, 0)

        def getRuleIndex(self):
            return EParser.RULE_comment_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = EParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1714
            self.match(EParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Native_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Native_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_native_statement_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_statement_list(self)




    def native_statement_list(self):

        localctx = EParser.Native_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_native_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1716 
            self.native_statement()
            self.state = 1722
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,131,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1717 
                    self.lfp()
                    self.state = 1718 
                    self.native_statement() 
                self.state = 1724
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,131,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(EParser.Native_statementContext, self).copyFrom(ctx)



    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.CSharpNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(EParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(EParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.JavaNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(EParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(EParser.Java_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(EParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(EParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptNativeStatement(self)


    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.Python2NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(EParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(EParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython2NativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.Python3NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(EParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(EParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = EParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_native_statement)
        try:
            self.state = 1735
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1725
                self.match(EParser.JAVA)
                self.state = 1726 
                self.java_statement()

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1727
                self.match(EParser.CSHARP)
                self.state = 1728 
                self.csharp_statement()

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1729
                self.match(EParser.PYTHON2)
                self.state = 1730 
                self.python_native_statement()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1731
                self.match(EParser.PYTHON3)
                self.state = 1732 
                self.python_native_statement()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1733
                self.match(EParser.JAVASCRIPT)
                self.state = 1734 
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
            super(EParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def python_statement(self):
            return self.getTypedRuleContext(EParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(EParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_native_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = EParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1737 
            self.python_statement()
            self.state = 1739
            _la = self._input.LA(1)
            if _la==EParser.SEMI:
                self.state = 1738
                self.match(EParser.SEMI)


            self.state = 1742
            _la = self._input.LA(1)
            if _la==EParser.FROM:
                self.state = 1741 
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
            super(EParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_statement(self):
            return self.getTypedRuleContext(EParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(EParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = EParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1744 
            self.javascript_statement()
            self.state = 1746
            _la = self._input.LA(1)
            if _la==EParser.SEMI:
                self.state = 1745
                self.match(EParser.SEMI)


            self.state = 1749
            _la = self._input.LA(1)
            if _la==EParser.FROM:
                self.state = 1748 
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
            super(EParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.StatementContext)
            else:
                return self.getTypedRuleContext(EParser.StatementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_statement_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStatement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = EParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1751 
            self.statement()
            self.state = 1757
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1752 
                    self.lfp()
                    self.state = 1753 
                    self.statement() 
                self.state = 1759
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assertion(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.AssertionContext)
            else:
                return self.getTypedRuleContext(EParser.AssertionContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_assertion_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssertion_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssertion_list(self)




    def assertion_list(self):

        localctx = EParser.Assertion_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_assertion_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1760 
            self.assertion()
            self.state = 1766
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,138,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1761 
                    self.lfp()
                    self.state = 1762 
                    self.assertion() 
                self.state = 1768
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,138,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def switch_case_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Switch_case_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Switch_case_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_switch_case_statement_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitch_case_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitch_case_statement_list(self)




    def switch_case_statement_list(self):

        localctx = EParser.Switch_case_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_switch_case_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1769 
            self.switch_case_statement()
            self.state = 1775
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1770 
                    self.lfp()
                    self.state = 1771 
                    self.switch_case_statement() 
                self.state = 1777
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,139,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def catch_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Catch_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Catch_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_catch_statement_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatch_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatch_statement_list(self)




    def catch_statement_list(self):

        localctx = EParser.Catch_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1778 
            self.catch_statement()
            self.state = 1784
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1779 
                    self.lfp()
                    self.state = 1780 
                    self.catch_statement() 
                self.state = 1786
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,140,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_collectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(EParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralListLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralListLiteral(self)


    class LiteralRangeLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralRangeLiteralContext, self).__init__(parser)
            self.low = None # Atomic_literalContext
            self.high = None # Atomic_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RANGE(self):
            return self.getToken(EParser.RANGE, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(EParser.Atomic_literalContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralRangeLiteral(self)


    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralSetLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(EParser.LT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)

        def GT(self):
            return self.getToken(EParser.GT, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = EParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_literal_collection)
        try:
            self.state = 1801
            la_ = self._interp.adaptivePredict(self._input,141,self._ctx)
            if la_ == 1:
                localctx = EParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1787
                self.match(EParser.LBRAK)
                self.state = 1788 
                localctx.low = self.atomic_literal()
                self.state = 1789
                self.match(EParser.RANGE)
                self.state = 1790 
                localctx.high = self.atomic_literal()
                self.state = 1791
                self.match(EParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = EParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1793
                self.match(EParser.LBRAK)
                self.state = 1794 
                self.literal_list_literal()
                self.state = 1795
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1797
                self.match(EParser.LT)
                self.state = 1798 
                self.literal_list_literal()
                self.state = 1799
                self.match(EParser.GT)
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
            super(EParser.Atomic_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_atomic_literal

     
        def copyFrom(self, ctx):
            super(EParser.Atomic_literalContext, self).copyFrom(ctx)



    class MinIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.MinIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MIN_INTEGER(self):
            return self.getToken(EParser.MIN_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(EParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBooleanLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(EParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitHexadecimalLiteral(self)


    class UUIDLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.UUIDLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def UUID_LITERAL(self):
            return self.getToken(EParser.UUID_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUUIDLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUUIDLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(EParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(EParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(EParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(EParser.Null_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(EParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = EParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_atomic_literal)
        try:
            self.state = 1817
            token = self._input.LA(1)
            if token in [EParser.MIN_INTEGER]:
                localctx = EParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1803
                localctx.t = self.match(EParser.MIN_INTEGER)

            elif token in [EParser.MAX_INTEGER]:
                localctx = EParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1804
                localctx.t = self.match(EParser.MAX_INTEGER)

            elif token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1805
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.HEXA_LITERAL]:
                localctx = EParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1806
                localctx.t = self.match(EParser.HEXA_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1807
                localctx.t = self.match(EParser.CHAR_LITERAL)

            elif token in [EParser.DATE_LITERAL]:
                localctx = EParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1808
                localctx.t = self.match(EParser.DATE_LITERAL)

            elif token in [EParser.TIME_LITERAL]:
                localctx = EParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1809
                localctx.t = self.match(EParser.TIME_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1810
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1811
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.DATETIME_LITERAL]:
                localctx = EParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1812
                localctx.t = self.match(EParser.DATETIME_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1813
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.PERIOD_LITERAL]:
                localctx = EParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1814
                localctx.t = self.match(EParser.PERIOD_LITERAL)

            elif token in [EParser.UUID_LITERAL]:
                localctx = EParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1815
                localctx.t = self.match(EParser.UUID_LITERAL)

            elif token in [EParser.NOTHING]:
                localctx = EParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1816 
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
            super(EParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(EParser.Atomic_literalContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_literal_list_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteral_list_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteral_list_literal(self)




    def literal_list_literal(self):

        localctx = EParser.Literal_list_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1819 
            self.atomic_literal()
            self.state = 1824
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1820
                self.match(EParser.COMMA)
                self.state = 1821 
                self.atomic_literal()
                self.state = 1826
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
            super(EParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(EParser.Selectable_expressionContext, self).copyFrom(ctx)



    class ThisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.ThisExpressionContext, self).__init__(parser)
            self.exp = None # This_expressionContext
            self.copyFrom(ctx)

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = EParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_selectable_expression)
        try:
            self.state = 1831
            la_ = self._interp.adaptivePredict(self._input,144,self._ctx)
            if la_ == 1:
                localctx = EParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1827 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1828 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = EParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1829 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = EParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1830 
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
            super(EParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(EParser.SELF, 0)

        def THIS(self):
            return self.getToken(EParser.THIS, 0)

        def getRuleIndex(self):
            return EParser.RULE_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = EParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1833
            _la = self._input.LA(1)
            if not(_la==EParser.SELF or _la==EParser.THIS):
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
            super(EParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def getRuleIndex(self):
            return EParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = EParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1835
            self.match(EParser.LPAR)
            self.state = 1836 
            self.expression(0)
            self.state = 1837
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)


        def collection_literal(self):
            return self.getTypedRuleContext(EParser.Collection_literalContext,0)


        def getRuleIndex(self):
            return EParser.RULE_literal_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = EParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_literal_expression)
        try:
            self.state = 1841
            token = self._input.LA(1)
            if token in [EParser.NOTHING, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.MIN_INTEGER, EParser.MAX_INTEGER, EParser.TEXT_LITERAL, EParser.UUID_LITERAL, EParser.INTEGER_LITERAL, EParser.HEXA_LITERAL, EParser.DECIMAL_LITERAL, EParser.DATETIME_LITERAL, EParser.TIME_LITERAL, EParser.DATE_LITERAL, EParser.PERIOD_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1839 
                self.atomic_literal()

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.LCURL, EParser.LT, EParser.MUTABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1840 
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
            super(EParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def range_literal(self):
            return self.getTypedRuleContext(EParser.Range_literalContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(EParser.List_literalContext,0)


        def set_literal(self):
            return self.getTypedRuleContext(EParser.Set_literalContext,0)


        def dict_literal(self):
            return self.getTypedRuleContext(EParser.Dict_literalContext,0)


        def tuple_literal(self):
            return self.getTypedRuleContext(EParser.Tuple_literalContext,0)


        def getRuleIndex(self):
            return EParser.RULE_collection_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCollection_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCollection_literal(self)




    def collection_literal(self):

        localctx = EParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_collection_literal)
        try:
            self.state = 1848
            la_ = self._interp.adaptivePredict(self._input,146,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1843 
                self.range_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1844 
                self.list_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1845 
                self.set_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1846 
                self.dict_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1847 
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
            super(EParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(EParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_tuple_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = EParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1851
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1850
                self.match(EParser.MUTABLE)


            self.state = 1853
            self.match(EParser.LPAR)
            self.state = 1855
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)) | (1 << (EParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (EParser.TEXT_LITERAL - 164)) | (1 << (EParser.UUID_LITERAL - 164)) | (1 << (EParser.INTEGER_LITERAL - 164)) | (1 << (EParser.HEXA_LITERAL - 164)) | (1 << (EParser.DECIMAL_LITERAL - 164)) | (1 << (EParser.DATETIME_LITERAL - 164)) | (1 << (EParser.TIME_LITERAL - 164)) | (1 << (EParser.DATE_LITERAL - 164)) | (1 << (EParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1854 
                self.expression_tuple()


            self.state = 1857
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Dict_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(EParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_dict_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = EParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1860
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1859
                self.match(EParser.MUTABLE)


            self.state = 1862
            self.match(EParser.LCURL)
            self.state = 1864
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)) | (1 << (EParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (EParser.TEXT_LITERAL - 164)) | (1 << (EParser.UUID_LITERAL - 164)) | (1 << (EParser.INTEGER_LITERAL - 164)) | (1 << (EParser.HEXA_LITERAL - 164)) | (1 << (EParser.DECIMAL_LITERAL - 164)) | (1 << (EParser.DATETIME_LITERAL - 164)) | (1 << (EParser.TIME_LITERAL - 164)) | (1 << (EParser.DATE_LITERAL - 164)) | (1 << (EParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1863 
                self.dict_entry_list()


            self.state = 1866
            self.match(EParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Expression_tupleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_expression_tuple

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterExpression_tuple(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitExpression_tuple(self)




    def expression_tuple(self):

        localctx = EParser.Expression_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1868 
            self.expression(0)
            self.state = 1869
            self.match(EParser.COMMA)
            self.state = 1878
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)) | (1 << (EParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (EParser.TEXT_LITERAL - 164)) | (1 << (EParser.UUID_LITERAL - 164)) | (1 << (EParser.INTEGER_LITERAL - 164)) | (1 << (EParser.HEXA_LITERAL - 164)) | (1 << (EParser.DECIMAL_LITERAL - 164)) | (1 << (EParser.DATETIME_LITERAL - 164)) | (1 << (EParser.TIME_LITERAL - 164)) | (1 << (EParser.DATE_LITERAL - 164)) | (1 << (EParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1870 
                self.expression(0)
                self.state = 1875
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==EParser.COMMA:
                    self.state = 1871
                    self.match(EParser.COMMA)
                    self.state = 1872 
                    self.expression(0)
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

    class Dict_entry_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dict_entry(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Dict_entryContext)
            else:
                return self.getTypedRuleContext(EParser.Dict_entryContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_dict_entry_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDict_entry_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDict_entry_list(self)




    def dict_entry_list(self):

        localctx = EParser.Dict_entry_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1880 
            self.dict_entry()
            self.state = 1885
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1881
                self.match(EParser.COMMA)
                self.state = 1882 
                self.dict_entry()
                self.state = 1887
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
            super(EParser.Dict_entryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExpressionContext
            self.value = None # ExpressionContext

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_dict_entry

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = EParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1888 
            localctx.key = self.expression(0)
            self.state = 1889
            self.match(EParser.COLON)
            self.state = 1890 
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
            super(EParser.Slice_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_slice_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Slice_argumentsContext, self).copyFrom(ctx)



    class SliceFirstAndLastContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Slice_argumentsContext)
            super(EParser.SliceFirstAndLastContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceFirstAndLast(self)


    class SliceLastOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Slice_argumentsContext)
            super(EParser.SliceLastOnlyContext, self).__init__(parser)
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceLastOnly(self)


    class SliceFirstOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Slice_argumentsContext)
            super(EParser.SliceFirstOnlyContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = EParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_slice_arguments)
        try:
            self.state = 1901
            la_ = self._interp.adaptivePredict(self._input,154,self._ctx)
            if la_ == 1:
                localctx = EParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1892 
                localctx.first = self.expression(0)
                self.state = 1893
                self.match(EParser.COLON)
                self.state = 1894 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1896 
                localctx.first = self.expression(0)
                self.state = 1897
                self.match(EParser.COLON)
                pass

            elif la_ == 3:
                localctx = EParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1899
                self.match(EParser.COLON)
                self.state = 1900 
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
            super(EParser.Assign_variable_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = EParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1903 
            self.variable_identifier()
            self.state = 1904 
            self.assign()
            self.state = 1905 
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
            super(EParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(EParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Assignable_instanceContext)
            super(EParser.ChildInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(EParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(EParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Assignable_instanceContext)
            super(EParser.RootInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRootInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 280
        self.enterRecursionRule(localctx, 280, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1908 
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1914
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,155,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ChildInstanceContext(self, EParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1910
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1911 
                    self.child_instance() 
                self.state = 1916
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,155,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Is_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Is_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_is_expression

     
        def copyFrom(self, ctx):
            super(EParser.Is_expressionContext, self).copyFrom(ctx)



    class IsATypeExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Is_expressionContext)
            super(EParser.IsATypeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Is_expressionContext)
            super(EParser.IsOtherExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = EParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_is_expression)
        try:
            self.state = 1921
            la_ = self._interp.adaptivePredict(self._input,156,self._ctx)
            if la_ == 1:
                localctx = EParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1917
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1918
                self.match(EParser.VARIABLE_IDENTIFIER)
                self.state = 1919 
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = EParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1920 
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
            super(EParser.Order_by_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def order_by(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Order_byContext)
            else:
                return self.getTypedRuleContext(EParser.Order_byContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_order_by_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = EParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_order_by_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1923 
            self.order_by()
            self.state = 1928
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1924
                    self.match(EParser.COMMA)
                    self.state = 1925 
                    self.order_by() 
                self.state = 1930
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_byContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Order_byContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Variable_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(EParser.DOT)
            else:
                return self.getToken(EParser.DOT, i)

        def ASC(self):
            return self.getToken(EParser.ASC, 0)

        def DESC(self):
            return self.getToken(EParser.DESC, 0)

        def getRuleIndex(self):
            return EParser.RULE_order_by

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = EParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1931 
            self.variable_identifier()
            self.state = 1936
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,158,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1932
                    self.match(EParser.DOT)
                    self.state = 1933 
                    self.variable_identifier() 
                self.state = 1938
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,158,self._ctx)

            self.state = 1940
            la_ = self._interp.adaptivePredict(self._input,159,self._ctx)
            if la_ == 1:
                self.state = 1939
                _la = self._input.LA(1)
                if not(_la==EParser.ASC or _la==EParser.DESC):
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
            super(EParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_operator

     
        def copyFrom(self, ctx):
            super(EParser.OperatorContext, self).copyFrom(ctx)



    class OperatorPlusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorPlusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(EParser.PLUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(EParser.DivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(EParser.IdivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(EParser.MultiplyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(EParser.ModuloContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = EParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_operator)
        try:
            self.state = 1948
            token = self._input.LA(1)
            if token in [EParser.PLUS]:
                localctx = EParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1942
                self.match(EParser.PLUS)

            elif token in [EParser.MINUS]:
                localctx = EParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1943
                self.match(EParser.MINUS)

            elif token in [EParser.STAR]:
                localctx = EParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1944 
                self.multiply()

            elif token in [EParser.SLASH]:
                localctx = EParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1945 
                self.divide()

            elif token in [EParser.BSLASH]:
                localctx = EParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1946 
                self.idivide()

            elif token in [EParser.PERCENT, EParser.MODULO]:
                localctx = EParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1947 
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
            super(EParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_new_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = EParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1950
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1951
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
            super(EParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_key_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = EParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1953
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1954
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
            super(EParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_module_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = EParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1956
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1957
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
            super(EParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_value_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = EParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1959
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1960
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
            super(EParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_symbols_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = EParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1962
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1963
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
            super(EParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(EParser.EQ, 0)

        def getRuleIndex(self):
            return EParser.RULE_assign

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign(self)




    def assign(self):

        localctx = EParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1965
            self.match(EParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.MultiplyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(EParser.STAR, 0)

        def getRuleIndex(self):
            return EParser.RULE_multiply

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = EParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1967
            self.match(EParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(EParser.SLASH, 0)

        def getRuleIndex(self):
            return EParser.RULE_divide

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDivide(self)




    def divide(self):

        localctx = EParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1969
            self.match(EParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.IdivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BSLASH(self):
            return self.getToken(EParser.BSLASH, 0)

        def getRuleIndex(self):
            return EParser.RULE_idivide

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = EParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1971
            self.match(EParser.BSLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuloContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.ModuloContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(EParser.PERCENT, 0)

        def MODULO(self):
            return self.getToken(EParser.MODULO, 0)

        def getRuleIndex(self):
            return EParser.RULE_modulo

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitModulo(self)




    def modulo(self):

        localctx = EParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1973
            _la = self._input.LA(1)
            if not(_la==EParser.PERCENT or _la==EParser.MODULO):
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
            super(EParser.Javascript_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_statement

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_statementContext, self).copyFrom(ctx)



    class JavascriptStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_statementContext)
            super(EParser.JavascriptStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptStatement(self)


    class JavascriptReturnStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_statementContext)
            super(EParser.JavascriptReturnStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = EParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_javascript_statement)
        try:
            self.state = 1982
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1975
                self.match(EParser.RETURN)
                self.state = 1976 
                localctx.exp = self.javascript_expression(0)
                self.state = 1977
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1979 
                localctx.exp = self.javascript_expression(0)
                self.state = 1980
                self.match(EParser.SEMI)

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
            super(EParser.Javascript_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_expressionContext, self).copyFrom(ctx)


    class JavascriptSelectorExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_expressionContext)
            super(EParser.JavascriptSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Javascript_expressionContext
            self.child = None # Javascript_selector_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)

        def javascript_selector_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_expressionContext)
            super(EParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 312
        self.enterRecursionRule(localctx, 312, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1985 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1991
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,162,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptSelectorExpressionContext(self, EParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1987
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1988 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1993
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,162,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_this_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_this_expressionContext,0)


        def javascript_new_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_new_expressionContext,0)


        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_parenthesis_expressionContext,0)


        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_identifier_expressionContext,0)


        def javascript_literal_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_literal_expressionContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_method_expressionContext,0)


        def javascript_item_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_item_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = EParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_javascript_primary_expression)
        try:
            self.state = 2001
            la_ = self._interp.adaptivePredict(self._input,163,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1994 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1995 
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1996 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1997 
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1998 
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1999 
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2000 
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
            super(EParser.Javascript_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = EParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2003 
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
            super(EParser.Javascript_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(EParser.New_tokenContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_method_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_new_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = EParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2005 
            self.new_token()
            self.state = 2006 
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
            super(EParser.Javascript_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_selector_expressionContext, self).copyFrom(ctx)



    class JavaScriptMemberExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavaScriptMemberExpressionContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptItemExpression(self)


    class JavaScriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavaScriptMethodExpressionContext, self).__init__(parser)
            self.method = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = EParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_javascript_selector_expression)
        try:
            self.state = 2013
            la_ = self._interp.adaptivePredict(self._input,164,self._ctx)
            if la_ == 1:
                localctx = EParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2008
                self.match(EParser.DOT)
                self.state = 2009 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = EParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2010
                self.match(EParser.DOT)
                self.state = 2011 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = EParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2012 
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
            super(EParser.Javascript_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext
            self.args = None # Javascript_argumentsContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def javascript_arguments(self):
            return self.getTypedRuleContext(EParser.Javascript_argumentsContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = EParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2015 
            localctx.name = self.javascript_identifier()
            self.state = 2016
            self.match(EParser.LPAR)
            self.state = 2018
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (EParser.READ - 131)) | (1 << (EParser.SELF - 131)) | (1 << (EParser.TEST - 131)) | (1 << (EParser.THIS - 131)) | (1 << (EParser.WRITE - 131)) | (1 << (EParser.BOOLEAN_LITERAL - 131)) | (1 << (EParser.CHAR_LITERAL - 131)) | (1 << (EParser.SYMBOL_IDENTIFIER - 131)) | (1 << (EParser.TYPE_IDENTIFIER - 131)) | (1 << (EParser.VARIABLE_IDENTIFIER - 131)) | (1 << (EParser.DOLLAR_IDENTIFIER - 131)) | (1 << (EParser.TEXT_LITERAL - 131)) | (1 << (EParser.INTEGER_LITERAL - 131)) | (1 << (EParser.DECIMAL_LITERAL - 131)))) != 0):
                self.state = 2017 
                localctx.args = self.javascript_arguments(0)


            self.state = 2020
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_argumentsContext, self).copyFrom(ctx)


    class JavascriptArgumentListContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_argumentsContext)
            super(EParser.JavascriptArgumentListContext, self).__init__(parser)
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptArgumentList(self)


    class JavascriptArgumentListItemContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_argumentsContext)
            super(EParser.JavascriptArgumentListItemContext, self).__init__(parser)
            self.items = None # Javascript_argumentsContext
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def javascript_arguments(self):
            return self.getTypedRuleContext(EParser.Javascript_argumentsContext,0)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 324
        self.enterRecursionRule(localctx, 324, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2023 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2030
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,166,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptArgumentListItemContext(self, EParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 2025
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2026
                    self.match(EParser.COMMA)
                    self.state = 2027 
                    localctx.item = self.javascript_expression(0) 
                self.state = 2032
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,166,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_item_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = EParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2033
            self.match(EParser.LBRAK)
            self.state = 2034 
            localctx.exp = self.javascript_expression(0)
            self.state = 2035
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = EParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2037
            self.match(EParser.LPAR)
            self.state = 2038 
            localctx.exp = self.javascript_expression(0)
            self.state = 2039
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext

        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_identifier_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = EParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2041 
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
            super(EParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



    class JavascriptIntegerLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = EParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_javascript_literal_expression)
        try:
            self.state = 2048
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2043
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2044
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2045
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2046
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2047
                localctx.t = self.match(EParser.CHAR_LITERAL)

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
            super(EParser.Javascript_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def getRuleIndex(self):
            return EParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = EParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2050
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (EParser.READ - 131)) | (1 << (EParser.TEST - 131)) | (1 << (EParser.WRITE - 131)) | (1 << (EParser.SYMBOL_IDENTIFIER - 131)) | (1 << (EParser.TYPE_IDENTIFIER - 131)) | (1 << (EParser.VARIABLE_IDENTIFIER - 131)) | (1 << (EParser.DOLLAR_IDENTIFIER - 131)))) != 0)):
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
            super(EParser.Python_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_statement

     
        def copyFrom(self, ctx):
            super(EParser.Python_statementContext, self).copyFrom(ctx)



    class PythonStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_statementContext)
            super(EParser.PythonStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonStatement(self)


    class PythonReturnStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_statementContext)
            super(EParser.PythonReturnStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = EParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_python_statement)
        try:
            self.state = 2055
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2052
                self.match(EParser.RETURN)
                self.state = 2053 
                localctx.exp = self.python_expression(0)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2054 
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
            super(EParser.Python_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_expressionContext, self).copyFrom(ctx)


    class PythonSelectorExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_expressionContext)
            super(EParser.PythonSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Python_expressionContext
            self.child = None # Python_selector_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)

        def python_selector_expression(self):
            return self.getTypedRuleContext(EParser.Python_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_expressionContext)
            super(EParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(EParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 338
        self.enterRecursionRule(localctx, 338, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2058 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2064
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,169,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonSelectorExpressionContext(self, EParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 2060
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2061 
                    localctx.child = self.python_selector_expression() 
                self.state = 2066
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,169,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_primary_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_primary_expressionContext, self).copyFrom(ctx)



    class PythonParenthesisExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Python_parenthesis_expressionContext
            self.copyFrom(ctx)

        def python_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Python_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonIdentifierExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(EParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(EParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = EParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_python_primary_expression)
        try:
            self.state = 2071
            la_ = self._interp.adaptivePredict(self._input,170,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2067 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2068 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2069 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = EParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2070 
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
            super(EParser.Python_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_selector_expressionContext, self).copyFrom(ctx)



    class PythonMethodExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_selector_expressionContext)
            super(EParser.PythonMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def python_method_expression(self):
            return self.getTypedRuleContext(EParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonMethodExpression(self)


    class PythonItemExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_selector_expressionContext)
            super(EParser.PythonItemExpressionContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = EParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_python_selector_expression)
        try:
            self.state = 2079
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2073
                self.match(EParser.DOT)
                self.state = 2074 
                localctx.exp = self.python_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2075
                self.match(EParser.LBRAK)
                self.state = 2076 
                localctx.exp = self.python_expression(0)
                self.state = 2077
                self.match(EParser.RBRAK)

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
            super(EParser.Python_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Python_identifierContext
            self.args = None # Python_argument_listContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)


        def python_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_argument_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = EParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2081 
            localctx.name = self.python_identifier()
            self.state = 2082
            self.match(EParser.LPAR)
            self.state = 2084
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (EParser.READ - 131)) | (1 << (EParser.SELF - 131)) | (1 << (EParser.TEST - 131)) | (1 << (EParser.THIS - 131)) | (1 << (EParser.WRITE - 131)) | (1 << (EParser.BOOLEAN_LITERAL - 131)) | (1 << (EParser.CHAR_LITERAL - 131)) | (1 << (EParser.SYMBOL_IDENTIFIER - 131)) | (1 << (EParser.TYPE_IDENTIFIER - 131)) | (1 << (EParser.VARIABLE_IDENTIFIER - 131)) | (1 << (EParser.DOLLAR_IDENTIFIER - 131)) | (1 << (EParser.TEXT_LITERAL - 131)) | (1 << (EParser.INTEGER_LITERAL - 131)) | (1 << (EParser.DECIMAL_LITERAL - 131)))) != 0):
                self.state = 2083 
                localctx.args = self.python_argument_list()


            self.state = 2086
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Python_argument_listContext, self).copyFrom(ctx)



    class PythonOrdinalOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_argument_listContext)
            super(EParser.PythonOrdinalOnlyArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.copyFrom(ctx)

        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_ordinal_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_argument_listContext)
            super(EParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonNamedOnlyArgumentList(self)


    class PythonArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_argument_listContext)
            super(EParser.PythonArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_ordinal_argument_listContext,0)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = EParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_python_argument_list)
        try:
            self.state = 2094
            la_ = self._interp.adaptivePredict(self._input,173,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2088 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2089 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2090 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2091
                self.match(EParser.COMMA)
                self.state = 2092 
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
            super(EParser.Python_ordinal_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_ordinal_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Python_ordinal_argument_listContext, self).copyFrom(ctx)


    class PythonOrdinalArgumentListContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_ordinal_argument_listContext)
            super(EParser.PythonOrdinalArgumentListContext, self).__init__(parser)
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonOrdinalArgumentList(self)


    class PythonOrdinalArgumentListItemContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_ordinal_argument_listContext)
            super(EParser.PythonOrdinalArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_ordinal_argument_listContext
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_ordinal_argument_listContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 348
        self.enterRecursionRule(localctx, 348, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2097 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,174,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonOrdinalArgumentListItemContext(self, EParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2099
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2100
                    self.match(EParser.COMMA)
                    self.state = 2101 
                    localctx.item = self.python_expression(0) 
                self.state = 2106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,174,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_named_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_named_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_named_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Python_named_argument_listContext, self).copyFrom(ctx)


    class PythonNamedArgumentListContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_named_argument_listContext)
            super(EParser.PythonNamedArgumentListContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(EParser.EQ, 0)
        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonNamedArgumentList(self)


    class PythonNamedArgumentListItemContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_named_argument_listContext)
            super(EParser.PythonNamedArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_named_argument_listContext
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def EQ(self):
            return self.getToken(EParser.EQ, 0)
        def python_named_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_named_argument_listContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2108 
            localctx.name = self.python_identifier()
            self.state = 2109
            self.match(EParser.EQ)
            self.state = 2110 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,175,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonNamedArgumentListItemContext(self, EParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2112
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2113
                    self.match(EParser.COMMA)
                    self.state = 2114 
                    localctx.name = self.python_identifier()
                    self.state = 2115
                    self.match(EParser.EQ)
                    self.state = 2116 
                    localctx.exp = self.python_expression(0) 
                self.state = 2122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,175,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Python_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = EParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2123
            self.match(EParser.LPAR)
            self.state = 2124 
            localctx.exp = self.python_expression(0)
            self.state = 2125
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_identifier_expressionContext, self).copyFrom(ctx)


    class PythonChildIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonChildIdentifierContext, self).__init__(parser)
            self.parent = None # Python_identifier_expressionContext
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def python_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Python_identifier_expressionContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 354
        self.enterRecursionRule(localctx, 354, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2130
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2128
                self.match(EParser.DOLLAR_IDENTIFIER)

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2129 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,177,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonChildIdentifierContext(self, EParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2132
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2133
                    self.match(EParser.DOT)
                    self.state = 2134 
                    localctx.name = self.python_identifier() 
                self.state = 2139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,177,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_literal_expressionContext, self).copyFrom(ctx)



    class PythonIntegerLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = EParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_python_literal_expression)
        try:
            self.state = 2145
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2140
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2141
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2142
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2143
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2144
                localctx.t = self.match(EParser.CHAR_LITERAL)

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
            super(EParser.Python_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def SELF(self):
            return self.getToken(EParser.SELF, 0)

        def THIS(self):
            return self.getToken(EParser.THIS, 0)

        def getRuleIndex(self):
            return EParser.RULE_python_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = EParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2147
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (EParser.READ - 131)) | (1 << (EParser.SELF - 131)) | (1 << (EParser.TEST - 131)) | (1 << (EParser.THIS - 131)) | (1 << (EParser.WRITE - 131)) | (1 << (EParser.SYMBOL_IDENTIFIER - 131)) | (1 << (EParser.TYPE_IDENTIFIER - 131)) | (1 << (EParser.VARIABLE_IDENTIFIER - 131)))) != 0)):
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
            super(EParser.Java_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_statement

     
        def copyFrom(self, ctx):
            super(EParser.Java_statementContext, self).copyFrom(ctx)



    class JavaReturnStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_statementContext)
            super(EParser.JavaReturnStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaReturnStatement(self)


    class JavaStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_statementContext)
            super(EParser.JavaStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = EParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_java_statement)
        try:
            self.state = 2156
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2149
                self.match(EParser.RETURN)
                self.state = 2150 
                localctx.exp = self.java_expression(0)
                self.state = 2151
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.NATIVE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2153 
                localctx.exp = self.java_expression(0)
                self.state = 2154
                self.match(EParser.SEMI)

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
            super(EParser.Java_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_expressionContext, self).copyFrom(ctx)


    class JavaSelectorExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_expressionContext)
            super(EParser.JavaSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Java_expressionContext
            self.child = None # Java_selector_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)

        def java_selector_expression(self):
            return self.getTypedRuleContext(EParser.Java_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_expressionContext)
            super(EParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(EParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 362
        self.enterRecursionRule(localctx, 362, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2159 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,180,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaSelectorExpressionContext(self, EParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2161
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2162 
                    localctx.child = self.java_selector_expression() 
                self.state = 2167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,180,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def java_this_expression(self):
            return self.getTypedRuleContext(EParser.Java_this_expressionContext,0)


        def java_new_expression(self):
            return self.getTypedRuleContext(EParser.Java_new_expressionContext,0)


        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Java_parenthesis_expressionContext,0)


        def java_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_identifier_expressionContext,0)


        def java_literal_expression(self):
            return self.getTypedRuleContext(EParser.Java_literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = EParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_java_primary_expression)
        try:
            self.state = 2173
            la_ = self._interp.adaptivePredict(self._input,181,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2168 
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2169 
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2170 
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2171 
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2172 
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
            super(EParser.Java_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = EParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2175 
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
            super(EParser.Java_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(EParser.New_tokenContext,0)


        def java_method_expression(self):
            return self.getTypedRuleContext(EParser.Java_method_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_new_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = EParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2177 
            self.new_token()
            self.state = 2178 
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
            super(EParser.Java_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_selector_expressionContext, self).copyFrom(ctx)



    class JavaItemExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_selector_expressionContext)
            super(EParser.JavaItemExpressionContext, self).__init__(parser)
            self.exp = None # Java_item_expressionContext
            self.copyFrom(ctx)

        def java_item_expression(self):
            return self.getTypedRuleContext(EParser.Java_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaItemExpression(self)


    class JavaMethodExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_selector_expressionContext)
            super(EParser.JavaMethodExpressionContext, self).__init__(parser)
            self.exp = None # Java_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def java_method_expression(self):
            return self.getTypedRuleContext(EParser.Java_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = EParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_java_selector_expression)
        try:
            self.state = 2183
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2180
                self.match(EParser.DOT)
                self.state = 2181 
                localctx.exp = self.java_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2182 
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
            super(EParser.Java_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Java_identifierContext
            self.args = None # Java_argumentsContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def java_identifier(self):
            return self.getTypedRuleContext(EParser.Java_identifierContext,0)


        def java_arguments(self):
            return self.getTypedRuleContext(EParser.Java_argumentsContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = EParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2185 
            localctx.name = self.java_identifier()
            self.state = 2186
            self.match(EParser.LPAR)
            self.state = 2188
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (EParser.READ - 131)) | (1 << (EParser.SELF - 131)) | (1 << (EParser.TEST - 131)) | (1 << (EParser.THIS - 131)) | (1 << (EParser.WRITE - 131)) | (1 << (EParser.BOOLEAN_LITERAL - 131)) | (1 << (EParser.CHAR_LITERAL - 131)) | (1 << (EParser.SYMBOL_IDENTIFIER - 131)) | (1 << (EParser.TYPE_IDENTIFIER - 131)) | (1 << (EParser.VARIABLE_IDENTIFIER - 131)) | (1 << (EParser.NATIVE_IDENTIFIER - 131)) | (1 << (EParser.DOLLAR_IDENTIFIER - 131)) | (1 << (EParser.TEXT_LITERAL - 131)) | (1 << (EParser.INTEGER_LITERAL - 131)) | (1 << (EParser.DECIMAL_LITERAL - 131)))) != 0):
                self.state = 2187 
                localctx.args = self.java_arguments(0)


            self.state = 2190
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Java_argumentsContext, self).copyFrom(ctx)


    class JavaArgumentListItemContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_argumentsContext)
            super(EParser.JavaArgumentListItemContext, self).__init__(parser)
            self.items = None # Java_argumentsContext
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def java_arguments(self):
            return self.getTypedRuleContext(EParser.Java_argumentsContext,0)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_argumentsContext)
            super(EParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 374
        self.enterRecursionRule(localctx, 374, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2193 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,184,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaArgumentListItemContext(self, EParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2195
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2196
                    self.match(EParser.COMMA)
                    self.state = 2197 
                    localctx.item = self.java_expression(0) 
                self.state = 2202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,184,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_item_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = EParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2203
            self.match(EParser.LBRAK)
            self.state = 2204 
            localctx.exp = self.java_expression(0)
            self.state = 2205
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = EParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2207
            self.match(EParser.LPAR)
            self.state = 2208 
            localctx.exp = self.java_expression(0)
            self.state = 2209
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_identifier_expressionContext, self).copyFrom(ctx)


    class JavaIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_identifier_expressionContext)
            super(EParser.JavaIdentifierContext, self).__init__(parser)
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def java_identifier(self):
            return self.getTypedRuleContext(EParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaIdentifier(self)


    class JavaChildIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_identifier_expressionContext)
            super(EParser.JavaChildIdentifierContext, self).__init__(parser)
            self.parent = None # Java_identifier_expressionContext
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def java_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_identifier_expressionContext,0)

        def java_identifier(self):
            return self.getTypedRuleContext(EParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 380
        self.enterRecursionRule(localctx, 380, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2212 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,185,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildIdentifierContext(self, EParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2214
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2215
                    self.match(EParser.DOT)
                    self.state = 2216 
                    localctx.name = self.java_identifier() 
                self.state = 2221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,185,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_class_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_class_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_class_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_class_identifier_expressionContext, self).copyFrom(ctx)


    class JavaClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_class_identifier_expressionContext)
            super(EParser.JavaClassIdentifierContext, self).__init__(parser)
            self.klass = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaClassIdentifier(self)


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_class_identifier_expressionContext)
            super(EParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_class_identifier_expressionContext,0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 382
        self.enterRecursionRule(localctx, 382, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2223 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,186,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildClassIdentifierContext(self, EParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2225
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2226
                    localctx.name = self.match(EParser.DOLLAR_IDENTIFIER) 
                self.state = 2231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,186,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_literal_expressionContext, self).copyFrom(ctx)



    class JavaBooleanLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = EParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_java_literal_expression)
        try:
            self.state = 2237
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2232
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2233
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2234
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2235
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2236
                localctx.t = self.match(EParser.CHAR_LITERAL)

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
            super(EParser.Java_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def NATIVE_IDENTIFIER(self):
            return self.getToken(EParser.NATIVE_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def getRuleIndex(self):
            return EParser.RULE_java_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = EParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2239
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (EParser.READ - 131)) | (1 << (EParser.TEST - 131)) | (1 << (EParser.WRITE - 131)) | (1 << (EParser.SYMBOL_IDENTIFIER - 131)) | (1 << (EParser.TYPE_IDENTIFIER - 131)) | (1 << (EParser.VARIABLE_IDENTIFIER - 131)) | (1 << (EParser.NATIVE_IDENTIFIER - 131)) | (1 << (EParser.DOLLAR_IDENTIFIER - 131)))) != 0)):
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
            super(EParser.Csharp_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_statement

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_statementContext, self).copyFrom(ctx)



    class CSharpReturnStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_statementContext)
            super(EParser.CSharpReturnStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpReturnStatement(self)


    class CSharpStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_statementContext)
            super(EParser.CSharpStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = EParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_csharp_statement)
        try:
            self.state = 2248
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2241
                self.match(EParser.RETURN)
                self.state = 2242 
                localctx.exp = self.csharp_expression(0)
                self.state = 2243
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2245 
                localctx.exp = self.csharp_expression(0)
                self.state = 2246
                self.match(EParser.SEMI)

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
            super(EParser.Csharp_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_expressionContext, self).copyFrom(ctx)


    class CSharpSelectorExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_expressionContext)
            super(EParser.CSharpSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Csharp_expressionContext
            self.child = None # Csharp_selector_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)

        def csharp_selector_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_expressionContext)
            super(EParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 390
        self.enterRecursionRule(localctx, 390, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2251 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,189,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpSelectorExpressionContext(self, EParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2253
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2254 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,189,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def csharp_this_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_this_expressionContext,0)


        def csharp_new_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_new_expressionContext,0)


        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_parenthesis_expressionContext,0)


        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)


        def csharp_literal_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = EParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_csharp_primary_expression)
        try:
            self.state = 2265
            la_ = self._interp.adaptivePredict(self._input,190,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2260 
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2261 
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2262 
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2263 
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2264 
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
            super(EParser.Csharp_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = EParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2267 
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
            super(EParser.Csharp_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(EParser.New_tokenContext,0)


        def csharp_method_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_method_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_new_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = EParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2269 
            self.new_token()
            self.state = 2270 
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
            super(EParser.Csharp_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_selector_expressionContext, self).copyFrom(ctx)



    class CSharpMethodExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_selector_expressionContext)
            super(EParser.CSharpMethodExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def csharp_method_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_selector_expressionContext)
            super(EParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = EParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_csharp_selector_expression)
        try:
            self.state = 2275
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2272
                self.match(EParser.DOT)
                self.state = 2273 
                localctx.exp = self.csharp_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2274 
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
            super(EParser.Csharp_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Csharp_identifierContext
            self.args = None # Csharp_argumentsContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(EParser.Csharp_identifierContext,0)


        def csharp_arguments(self):
            return self.getTypedRuleContext(EParser.Csharp_argumentsContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = EParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2277 
            localctx.name = self.csharp_identifier()
            self.state = 2278
            self.match(EParser.LPAR)
            self.state = 2280
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (EParser.READ - 131)) | (1 << (EParser.SELF - 131)) | (1 << (EParser.TEST - 131)) | (1 << (EParser.THIS - 131)) | (1 << (EParser.WRITE - 131)) | (1 << (EParser.BOOLEAN_LITERAL - 131)) | (1 << (EParser.CHAR_LITERAL - 131)) | (1 << (EParser.SYMBOL_IDENTIFIER - 131)) | (1 << (EParser.TYPE_IDENTIFIER - 131)) | (1 << (EParser.VARIABLE_IDENTIFIER - 131)) | (1 << (EParser.DOLLAR_IDENTIFIER - 131)) | (1 << (EParser.TEXT_LITERAL - 131)) | (1 << (EParser.INTEGER_LITERAL - 131)) | (1 << (EParser.DECIMAL_LITERAL - 131)))) != 0):
                self.state = 2279 
                localctx.args = self.csharp_arguments(0)


            self.state = 2282
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_argumentsContext, self).copyFrom(ctx)


    class CSharpArgumentListContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_argumentsContext)
            super(EParser.CSharpArgumentListContext, self).__init__(parser)
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpArgumentList(self)


    class CSharpArgumentListItemContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_argumentsContext)
            super(EParser.CSharpArgumentListItemContext, self).__init__(parser)
            self.items = None # Csharp_argumentsContext
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def csharp_arguments(self):
            return self.getTypedRuleContext(EParser.Csharp_argumentsContext,0)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 402
        self.enterRecursionRule(localctx, 402, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2285 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,193,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpArgumentListItemContext(self, EParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2287
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2288
                    self.match(EParser.COMMA)
                    self.state = 2289 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2294
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,193,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_item_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = EParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2295
            self.match(EParser.LBRAK)
            self.state = 2296 
            localctx.exp = self.csharp_expression(0)
            self.state = 2297
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = EParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2299
            self.match(EParser.LPAR)
            self.state = 2300 
            localctx.exp = self.csharp_expression(0)
            self.state = 2301
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_identifier_expressionContext, self).copyFrom(ctx)


    class CSharpIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpIdentifierContext, self).__init__(parser)
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def csharp_identifier(self):
            return self.getTypedRuleContext(EParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpIdentifier(self)


    class CSharpChildIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpChildIdentifierContext, self).__init__(parser)
            self.parent = None # Csharp_identifier_expressionContext
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(EParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 408
        self.enterRecursionRule(localctx, 408, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2306
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2304
                self.match(EParser.DOLLAR_IDENTIFIER)

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.TEST, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2305 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,195,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpChildIdentifierContext(self, EParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2308
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2309
                    self.match(EParser.DOT)
                    self.state = 2310 
                    localctx.name = self.csharp_identifier() 
                self.state = 2315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,195,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_literal_expressionContext, self).copyFrom(ctx)



    class CSharpBooleanLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpBooleanLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = EParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_csharp_literal_expression)
        try:
            self.state = 2321
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2316
                self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2317
                self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2318
                self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2319
                self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2320
                self.match(EParser.CHAR_LITERAL)

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
            super(EParser.Csharp_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def getRuleIndex(self):
            return EParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = EParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2323
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (EParser.READ - 131)) | (1 << (EParser.TEST - 131)) | (1 << (EParser.WRITE - 131)) | (1 << (EParser.SYMBOL_IDENTIFIER - 131)) | (1 << (EParser.TYPE_IDENTIFIER - 131)) | (1 << (EParser.VARIABLE_IDENTIFIER - 131)))) != 0)):
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
        self._predicates[16] = self.native_category_binding_list_sempred
        self._predicates[37] = self.else_if_statement_list_sempred
        self._predicates[43] = self.expression_sempred
        self._predicates[44] = self.unresolved_expression_sempred
        self._predicates[45] = self.unresolved_selector_sempred
        self._predicates[47] = self.invocation_trailer_sempred
        self._predicates[48] = self.instance_expression_sempred
        self._predicates[49] = self.instance_selector_sempred
        self._predicates[59] = self.argument_assignment_list_sempred
        self._predicates[60] = self.with_argument_assignment_list_sempred
        self._predicates[63] = self.child_instance_sempred
        self._predicates[83] = self.typedef_sempred
        self._predicates[103] = self.any_type_sempred
        self._predicates[140] = self.assignable_instance_sempred
        self._predicates[141] = self.is_expression_sempred
        self._predicates[145] = self.new_token_sempred
        self._predicates[146] = self.key_token_sempred
        self._predicates[147] = self.module_token_sempred
        self._predicates[148] = self.value_token_sempred
        self._predicates[149] = self.symbols_token_sempred
        self._predicates[156] = self.javascript_expression_sempred
        self._predicates[162] = self.javascript_arguments_sempred
        self._predicates[169] = self.python_expression_sempred
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

    def native_category_binding_list_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def else_if_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 39)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 38)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 37)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 36)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 35)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 33)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 22)
         

    def unresolved_expression_sempred(self, localctx, predIndex):
            if predIndex == 29:
                return self.precpred(self._ctx, 1)
         

    def unresolved_selector_sempred(self, localctx, predIndex):
            if predIndex == 30:
                return self.wasNot(EParser.WS)
         

    def invocation_trailer_sempred(self, localctx, predIndex):
            if predIndex == 31:
                return self.willBe(EParser.LF)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 32:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 33:
                return self.wasNot(EParser.WS)
         

            if predIndex == 34:
                return self.wasNot(EParser.WS)
         

            if predIndex == 35:
                return self.wasNot(EParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.was(EParser.WS)
         

    def with_argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 38:
                return self.wasNot(EParser.WS)
         

            if predIndex == 39:
                return self.wasNot(EParser.WS)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 41:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 42:
                return self.precpred(self._ctx, 3)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 43:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 44:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 45:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.isText(localctx.i1,"key")
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.isText(localctx.i1,"module")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.precpred(self._ctx, 1)
         



