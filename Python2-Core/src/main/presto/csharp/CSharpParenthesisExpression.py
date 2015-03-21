from presto.csharp.CSharpExpression import CSharpExpression


class CSharpParenthesisExpression ( CSharpExpression ):

	def __init__(self, expression):
		super(CSharpParenthesisExpression, self).__init__()
		self.expression = expression;
