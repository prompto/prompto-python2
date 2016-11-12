class PromptoError (Exception):

    def __init__(self, message = None, exception = None):
        super(PromptoError, self).__init__(message, exception)
        self.message = message
        self.exception = exception
