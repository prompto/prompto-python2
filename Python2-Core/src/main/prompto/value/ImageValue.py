from prompto.type.ImageType import ImageType
from prompto.value.BinaryValue import BinaryValue


class ImageValue(BinaryValue):

    def __init__(self, mimeType, data):
        super(ImageValue, self).__init__(ImageType.instance, mimeType, data)

