from presto.error.PrestoError import PrestoError


class ExecutionError(PrestoError):

    def __init__(self, message=None):
        super(ExecutionError, self).__init__(message)
