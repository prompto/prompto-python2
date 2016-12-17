from io import StringIO

from prompto.utils.ObjectList import ObjectList


class SymbolList (ObjectList):

    def __init__(self, symbol = None):
        super(SymbolList, self).__init__()
        if symbol is not None:
            self.append(symbol)

    def __str__(self):
        with StringIO() as sb:
            sb.write(u"[")
            for item in self:
                sb.write(item.getName())
                sb.write(u", ")
            slen = sb.tell()
            sb.truncate(slen - 2)
            sb.seek(slen - 2)
            sb.write(u"]")
            return sb.getvalue()
