class PrestoError ( Exception ):

    def __init__(self, message = None, exception = None):
        super(PrestoError, self).__init__(message, exception)
        self.message = message
        self.exception = exception
