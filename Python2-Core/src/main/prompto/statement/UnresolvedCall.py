from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.expression.ConstructorExpression import ConstructorExpression
from prompto.expression.MethodSelector import MethodSelector
from prompto.grammar.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.runtime.Context import InstanceContext
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.statement.MethodCall import MethodCall
from prompto.type.CategoryType import CategoryType
from prompto.error.SyntaxError import SyntaxError
from prompto.utils.CodeWriter import CodeWriter

class UnresolvedCall(SimpleStatement):

    def __init__(self, caller, assignments):
        super(UnresolvedCall, self).__init__()
        self.resolved = None
        self.caller = caller
        self.assignments = assignments

    def getCaller(self):
        return self.caller

    def getAssignments(self):
        return self.assignments

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
        if self.resolved is None:
            self.resolveAndCheck(context)
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
        name = self.caller.getName()
        # if this happens in the context of a member method, then we need to check for category members first
        if isinstance(context.getParentContext(), InstanceContext):
            decl = self.resolveUnresolvedMember(context.getParentContext(), name)
            if decl is not None:
                return MethodCall(MethodSelector(name), self.assignments)
        decl = context.getRegisteredDeclaration(IDeclaration, name)
        if decl is None:
            raise SyntaxError("Unknown name:" + name)
        if isinstance(decl, CategoryDeclaration):
            return ConstructorExpression(CategoryType(name), False, self.assignments)
        else:
            return MethodCall(MethodSelector(name), self.assignments)

    def resolveUnresolvedMember(self, context, name):
        decl = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, context.instanceType.name)
        methods = decl.findMemberMethods(context, name)
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
