from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily


class CssType(NativeType):

	def __init__(self):
		super(CssType, self).__init__(TypeFamily.CSS)


	def checkAdd(self, context, other, tryReverse):
		if other is self:
			return self
		else:
			super(CssType, self).checkAdd(context, other, tryReverse)


CssType.instance = CssType()