from io import StringIO


class DictEntryList ( list ):

    def __init__(self, entry = None):
        super(DictEntryList, self).__init__()
        if entry is not None:
            self.append(entry)

    def __str__(self):
        with StringIO() as sb:
            sb.write(u'<')
            for item in self:
                sb.write(unicode(item))
                sb.write(u", ")
            slen = sb.tell()
            if slen>2:
                sb.truncate(slen-2)
                sb.seek(slen-2)
            else:
                sb.write(u':')
            sb.write(u'>')
            return sb.getvalue()

    def toDialect(self, writer):
        writer.append('<')
        if len(self)>0:
            for entry in self:
                entry.toDialect(writer)
                writer.append(", ")
            writer.trimLast(2)
        else:
            writer.append(':')
        writer.append('>')
