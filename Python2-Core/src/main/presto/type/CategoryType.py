from presto.runtime.Score import Score
from presto.type.BaseType import BaseType
from presto.error.SyntaxError import SyntaxError
from presto.error.PrestoError import PrestoError
from presto.declaration.IDeclaration import IDeclaration
from presto.declaration.AttributeDeclaration import AttributeDeclaration
from presto.grammar.Operator import Operator

class CategoryType(BaseType):

    def __init__(self, name):
        super(CategoryType, self).__init__(name)

    def __eq__(self, obj):
        if obj == None:
            return False
        if id(obj) == id(self):
            return True
        if not isinstance(obj, CategoryType):
            return False
        return self.getName() == obj.getName()

    def checkUnique(self, context):
        actual = context.getRegisteredDeclaration(IDeclaration, self.name)
        if actual is not None:
            raise SyntaxError("Duplicate name: \"" + self.name + "\"")

    def getDeclaration(self, context):
        from presto.declaration.CategoryDeclaration import CategoryDeclaration
        actual = context.getRegisteredDeclaration(CategoryDeclaration, self.name)
        if actual is None:
            raise SyntaxError("Unknown category: \"" + self.name + "\"")
        return actual

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
        from presto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        actual = self.getDeclaration(context)
        if isinstance(actual, ConcreteCategoryDeclaration):
            try:
                method = actual.findOperator(self, operator, other)
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
            raise SyntaxError("Unsupported operation: " + self.name + " " + operator.token + " " + other.name)

    def checkExists(self, context):
        self.getDeclaration(context)

    def checkMember(self, context, name):
        from presto.declaration.CategoryDeclaration import CategoryDeclaration
        cd = context.getRegisteredDeclaration(CategoryDeclaration, self.getName())
        if cd is None:
            raise SyntaxError("Unknown category:" + self.getName())
        if not cd.hasAttribute(context, name):
            raise SyntaxError("No attribute:" + name + " in category:" + self.getName())
        ad = context.getRegisteredDeclaration(AttributeDeclaration, name)
        if ad is None:
            raise SyntaxError("Unknown atttribute:" + name)
        return ad.getType(context)

    def isAssignableTo(self, context, other):
        if self.name == other.getName():
            return True
        from presto.type.AnyType import AnyType
        if isinstance(other, AnyType):
            return True
        if not isinstance(other, CategoryType):
            return False
        return self.isCategoryAssignableTo(context, other)

    def isCategoryAssignableTo(self, context, other):
        if self.name == other.getName():
            return True
        try:
            cd = self.getDeclaration(context)
            return self.isDerivedFromCompatibleCategory(context, cd, other) \
                or self.isAssignableToAnonymousCategory(context, cd, other)
        except SyntaxError:
            return False

    def isDerivedFromCompatibleCategory(self, context, decl, other):
        if decl.getDerivedFrom() is None:
            return False
        for derived in decl.getDerivedFrom():
            ct = CategoryType(derived)
            if ct.isAssignableTo(context, other):
                return True
        return False

    def isAssignableToAnonymousCategory(self, context, decl, other):
        if not other.isAnonymous():
            return False
        try:
            cd = other.getDeclaration(context)
            return self.checkAssignableToAnonymousCategory(context, decl, cd)
        except SyntaxError:
            return False

    def isAnonymous(self):
        return self.name[0:1].islower()  # since it's the name of the argument

    def checkAssignableToAnonymousCategory(self, context, decl, other):
        # an anonymous category extends 1 and only 1 category
        baseName = other.getDerivedFrom()[0]
        # check we derive from root category (if not extending 'Any')
        if not "any" == baseName and not decl.isDerivedFrom(context, CategoryType(baseName)):
            return False
        for attribute in other.getAttributes():
            if not decl.hasAttribute(context, attribute):
                return False
        return True

    def isMoreSpecificThan(self, context, other):
        if not isinstance(other, CategoryType):
            return False
        if other.isAnonymous():
            return True
        from presto.declaration.CategoryDeclaration import CategoryDeclaration
        selfDecl = context.getRegisteredDeclaration(CategoryDeclaration, self.getName())
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
        from presto.declaration.CategoryDeclaration import CategoryDeclaration
        decl = context.getRegisteredDeclaration(CategoryDeclaration, self.getName())
        return decl.newInstance()

    def sort(self, context, source, key=None):
        if key is None:
            from presto.grammar.UnresolvedIdentifier import UnresolvedIdentifier
            key = UnresolvedIdentifier("key")
        decl = self.getDeclaration(context)
        if decl.hasAttribute(context, str(key)):
            return self.sortByAttribute(context, source, str(key))
        elif decl.hasMethod(context, str(key), None):
            return self.sortByClassMethod(context, source, str(key))
        elif self.globalMethodExists(context, source, str(key)):
            return self.sortByGlobalMethod(context, source, str(key))
        else:
            return self.sortByExpression(context, source, key)

    def sortByExpression(self, context, source, exp):

        def compare(o1, o2):
            co = context.newInstanceContext(o1, None)
            key1 = exp.interpret(co)
            co = context.newInstanceContext(o2, None)
            key2 = exp.interpret(co)
            return self.compareKeys(key1, key2)

        return sorted(source, cmp=compare)

    def sortByAttribute(self, context, source, name):

        def compare(o1, o2):
            key1 = o1.GetMember(context, name)
            key2 = o2.GetMember(context, name)
            return self.compareKeys(key1, key2)

        return sorted(source, cmp=compare)

    def sortByClassMethod(self, context, source, name):
        return None

    def globalMethodExists(self, context, source, name):
        from presto.statement.MethodCall import MethodCall
        from presto.runtime.MethodFinder import MethodFinder
        try:
            from presto.value.ExpressionValue import ExpressionValue
            from presto.grammar.ArgumentAssignment import ArgumentAssignment
            from presto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
            from presto.expression.MethodSelector import MethodSelector
            exp = ExpressionValue(self, self.newInstance(context))
            arg = ArgumentAssignment(None, exp)
            args = ArgumentAssignmentList(item=arg)
            proto = MethodCall(MethodSelector(name), args)
            finder = MethodFinder(context, proto)
            return finder.findMethod(True) is not None
        except PrestoError:
            return False

    def sortByGlobalMethod(self, context, source, name):
        from presto.statement.MethodCall import MethodCall
        from presto.runtime.MethodFinder import MethodFinder
        from presto.value.ExpressionValue import ExpressionValue
        from presto.grammar.ArgumentAssignment import ArgumentAssignment
        from presto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
        from presto.expression.MethodSelector import MethodSelector
        exp = ExpressionValue(self, self.newInstance(context))
        arg = ArgumentAssignment(None, exp)
        args = ArgumentAssignmentList(item=arg)
        proto = MethodCall(MethodSelector(name), args)
        finder = MethodFinder(context, proto)
        method = finder.findMethod(True)
        return self.doSortByGlobalMethod(context, source, proto, method)

    def doSortByGlobalMethod(self, context, source, method, declaration):
        from presto.value.ExpressionValue import ExpressionValue

        def compare(o1, o2):
            assignment = method.getAssignments()[0]
            assignment.setExpression(ExpressionValue(self, o1))
            key1 = method.interpret(context)
            assignment.setExpression(ExpressionValue(self, o2))
            key2 = method.interpret(context)
            return self.compareKeys(key1, key2)

        return sorted(source, cmp=compare)

    def compareKeys(self, key1, key2):
        if key1 is None and key2 is None:
            return 0
        elif key1 is None:
            return -1
        elif key2 is None:
            return 1
        else:
            return cmp(key1,key2)
