from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily


class JsxType(NativeType):

	def __init__(self):
		super(JsxType, self).__init__(TypeFamily.JSX)

JsxType.instance = JsxType()