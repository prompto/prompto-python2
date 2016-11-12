from prompto.error.PromptoError import PromptoError

class SyntaxError (PromptoError):

    def __init__(self, message):
        super(SyntaxError, self).__init__(message)
