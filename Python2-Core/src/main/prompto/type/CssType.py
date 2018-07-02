from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily


class CssType(NativeType):

	def __init__(self):
		super(CssType, self).__init__(TypeFamily.CSS)

CssType.instance = CssType()