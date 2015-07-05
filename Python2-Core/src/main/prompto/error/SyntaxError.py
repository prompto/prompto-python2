from prompto.error.PrestoError import PrestoError

class SyntaxError ( PrestoError ):

    def __init__(self, message):
        super(SyntaxError, self).__init__(message)
