class TypeFamily(object):
    
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
TypeFamily.ANY = TypeFamily("ANY")
TypeFamily.METHOD = TypeFamily("METHOD")
TypeFamily.CURSOR = TypeFamily("CURSOR")
TypeFamily.ITERATOR = TypeFamily("ITERATOR")
TypeFamily.CLASS = TypeFamily("CLASS")
TypeFamily.TYPE = TypeFamily("TYPE")
TypeFamily.CODE = TypeFamily("CODE")
# volatile
TypeFamily.MISSING = TypeFamily("MISSING")
