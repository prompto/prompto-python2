from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.declaration.IEnumeratedDeclaration import IEnumeratedDeclaration
from prompto.error.PromptoError import PromptoError
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.Symbol import Symbol
from prompto.grammar.Operator import Operator
from prompto.parser.Dialect import Dialect
from prompto.runtime.Score import Score
from prompto.store.DataStore import DataStore
from prompto.store.Store import IStored
from prompto.type.AnyType import AnyType
from prompto.type.MethodType import MethodType
from prompto.type.TextType import TextType
from prompto.type.BaseType import BaseType
from prompto.type.MissingType import MissingType
from prompto.type.NullType import NullType
from prompto.store.TypeFamily import TypeFamily



class CategoryType(BaseType):

    def __init__(self, name, family = TypeFamily.CATEGORY):
        super(CategoryType, self).__init__(family)
        self.typeName = name
        self.mutable = False

    def __eq__(self, obj):
        if obj is None:
            return False
        if id(obj) == id(self):
            return True
        if not isinstance(obj, CategoryType):
            return False
        return self.typeName == obj.typeName


    def toDialect(self, writer):
        if self.mutable:
            writer.append("mutable ")
        writer.append(self.typeName)


    def newInstanceFromStored(self, context, document):
        decl = self.getDeclaration(context)
        inst = decl.newInstanceFromStored(context, document)
        inst.mutable = self.mutable
        return inst

    def checkUnique(self, context):
        actual = context.getRegisteredDeclaration(IDeclaration, self.typeName)
        if actual is not None:
            raise SyntaxError("Duplicate name: \"" + self.typeName + "\"")

    def getDeclaration(self, context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
        decl = context.getRegisteredDeclaration(CategoryDeclaration, self.typeName)
        if decl is None:
            decl = context.getRegisteredDeclaration(EnumeratedNativeDeclaration, self.typeName)
        if decl is None:
            raise SyntaxError("Unknown category: \"" + self.typeName + "\"")
        return decl

    def checkMultiply(self, context, other, tryReverse):
        typ = self.checkOperator(context, other, tryReverse, Operator.MULTIPLY)
        if typ is not None:
            return typ
        else:
            return super(CategoryType, self).checkMultiply(context, other, tryReverse)


    def checkDivide(self, context, other):
        typ = self.checkOperator(context, other, False, Operator.DIVIDE)
        if typ is not None:
            return typ
        else:
            return super(CategoryType, self).checkDivide(context, other)


    def checkIntDivide(self, context, other):
        typ = self.checkOperator(context, other, False, Operator.IDIVIDE)
        if typ is not None:
            return typ
        else:
            return super(CategoryType, self).checkIntDivide(context, other)


    def checkModulo(self, context, other):
        typ = self.checkOperator(context, other, False, Operator.MODULO)
        if typ is not None:
            return typ
        else:
            return super(CategoryType, self).checkModulo(context, other)


    def checkAdd(self, context, other, tryReverse):
        typ = self.checkOperator(context, other, tryReverse, Operator.PLUS)
        if typ is not None:
            return typ
        else:
            return super(CategoryType, self).checkAdd(context, other, tryReverse)


    def checkSubstract(self, context, other):
        typ = self.checkOperator(context, other, False, Operator.MINUS)
        if typ is not None:
            return typ
        else:
            return super(CategoryType, self).checkSubstract(context, other)

    def checkOperator(self, context, other, tryReverse, operator):
        from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        actual = self.getDeclaration(context)
        if isinstance(actual, ConcreteCategoryDeclaration):
            try:
                method = actual.getOperatorMethod(self, operator, other)
                if method is None:
                    return None
                context = context.newInstanceContext(None, self)
                local = context.newChildContext()
                method.registerArguments(local)
                return method.check(local)
            except SyntaxError as e:
                # ok to pass, will try reverse
                pass
        if tryReverse:
            return None
        else:
            raise SyntaxError("Unsupported operation: " + self.typeName + " " + operator.token + " " + other.name)

    def checkExists(self, context):
        self.getDeclaration(context)

    def checkMember(self, context, name):
        dd = context.getRegisteredDeclaration(IDeclaration, self.typeName)
        if dd is None:
            raise SyntaxError("Unknown category:" + self.typeName)
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
        if isinstance(dd, EnumeratedNativeDeclaration):
            return dd.type.checkMember(context, name)
        elif isinstance(dd, CategoryDeclaration):
            if dd.hasAttribute(context, name):
                ad = context.getRegisteredDeclaration(AttributeDeclaration, name)
                if ad is None:
                    raise SyntaxError("Missing atttribute:" + name)
                else:
                    return ad.getType(context)
            elif "text" == name:
                return TextType.instance
            elif dd.hasMethod(context, name):
                method = dd.getMemberMethodsMap(context, name).getFirst()
                return MethodType(method)
            else:
                raise SyntaxError("No attribute:" + name + " in category:" + self.typeName)
        else:
            raise SyntaxError("Not a category:" + self.typeName)


    def isDerivedFrom(self, context, other):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        if not isinstance(other, CategoryType):
            return False
        try:
            thisDecl = self.getDeclaration(context)
            if isinstance(thisDecl, CategoryDeclaration):
                if thisDecl.derivedFrom is None:
                    return False
                for derived in thisDecl.derivedFrom:
                    cat = CategoryType(derived)
                    if cat==other or cat.isDerivedFrom(context, other):
                        return True
        except:
            return False
        return False



    def isAssignableFrom(self, context, other):
        return super(CategoryType, self).isAssignableFrom(context, other) or \
            (isinstance(other, CategoryType) and self.isAssignableFromCategory(context, other))



    def isAssignableFromCategory(self, context, other):
        return "Any" == self.typeName or \
               other.isDerivedFrom(context, self) or \
               other.isDerivedFromAnonymous(context, self)


    def isAnonymous(self):
        return self.typeName[0:1].islower()  # since it's the name of the argument


    def isDerivedFromAnonymous(self, context, other):
        if not other.isAnonymous():
            return False
        try:
            from prompto.declaration.CategoryDeclaration import CategoryDeclaration
            thisDecl = self.getDeclaration(context)
            if isinstance(thisDecl, CategoryDeclaration):
                otherDecl = other.getDeclaration(context)
                if isinstance(otherDecl, CategoryDeclaration):
                    # an anonymous category extends 1 and only 1 category
                    baseName = otherDecl.derivedFrom[0]
                    # check we derive from root category ( if not extending 'any')
                    if not "any" == baseName and not thisDecl.isDerivedFrom(context, CategoryType(baseName)):
                        return False
                    for attribute in otherDecl.getAllAttributes(context):
                        if not thisDecl.hasAttribute(context, attribute):
                            return False
                    return True
        except:
            return False



    def isMoreSpecificThan(self, context, other):
        if isinstance(other, (NullType, AnyType, MissingType)):
            return True
        if not isinstance(other, CategoryType):
            return False
        if other.isAnonymous():
            return True
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        selfDecl = context.getRegisteredDeclaration(CategoryDeclaration, self.typeName)
        if selfDecl.isDerivedFrom(context, other):
            return True
        return False



    def scoreMostSpecific(self, context, t1, t2):
        if t1 == t2:
            return Score.SIMILAR
        if self == t1:
            return Score.BETTER
        if self == t2:
            return Score.WORSE
        # since self derives from both t1 and t2, return the most specific of t1 and t2
        if t1.isMoreSpecificThan(context, t2):
            return Score.BETTER
        if t2.isMoreSpecificThan(context, t1):
            return Score.WORSE
        return Score.SIMILAR  # should never happen

    def newInstance(self, context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        decl = context.getRegisteredDeclaration(CategoryDeclaration, self.typeName)
        return decl.newInstance(context)

    def sort(self, context, source, desc, key=None):
        if key is None:
            from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
            key = UnresolvedIdentifier("key", Dialect.O)
        decl = self.getDeclaration(context)
        if decl.hasAttribute(context, str(key)):
            return self.sortByAttribute(context, source, desc, str(key))
        elif decl.hasMethod(context, str(key)):
            return self.sortByClassMethod(context, source, desc, str(key))
        elif self.globalMethodExists(context, source, str(key)):
            return self.sortByGlobalMethod(context, source, desc, str(key))
        else:
            return self.sortByExpression(context, source, desc, key)

    def sortByExpression(self, context, source, desc, exp):

        def compare(o1, o2):
            co = context.newInstanceContext(o1, None)
            key1 = exp.interpret(co)
            co = context.newInstanceContext(o2, None)
            key2 = exp.interpret(co)
            return self.compareKeys(key1, key2)

        return sorted(source, cmp=compare, reverse=desc)

    def sortByAttribute(self, context, source, desc, name):

        def compare(o1, o2):
            key1 = o1.getMemberValue(context, name)
            key2 = o2.getMemberValue(context, name)
            return self.compareKeys(key1, key2)

        return sorted(source, cmp=compare, reverse=desc)

    def sortByClassMethod(self, context, source, name):
        return None

    def globalMethodExists(self, context, source, name):
        from prompto.statement.MethodCall import MethodCall
        from prompto.runtime.MethodFinder import MethodFinder
        try:
            from prompto.value.ExpressionValue import ExpressionValue
            from prompto.grammar.ArgumentAssignment import ArgumentAssignment
            from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
            from prompto.expression.MethodSelector import MethodSelector
            exp = ExpressionValue(self, self.newInstance(context))
            arg = ArgumentAssignment(None, exp)
            args = ArgumentAssignmentList(items=[arg])
            proto = MethodCall(MethodSelector(name), args)
            finder = MethodFinder(context, proto)
            return finder.findMethod(True) is not None
        except PromptoError:
            return False


    def sortByGlobalMethod(self, context, source, desc, name):
        from prompto.statement.MethodCall import MethodCall
        from prompto.runtime.MethodFinder import MethodFinder
        from prompto.value.ExpressionValue import ExpressionValue
        from prompto.grammar.ArgumentAssignment import ArgumentAssignment
        from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
        from prompto.expression.MethodSelector import MethodSelector
        exp = ExpressionValue(self, self.newInstance(context))
        arg = ArgumentAssignment(None, exp)
        args = ArgumentAssignmentList(items=[arg])
        proto = MethodCall(MethodSelector(name), args)
        finder = MethodFinder(context, proto)
        method = finder.findMethod(True)
        return self.doSortByGlobalMethod(context, source, desc, proto, method)



    def doSortByGlobalMethod(self, context, source, desc, method, declaration):
        from prompto.value.ExpressionValue import ExpressionValue

        def compare(o1, o2):
            assignment = method.getAssignments()[0]
            assignment.setExpression(ExpressionValue(self, o1))
            key1 = method.interpret(context)
            assignment.setExpression(ExpressionValue(self, o2))
            key2 = method.interpret(context)
            return self.compareKeys(key1, key2)

        return sorted(source, cmp=compare, reverse=desc)


    def compareKeys(self, key1, key2):
        if key1 is None and key2 is None:
            return 0
        elif key1 is None:
            return -1
        elif key2 is None:
            return 1
        else:
            return cmp(key1,key2)


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        decl = self.getDeclaration(context)
        if decl is None:
            return super(CategoryType, self).convertPythonValueToPromptoValue(context, value, returnType)
        if isinstance(decl, IEnumeratedDeclaration):
            return self.loadEnumValue(context, decl, value)
        if DataStore.instance.isDbIdType(type(value)):
            value = DataStore.instance.fetchUnique(value)
        if isinstance(value, IStored):
            return decl.newInstanceFromStored(context, value)
        else:
            return super(CategoryType, self).convertPythonValueToPromptoValue(context, value, returnType)


    def loadEnumValue(self, context, decl, name):
        return context.getRegisteredValue( Symbol, name)


    def getMemberMethods(self, context, name):
        from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        cd = self.getDeclaration(context)
        if not isinstance(cd, ConcreteCategoryDeclaration):
            raise SyntaxError("Unknown category:" + self.typeName)
        else:
            return cd.getMemberMethodsMap(context, name).values()
