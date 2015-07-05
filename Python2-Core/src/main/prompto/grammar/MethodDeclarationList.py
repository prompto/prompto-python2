class MethodDeclarationList (list):

	def __init__(self, method = None):
		super(MethodDeclarationList, self).__init__()
		if method is not None:
			self.append(method)
