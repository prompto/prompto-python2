from prompto.error.InternalError import InternalError
from prompto.error.InvalidResourceError import InvalidResourceError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.expression.IExpression import IExpression
from prompto.type.BlobType import BlobType
from prompto.type.ResourceType import ResourceType
from prompto.value.BlobValue import BlobValue
from prompto.value.IResource import IResource
from prompto.error.SyntaxError import SyntaxError

class ReadBlobExpression (IExpression) :

    def __init__(self, resource):
        super(ReadBlobExpression, self).__init__()
        self.resource = resource


    def __str__(self):
        return "read Blob from " + str(self.resource)



    def check(self, context):
        context = context.newResourceContext()
        sourceType = self.resource.check(context)
        if not isinstance(sourceType, ResourceType):
            raise SyntaxError("Not a readable resource!")
        return BlobType.instance



    def interpret(self, context):
        context = context.newResourceContext()
        o = self.resource.interpret(context)
        if o is None:
            raise NullReferenceError()
        if not isinstance(o, IResource):
            raise InternalError("Illegal read source: " + o)
        if not o.isReadable():
            raise InvalidResourceError("Not readable")
        try:
            return BlobValue(o.readBinary())
        finally:
            o.close()



    def toDialect(self, writer):
        writer.append("read Blob from ")
        self.resource.toDialect(writer)
