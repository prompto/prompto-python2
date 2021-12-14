class IStorable(object):
    pass


class IStored(object):
    pass


class IAuditRecord(object):
    pass


class IAuditMetadata(object):
    pass


class AuditOperation(object):
    INSERT = "INSERT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class IStore(object):

    def isDbIdType(self, typ):
        raise Exception("isDbIdType must be implemented by Store instance!")

    def getDbIdType(self):
        raise Exception("getDbIdType must be implemented by Store instance!")

    def newStorableDocument(self, categories, dbIdFactory):
        raise Exception("newStorableDocument must be implemented by Store instance!")

    def deleteAndStore (self, dbIdsToDel, docsToStore, withMeta):
        raise Exception("deleteAndStore must be implemented by Store instance!")

    def flush (self):
        raise Exception("flush must be implemented by Store instance!")

    def newQueryBuilder(self):
        raise Exception("newQueryBuilder must be implemented by Store instance!")

    def fetchOne (self, query):
        raise Exception("fetchOne must be implemented by Store instance!")

    def fetchUnique (self, dbId):
        raise Exception("fetchUnique must be implemented by Store instance!")

    def fetchMany(self, query):
        raise Exception("fetchMany must be implemented by Store instance!")

    def nextSequenceValue(self, name):
        raise Exception("nextSequenceValue must be implemented by Store instance!")

    def isAuditEnabled(self):
        raise Exception("isAuditEnabled must be implemented by Store instance!")

    def newAuditMetadata(self):
        raise Exception("newAuditMetadata must be implemented by Store instance!")

    def fetchLatestAuditMetadataId(self, dbId):
        raise Exception("fetchLatestAuditMetadataId must be implemented by Store instance!")

    def fetchAllAuditMetadataIds(self, dbId):
        raise Exception("fetchAllAuditMetadataIds must be implemented by Store instance!")

    def fetchAuditMetadata(self, dbId):
        raise Exception("fetchAuditMetadata must be implemented by Store instance!")

    def fetchAuditMetadataAsDocument (self, dbId):
        raise Exception("fetchAuditMetadataAsDocument must be implemented by Store instance!")

    def fetchLatestAuditRecord (self, dbId):
        raise Exception("fetchLatestAuditRecord must be implemented by Store instance!")

    def fetchLatestAuditRecordAsDocument(self, dbId):
        raise Exception("fetchLatestAuditRecord must be implemented by Store instance!")

    def fetchAuditRecordsMatching(self, auditPredicates, instancePredicates):
        raise Exception("fetchAuditRecordsMatching must be implemented by Store instance!")

    def fetchAuditRecordsMatchingAsDocuments(self, auditPredicates, instancePredicates):
        raise Exception("fetchAuditRecordsMatchingAsDocuments must be implemented by Store instance!")

    def deleteAuditRecord (self, dbId):
        raise Exception("deleteAuditRecord must be implemented by Store instance!")

    def deleteAuditMetadata (self, dbId):
        raise Exception("deleteAuditMetadata must be implemented by Store instance!")

class IQueryBuilder(object):

    def setFirst(self, first):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def setLast(self, first):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def verify(self, info, match, value):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def And(self):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def Or(self):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def Not(self):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def project(self, projection):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def addOrderByClause(self, info, descending):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def build(self):
        raise Exception("Must be implemented by QueryBuilder instance!")
