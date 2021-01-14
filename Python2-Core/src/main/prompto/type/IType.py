from prompto.error.SyntaxError import SyntaxError

class IType(object):

	def __init__(self, typeName):
		self.typeName = typeName

	def anyfy(self):
		return self

	def resolve(self, context, onError = None):
		return self

	def isMutable(self, context):
		return False

	def asMutable(self, context, mutable):
		if mutable:
			raise SyntaxError("Cannot mutate " + self.typeName)
		else:
			return self