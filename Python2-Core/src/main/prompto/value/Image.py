from prompto.type.ImageType import ImageType
from prompto.value.BinaryValue import BinaryValue


class Image(BinaryValue):

    def __init__(self, mimeType, data):
        super(Image, self).__init__(ImageType.instance, mimeType, data)

