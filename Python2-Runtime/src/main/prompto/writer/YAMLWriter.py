import yaml
from StringIO import StringIO

from prompto.error.ReadWriteError import ReadWriteError

def yamlWrite(docs):
    stream = StringIO()
    try:
        yaml.safe_dump_all(docs, stream)
        return unicode(stream.getvalue())
    except Exception as e:
        raise ReadWriteError(e.message)


