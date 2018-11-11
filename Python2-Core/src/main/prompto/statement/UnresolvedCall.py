from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.ConstructorExpression import ConstructorExpression
from prompto.expression.MethodSelector import MethodSelector
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.grammar.INamed import INamed
from prompto.statement.MethodCall import MethodCall
from prompto.statement.BaseStatement import BaseStatement
from prompto.type.CategoryType import CategoryType
from prompto.type.MethodType import MethodType
from prompto.utils.CodeWriter import CodeWriter


class UnresolvedCall(BaseStatement):

    def __init__(self, caller, assignments):
        super(UnresolvedCall, self).__init__()
        self.resolved = None
        self.caller = caller
        self.assignments = assignments


    def isSimple(self):
        return True


    def toDialect(self, writer):
        try:
            self.resolve(writer.context)
            self.resolved.toDialect(writer)
        except:
            self.caller.toDialect(writer)
            if self.assignments is not None:
                self.assignments.toDialect(writer)


    def check(self, context):
        return self.resolveAndCheck(context)


    def interpret(self, context):
        self.resolve(context)
        return self.resolved.interpret(context)


    def resolveAndCheck(self, context):
        self.resolve(context)
        return self.resolved.check(context)


    def resolve(self, context):
        if self.resolved is None:
            if isinstance(self.caller, UnresolvedIdentifier):
                self.resolved = self.resolveUnresolvedIdentifier(context)
            else:
                self.resolved = self.resolveMember(context)
        return self.resolved


    def resolveUnresolvedIdentifier(self, context):
        name = self.caller.name
        # if this happens in the context of a member method, then we need to check for category members first
        instance = context.getClosestInstanceContext()
        if instance is not None:
            decl = self.resolveUnresolvedMember(instance, name)
            if decl is not None:
                return MethodCall(MethodSelector(name), self.assignments)
        # it could be a reference to a local closure
        named = context.getRegisteredValue(INamed, name)
        if named is not None:
            itype = named.getType(context)
            if isinstance(itype, MethodType):
                call = MethodCall(MethodSelector(name), self.assignments)
                call.variableName = name
                return call
        # can only be global then
        decl = context.getRegisteredDeclaration(IDeclaration, name)
        if decl is None:
            raise SyntaxError("Unknown name:" + name)
        if isinstance(decl, CategoryDeclaration):
            return ConstructorExpression(CategoryType(name), None, self.assignments, False)
        else:
            return MethodCall(MethodSelector(name), self.assignments)


    def resolveUnresolvedMember(self, context, name):
        decl = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, context.instanceType.typeName)
        methods = decl.getMemberMethodsMap(context, name)
        if methods is not None and len(methods)>0:
            return methods
        else:
            return None


    def resolveMember(self, context):
        parent = self.caller.getParent()
        name = self.caller.getName()
        return MethodCall(MethodSelector(name, parent), self.assignments)


    def interpretAssert(self, context, testMethodDeclaration):
        self.resolve(context)
        if getattr(self.resolved, "interpretAssert", None) is not None:
            return self.resolved.interpretAssert(context, testMethodDeclaration)
        else:
            writer = CodeWriter(self.dialect, context)
            self.resolved.toDialect(writer)
            raise SyntaxError("Cannot test '" + str(writer) + "'")
