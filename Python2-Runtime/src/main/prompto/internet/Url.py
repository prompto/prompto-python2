from prompto.value.IResource import IResource
import urllib2

class Url(IResource):

    def __init__(self):
        self.path = None

    def isReadable(self):
        return True

    def isWritable(self):
        return True

    def close(self):
        pass

    def readFully(self):
        response = urllib2.urlopen(self.path)
        return str(response.read())

    def writeFully(self, data):
        pass
