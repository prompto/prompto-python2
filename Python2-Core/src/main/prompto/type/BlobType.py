from prompto.type.BinaryType import BinaryType
from prompto.type.TypeFamily import TypeFamily



class BlobType(BinaryType):

    instance = None

    def __init__(self):
        super(BlobType, self).__init__(TypeFamily.BLOB)

BlobType.instance = BlobType()