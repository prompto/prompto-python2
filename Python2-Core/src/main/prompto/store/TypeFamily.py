class TypeFamily(object):

    BOOLEAN = None
    CHARACTER = None
    INTEGER = None
    DECIMAL = None
    TEXT = None
    UUID = None
    DATE = None
    TIME = None
    DATETIME = None
    PERIOD = None
    VERSION = None
    LIST = None
    SET = None
    TUPLE = None
    RANGE = None
    BLOB = None
    IMAGE = None
    DOCUMENT = None
    CATEGORY = None
    RESOURCE = None
    DICTIONARY = None
    ENUMERATED = None
    # non storable
    VOID = None
    NULL = None
    DBID = None
    ANY = None
    METHOD = None
    CURSOR = None
    ITERATOR = None
    CLASS = None
    TYPE = None
    CODE = None
    JSX = None
    CSS = None
    HTML = None
    # volatile
    MISSING = None

    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    
# storable
TypeFamily.BOOLEAN = TypeFamily("BOOLEAN")
TypeFamily.CHARACTER = TypeFamily("CHARACTER")
TypeFamily.INTEGER = TypeFamily("INTEGER")
TypeFamily.DECIMAL = TypeFamily("DECIMAL")
TypeFamily.TEXT = TypeFamily("TEXT")
TypeFamily.UUID = TypeFamily("UUID")
TypeFamily.DATE = TypeFamily("DATE")
TypeFamily.TIME = TypeFamily("TIME")
TypeFamily.DATETIME = TypeFamily("DATETIME")
TypeFamily.PERIOD = TypeFamily("PERIOD")
TypeFamily.VERSION = TypeFamily("VERSION")
TypeFamily.LIST = TypeFamily("LIST")
TypeFamily.SET = TypeFamily("SET")
TypeFamily.TUPLE = TypeFamily("TUPLE")
TypeFamily.RANGE = TypeFamily("RANGE")
TypeFamily.BLOB = TypeFamily("BLOB")
TypeFamily.IMAGE = TypeFamily("IMAGE")
TypeFamily.DOCUMENT = TypeFamily("DOCUMENT")
TypeFamily.CATEGORY = TypeFamily("CATEGORY")
TypeFamily.RESOURCE = TypeFamily("RESOURCE")
TypeFamily.DICTIONARY = TypeFamily("DICTIONARY")
TypeFamily.ENUMERATED = TypeFamily("ENUMERATED")

# non storable
TypeFamily.VOID = TypeFamily("VOID")
TypeFamily.NULL = TypeFamily("NULL")
TypeFamily.DBID = TypeFamily("DBID")
TypeFamily.ANY = TypeFamily("ANY")
TypeFamily.METHOD = TypeFamily("METHOD")
TypeFamily.CURSOR = TypeFamily("CURSOR")
TypeFamily.ITERATOR = TypeFamily("ITERATOR")
TypeFamily.CLASS = TypeFamily("CLASS")
TypeFamily.TYPE = TypeFamily("TYPE")
TypeFamily.CODE = TypeFamily("CODE")
TypeFamily.JSX = TypeFamily("JSX")
TypeFamily.CSS = TypeFamily("CSS")
TypeFamily.HTML = TypeFamily("HTML")
TypeFamily.PROPERTIES = TypeFamily("PROPERTIES")

# volatile
TypeFamily.MISSING = TypeFamily("MISSING")
