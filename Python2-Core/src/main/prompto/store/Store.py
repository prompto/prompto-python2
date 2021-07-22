class IStorable(object):
    pass


class IStored(object):
    pass


class IStore(object):

    def isDbIdType(self, typ):
        raise Exception("isDbIdType must be implemented by Store instance!")

    def getDbIdType(self):
        raise Exception("getDbIdType must be implemented by Store instance!")

    def newStorableDocument(self, categories, dbIdFactory):
        raise Exception("newStorable must be implemented by Store instance!")

    def newAuditMetadata(self):
        raise Exception("newAuditMetadata must be implemented by Store instance!")

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

    def fetchLatestAuditMetadataId(self, dbId):
        raise Exception("fetchLatestAuditMetadataId must be implemented by Store instance!")

    def fetchAllAuditMetadataIds(self, dbId):
        raise Exception("fetchAllAuditMetadataIds must be implemented by Store instance!")

    def fetchAuditMetadata(self, dbId):
        raise Exception("fetchAuditMetadata must be implemented by Store instance!")

    def fetchAuditMetadataAsDocument (self, dbId):
        return self.fetchAuditMetadata(dbId)


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

    def addOrderByClause(self, info, descending):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def build(self):
        raise Exception("Must be implemented by QueryBuilder instance!")
