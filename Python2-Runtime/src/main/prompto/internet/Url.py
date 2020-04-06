from prompto.intrinsic.Binary import Binary
from prompto.value.IResource import IResource
import urllib2

class Url(IResource):

    def __init__(self):
        self.path = None
        self.reader = None


    def isReadable(self):
        return True


    def isWritable(self):
        return True


    def close(self):
        if self.reader is not None:
            self.reader.close()


    def readBinary(self):
        with urllib2.urlopen(self.path) as response:
            data = response.read()
            mimeType = response.info().gettype()
            if mimeType.index(";") > 0:
                mimeType = mimeType[0, mimeType.index(";")]
            return Binary(mimeType, data)


    def readFully(self):
        response = urllib2.urlopen(self.path)
        try:
            return str(response.read())
        finally:
            response.close()


    def readLine(self):
        if self.reader is None:
            self.reader = urllib2.urlopen(self.path)
        return str(self.reader.readLine())


    def writeFully(self, data):
        pass


    def writeLine(self, data):
        pass
