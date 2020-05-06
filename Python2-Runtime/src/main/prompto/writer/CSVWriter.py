import csv
from io import StringIO

class csvDialect(csv.Dialect):
    delimiter = ','
    quotechar = '"'
    escapechar = '\\'
    doublequote = True
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL


def patch(file):
    saved_write = file.write
    def patched_write(data):
        saved_write(unicode(data))
    file.write = patched_write
    return file


def csvWrite(docs, columns, mappings, delimiter, encloser):
    dialect = csvDialect()
    dialect.delimiter = delimiter
    dialect.quotechar = encloser
    with patch(StringIO()) as file:
        writer = csv.DictWriter(file, fieldnames=columns, dialect=dialect)
        if mappings is None:
            writer.writeheader()
        else:
            zipped = zip( columns, [ mappings.get(column, column) for column in columns] )
            headers = dict(zipped)
            writer.writerow(headers)
        writer.writerows(docs)
        file.flush()
        return file.getvalue()
