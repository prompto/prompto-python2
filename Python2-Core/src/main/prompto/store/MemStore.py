from prompto.declaration.AttributeInfo import AttributeInfo
from prompto.error.InvalidDataError import InvalidDataError
from prompto.store.MatchOp import MatchOp
from prompto.store.Query import Query
from prompto.store.Store import IStorable, IStored
from prompto.type.TypeFamily import TypeFamily

# a utility class for running unit tests only
class MemStore(object):

    lastDbId = 0

    @staticmethod
    def nextDbId():
        MemStore.lastDbId += 1
        return MemStore.lastDbId

    def __init__(self):
        self.documents = dict()


    def isDbIdType(self, typ):
        return typ in [int, long]


    def getDbIdType(self):
        return long


    def flush (self):
        pass # nothing to do


    def store (self, dbIdsToDel, docsToStore):
        if dbIdsToDel is not None:
            for dbId in dbIdsToDel:
                del self.documents[dbId]
        if docsToStore is not None:
            for doc in docsToStore:
                self.documents[doc.getData("dbId")] = doc

    def newStorable(self, categories):
        return StorableDocument(categories)


    def interpretFetchOne(self, context, typ, predicate):
        interpreter = QueryInterpreter(context)
        query = interpreter.buildFetchOneQuery(typ, predicate)
        return self.fetchOne(query)


    def fetchOne (self, query):
        predicate = query.predicate()
        for doc in self.documents.values():
            if doc.matches(predicate):
                return doc
        return None


    def fetchUnique (self, dbId):
        return self.documents.get(dbId, None)


    def interpretFetchMany(self, context, typ, start, end, predicate, orderBy):
        interpreter = QueryInterpreter(context)
        query = interpreter.buildFetchManyQuery(typ, start, end, predicate, orderBy)
        return self.fetchMany(query)


    def fetchMany(self, query):
        # iter all docs
        docs = self.documents.values()
        # filter with predicate
        if query.predicate() is not None:
            docs = self.filterDocs(docs, query.predicate())
        # sort if required
        if query.orderBys is not None:
            docs = self.sortDocs(docs, query.orderBys)
        # slice it if required
        if query.start is not None or query.end is not None:
            docs = self.sliceDocs(docs, query.start, query.end)
        # done
        return DocumentIterator(docs)


    def filterDocs(self, docs, predicate):
        res = []
        for doc in docs:
            if doc.matches(predicate):
                res.append(doc)
        return res


    def sortDocs(self, docs, orderBys):
        # need a closure builder on a per clause basis
        def valueExtractor(clause):
            # build the closure to be returned
            def extractValue(doc):
                source = doc
                value = None
                for name in clause.names:
                    value = source.getData(name)
                    source = value
                return value
            return extractValue
        # sorts are guaranteed to be stable, so go through clauses in reverse order
        for clause in reversed(orderBys):
            docs = sorted(docs, key=valueExtractor(clause), reverse = clause.descending)
        return docs

    def sliceDocs(self, docs, start, end):
        if start is None or start < 1:
            start = 1
        if end is None:
            end = len(docs)
        return docs[start-1:end]



class DocumentIterator(object):

    def __init__(self, docs):
        self.docs = docs

    def __len__(self):
        return len(self.docs)

    def __iter__(self):
        for doc in self.docs:
            yield doc


class StorableDocument(IStorable, IStored):

    def __init__(self, categories):
        self.document = None
        self.categories = categories

    def __getattribute__(self, key):
        if key=="dirty":
            return self.document is not None
        else:
            return object.__getattribute__(self, key)

    def __setattr__(self, key, value):
        if key=="dirty":
            if value==False:
                self.document = None
            else:
                self.document = self.newDocument(None)
        else:
            self.__dict__[key] = value


    def getOrCreateDbId(self):
        dbId = self.getData("dbId")
        if dbId is None:
            dbId = MemStore.nextDbId()
            self.setData("dbId", dbId)
        return dbId



    def getData(self, name):
        if self.document is None:
            return None
        else:
            return self.document.get(name, None)

    def setData (self, name, data):
        if self.document is None:
            self.document = self.newDocument(None)
        self.document[name] = data


    def newDocument(self, dbId):
        doc = dict()
        if self.categories is not None:
            doc["category"] = self.categories
        doc["dbId"] = dbId if dbId is not None else MemStore.nextDbId()
        return doc

    def matches(self, predicate):
        if predicate is None:
            return True
        else:
            return predicate.matches(self.document)


class QueryInterpreter(object):

    def __init__(self, context):
        self.context = context


    def buildFetchOneQuery(self, typ, predicate):
        q = Query()
        self.verifyType(q, typ)
        if predicate is not None:
            predicate.interpretQuery(self.context, q)
        if typ is not None and predicate is not None:
            q.And()
        return q



    def buildFetchManyQuery(self, typ, start, end, predicate, orderBy):
        q = Query()
        self.verifyType(q, typ)
        q.start = self.interpretLimit(self.context, start)
        q.end = self.interpretLimit(self.context, end)
        if predicate is not None:
            predicate.interpretQuery(self.context, q)
        if typ is not None and predicate is not None:
            q.And()
        if orderBy is not None:
            orderBy.interpretQuery(self.context, q)
        return q


    def verifyType(self, q, typ):
        if typ is not None:
            info = AttributeInfo("category", TypeFamily.TEXT, True, None)
            q.verify(info, MatchOp.CONTAINS, typ.typeName)


    def interpretLimit(self, context, exp):
        if exp is None:
            return None
        value = exp.interpret(context).getStorableData()
        if not isinstance(value, (int, long)):
            raise InvalidDataError("Expecting an Integer, got:" + value.type.typeName)
        return value
