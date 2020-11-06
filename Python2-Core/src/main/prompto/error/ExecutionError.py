from prompto.error.PromptoError import PromptoError


class ExecutionError(PromptoError):

    def __init__(self, message=None, exception=None):
        super(ExecutionError, self).__init__(message, exception)

    def interpret(self, context, errorName):
        exp = self.getExpression(context)
        if exp is None:
            from prompto.grammar.Argument import Argument
            from prompto.grammar.ArgumentList import ArgumentList
            from prompto.expression.ConstructorExpression import ConstructorExpression
            from prompto.param.UnresolvedParameter import UnresolvedParameter
            from prompto.literal.TextLiteral import TextLiteral
            from prompto.type.CategoryType import CategoryType
            args = ArgumentList()
            args.append(Argument(UnresolvedParameter("name"), TextLiteral(type(self).__name__)))
            args.append(Argument(UnresolvedParameter("text"), TextLiteral(self.message)))
            exp = ConstructorExpression(CategoryType("Error"), args, None)
        if context.getRegisteredValue(object, errorName) is None:
            from prompto.runtime.ErrorVariable import ErrorVariable
            context.registerValue(ErrorVariable(errorName))
        error = exp.interpret(context)
        context.setValue(errorName, error)
        return error

    def getExpression(self, context):
        return None