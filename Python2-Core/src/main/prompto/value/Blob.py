from prompto.type.BlobType import BlobType
from prompto.value.BinaryValue import BinaryValue


class Blob(BinaryValue):

    def __init__(self, mimeType, data):
        super(Blob, self).__init__(BlobType.instance, mimeType, data)

