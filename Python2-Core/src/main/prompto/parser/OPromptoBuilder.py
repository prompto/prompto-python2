from prompto.argument.CategoryArgument import CategoryArgument
from prompto.argument.CodeArgument import CodeArgument
from prompto.argument.ExtendedArgument import ExtendedArgument
from prompto.argument.UnresolvedArgument import UnresolvedArgument
from prompto.constraint.MatchingCollectionConstraint import MatchingCollectionConstraint
from prompto.constraint.MatchingExpressionConstraint import MatchingExpressionConstraint
from prompto.constraint.MatchingPatternConstraint import MatchingPatternConstraint
from prompto.csharp.CSharpBooleanLiteral import CSharpBooleanLiteral
from prompto.csharp.CSharpCharacterLiteral import CSharpCharacterLiteral
from prompto.csharp.CSharpDecimalLiteral import CSharpDecimalLiteral
from prompto.csharp.CSharpExpressionList import CSharpExpressionList
from prompto.csharp.CSharpIdentifierExpression import CSharpIdentifierExpression
from prompto.csharp.CSharpIntegerLiteral import CSharpIntegerLiteral
from prompto.csharp.CSharpMethodExpression import CSharpMethodExpression
from prompto.csharp.CSharpNativeCall import CSharpNativeCall
from prompto.csharp.CSharpNativeCategoryBinding import CSharpNativeCategoryBinding
from prompto.csharp.CSharpStatement import CSharpStatement
from prompto.csharp.CSharpTextLiteral import CSharpTextLiteral
from prompto.csharp.CSharpThisExpression import CSharpThisExpression
from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from prompto.declaration.DeclarationList import DeclarationList
from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
from prompto.declaration.GetterMethodDeclaration import GetterMethodDeclaration
from prompto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration
from prompto.declaration.NativeGetterMethodDeclaration import NativeGetterMethodDeclaration
from prompto.declaration.NativeMethodDeclaration import NativeMethodDeclaration
from prompto.declaration.NativeResourceDeclaration import NativeResourceDeclaration
from prompto.declaration.NativeSetterMethodDeclaration import NativeSetterMethodDeclaration
from prompto.declaration.OperatorMethodDeclaration import OperatorMethodDeclaration
from prompto.declaration.SetterMethodDeclaration import SetterMethodDeclaration
from prompto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration
from prompto.declaration.TestMethodDeclaration import TestMethodDeclaration
from prompto.expression.AddExpression import AddExpression
from prompto.expression.AndExpression import AndExpression
from prompto.expression.BlobExpression import BlobExpression
from prompto.expression.CastExpression import CastExpression
from prompto.expression.CategorySymbol import CategorySymbol
from prompto.expression.CodeExpression import CodeExpression
from prompto.expression.CompareExpression import CompareExpression
from prompto.expression.ConstructorExpression import ConstructorExpression
from prompto.expression.ContainsExpression import ContainsExpression
from prompto.expression.DivideExpression import DivideExpression
from prompto.expression.DocumentExpression import DocumentExpression
from prompto.expression.EqualsExpression import EqualsExpression
from prompto.expression.ExecuteExpression import ExecuteExpression
from prompto.expression.FetchAllExpression import FetchAllExpression
from prompto.expression.FetchExpression import FetchExpression
from prompto.expression.FetchOneExpression import FetchOneExpression
from prompto.expression.InstanceExpression import InstanceExpression
from prompto.expression.IntDivideExpression import IntDivideExpression
from prompto.expression.ItemSelector import ItemSelector
from prompto.expression.IteratorExpression import IteratorExpression
from prompto.expression.MemberSelector import MemberSelector
from prompto.expression.MethodExpression import MethodExpression
from prompto.expression.MethodSelector import MethodSelector
from prompto.expression.MinusExpression import MinusExpression
from prompto.expression.ModuloExpression import ModuloExpression
from prompto.expression.MultiplyExpression import MultiplyExpression
from prompto.expression.NativeSymbol import NativeSymbol
from prompto.expression.NotExpression import NotExpression
from prompto.expression.OrExpression import OrExpression
from prompto.expression.ParenthesisExpression import ParenthesisExpression
from prompto.expression.ReadExpression import ReadExpression
from prompto.expression.SliceSelector import SliceSelector
from prompto.expression.SortedExpression import SortedExpression
from prompto.expression.SubtractExpression import SubtractExpression
from prompto.expression.SymbolExpression import SymbolExpression
from prompto.expression.TernaryExpression import TernaryExpression
from prompto.expression.ThisExpression import ThisExpression
from prompto.expression.TypeExpression import TypeExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.grammar.ArgumentAssignment import ArgumentAssignment
from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from prompto.grammar.ArgumentList import ArgumentList
from prompto.grammar.CategorySymbolList import CategorySymbolList
from prompto.grammar.CmpOp import CmpOp
from prompto.grammar.ContOp import ContOp
from prompto.grammar.EqOp import EqOp
from prompto.grammar.IdentifierList import IdentifierList
from prompto.grammar.MethodDeclarationList import MethodDeclarationList
from prompto.grammar.NativeCategoryBindingList import NativeCategoryBindingList
from prompto.grammar.NativeSymbolList import NativeSymbolList
from prompto.grammar.Operator import Operator
from prompto.grammar.OrderByClause import OrderByClause
from prompto.grammar.OrderByClauseList import OrderByClauseList
from prompto.instance.ItemInstance import ItemInstance
from prompto.instance.MemberInstance import MemberInstance
from prompto.instance.VariableInstance import VariableInstance
from prompto.java.JavaBooleanLiteral import JavaBooleanLiteral
from prompto.java.JavaCharacterLiteral import JavaCharacterLiteral
from prompto.java.JavaDecimalLiteral import JavaDecimalLiteral
from prompto.java.JavaExpressionList import JavaExpressionList
from prompto.java.JavaIdentifierExpression import JavaIdentifierExpression
from prompto.java.JavaIntegerLiteral import JavaIntegerLiteral
from prompto.java.JavaItemExpression import JavaItemExpression
from prompto.java.JavaMethodExpression import JavaMethodExpression
from prompto.java.JavaNativeCall import JavaNativeCall
from prompto.java.JavaNativeCategoryBinding import JavaNativeCategoryBinding
from prompto.java.JavaStatement import JavaStatement
from prompto.java.JavaTextLiteral import JavaTextLiteral
from prompto.java.JavaThisExpression import JavaThisExpression
from prompto.javascript.JavaScriptBooleanLiteral import JavaScriptBooleanLiteral
from prompto.javascript.JavaScriptCharacterLiteral import JavaScriptCharacterLiteral
from prompto.javascript.JavaScriptDecimalLiteral import JavaScriptDecimalLiteral
from prompto.javascript.JavaScriptExpressionList import JavaScriptExpressionList
from prompto.javascript.JavaScriptIdentifierExpression import JavaScriptIdentifierExpression
from prompto.javascript.JavaScriptIntegerLiteral import JavaScriptIntegerLiteral
from prompto.javascript.JavaScriptMemberExpression import JavaScriptMemberExpression
from prompto.javascript.JavaScriptMethodExpression import JavaScriptMethodExpression
from prompto.javascript.JavaScriptModule import JavaScriptModule
from prompto.javascript.JavaScriptNativeCall import JavaScriptNativeCall
from prompto.javascript.JavaScriptNativeCategoryBinding import JavaScriptNativeCategoryBinding
from prompto.javascript.JavaScriptNewExpression import JavaScriptNewExpression
from prompto.javascript.JavaScriptStatement import JavaScriptStatement
from prompto.javascript.JavaScriptTextLiteral import JavaScriptTextLiteral
from prompto.javascript.JavaScriptThisExpression import JavaScriptThisExpression
from prompto.literal.BooleanLiteral import BooleanLiteral
from prompto.literal.CharacterLiteral import CharacterLiteral
from prompto.literal.DateLiteral import DateLiteral
from prompto.literal.DateTimeLiteral import DateTimeLiteral
from prompto.literal.DecimalLiteral import DecimalLiteral
from prompto.literal.DictEntry import DictEntry
from prompto.literal.DictEntryList import DictEntryList
from prompto.literal.DictLiteral import DictLiteral
from prompto.literal.HexaLiteral import HexaLiteral
from prompto.literal.IntegerLiteral import IntegerLiteral, MinIntegerLiteral, MaxIntegerLiteral
from prompto.literal.ListLiteral import ListLiteral
from prompto.literal.NullLiteral import NullLiteral
from prompto.literal.PeriodLiteral import PeriodLiteral
from prompto.literal.RangeLiteral import RangeLiteral
from prompto.literal.SetLiteral import SetLiteral
from prompto.literal.TextLiteral import TextLiteral
from prompto.literal.TimeLiteral import TimeLiteral
from prompto.literal.TupleLiteral import TupleLiteral
from prompto.parser.Dialect import Dialect
from prompto.parser.OParser import OParser
from prompto.parser.OParserListener import OParserListener
from prompto.parser.Section import Section
from prompto.python.PythonArgument import PythonNamedArgument, PythonNamedArgumentList, PythonOrdinalArgumentList
from prompto.python.PythonBooleanLiteral import PythonBooleanLiteral
from prompto.python.PythonCharacterLiteral import PythonCharacterLiteral
from prompto.python.PythonDecimalLiteral import PythonDecimalLiteral
from prompto.python.PythonIdentifierExpression import PythonIdentifierExpression
from prompto.python.PythonIntegerLiteral import PythonIntegerLiteral
from prompto.python.PythonMethodExpression import PythonMethodExpression
from prompto.python.PythonModule import PythonModule
from prompto.python.PythonNativeCall import PythonNativeCall, Python2NativeCall, Python3NativeCall
from prompto.python.PythonNativeCategoryBinding import PythonNativeCategoryBinding, Python2NativeCategoryBinding, Python3NativeCategoryBinding
from prompto.python.PythonStatement import PythonStatement
from prompto.python.PythonTextLiteral import PythonTextLiteral
from prompto.statement.AssignInstanceStatement import AssignInstanceStatement
from prompto.statement.AssignTupleStatement import AssignTupleStatement
from prompto.statement.AssignVariableStatement import AssignVariableStatement
from prompto.statement.AtomicSwitchCase import AtomicSwitchCase
from prompto.statement.CollectionSwitchCase import CollectionSwitchCase
from prompto.statement.CommentStatement import CommentStatement
from prompto.statement.DeclarationStatement import DeclarationStatement
from prompto.statement.DoWhileStatement import DoWhileStatement
from prompto.statement.ForEachStatement import ForEachStatement
from prompto.statement.IfStatement import IfElement, IfStatement, IfElementList
from prompto.statement.RaiseStatement import RaiseStatement
from prompto.statement.ReturnStatement import ReturnStatement
from prompto.statement.StatementList import StatementList
from prompto.statement.StoreStatement import StoreStatement
from prompto.statement.SwitchCase import SwitchCaseList
from prompto.statement.SwitchErrorStatement import SwitchErrorStatement
from prompto.statement.SwitchStatement import SwitchStatement
from prompto.statement.UnresolvedCall import UnresolvedCall
from prompto.statement.WhileStatement import WhileStatement
from prompto.statement.WithResourceStatement import WithResourceStatement
from prompto.statement.WithSingletonStatement import WithSingletonStatement
from prompto.statement.WriteStatement import WriteStatement
from prompto.type.AnyType import AnyType
from prompto.type.BlobType import BlobType
from prompto.type.BooleanType import BooleanType
from prompto.type.CategoryType import CategoryType
from prompto.type.CharacterType import CharacterType
from prompto.type.CodeType import CodeType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.DateType import DateType
from prompto.type.DecimalType import DecimalType
from prompto.type.DictType import DictType
from prompto.type.DocumentType import DocumentType
from prompto.type.IntegerType import IntegerType
from prompto.type.IteratorType import IteratorType
from prompto.type.ListType import ListType
from prompto.type.TextType import TextType
from prompto.type.TimeType import TimeType

# need forward declaration
OCleverParser = None

class OPromptoBuilder(OParserListener):

    def __init__(self, parser):
        self.input = parser.getTokenStream()
        self.path = parser.path
        self.nodeValues = dict()

    def getNodeValue(self, node):
        return self.nodeValues.get(node, None)

    def setNodeValue(self, node, value):
        self.nodeValues[node] = value
        if isinstance(value, Section):
            self.buildSection(node, value)

    def buildSection(self, node, section):
        first = self.findFirstValidToken(node.start.tokenIndex)
        last = self.findLastValidToken(node.stop.tokenIndex)
        section.setFrom(self.path, first, last, Dialect.O)

    def findFirstValidToken(self, idx):
        if idx == -1:  # happens because input.index() is called before any other read operation (bug?)
            idx = 0
        while idx < len(self.input.tokens):
            token = self.readValidToken(idx)
            if token is not None:
                return token
            idx += 1
        return None

    def findLastValidToken(self, idx):
        if idx == -1:  # happens because input.index() is called before any other read operation (bug?)
            idx = 0
        while idx >= 0:
            token = self.readValidToken(idx)
            if token is not None:
                return token
            idx -= 1
        return None

    def readValidToken(self, idx):
        token = self.input.tokens[idx]
        text = token.text
        if text is not None and len(text) > 0 and not text[0].isspace():
            return token
        else:
            return None


    def exitTypeIdentifier(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, UnresolvedIdentifier(name))


    def exitMethodCallExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAn_expression(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, typ)


    def exitAtomicLiteral(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCollectionLiteral(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitListLiteral(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)



    def exitBlobExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitBlob_expression(self, ctx):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, BlobExpression(exp))


    def exitBlobType(self, ctx):
        self.setNodeValue(ctx, BlobType.instance)


    def exitBooleanLiteral(self, ctx):
        self.setNodeValue(ctx, BooleanLiteral(ctx.t.text))



    def exitMinIntegerLiteral(self, ctx):
        self.setNodeValue(ctx, MinIntegerLiteral())



    def exitMaxIntegerLiteral(self, ctx):
        self.setNodeValue(ctx, MaxIntegerLiteral())



    def exitIntegerLiteral(self, ctx):
        self.setNodeValue(ctx, IntegerLiteral(ctx.t.text))



    def exitDecimalLiteral(self, ctx):
        self.setNodeValue(ctx, DecimalLiteral(ctx.t.text))



    def exitHexadecimalLiteral(self, ctx):
        self.setNodeValue(ctx, HexaLiteral(ctx.t.text))



    def exitCharacterLiteral(self, ctx):
        self.setNodeValue(ctx, CharacterLiteral(ctx.t.text))



    def exitDateLiteral(self, ctx):
        self.setNodeValue(ctx, DateLiteral(ctx.t.text))



    def exitDateTimeLiteral(self, ctx):
        self.setNodeValue(ctx, DateTimeLiteral(ctx.t.text))



    def exitTernaryExpression(self, ctx):
        condition = self.getNodeValue(ctx.test)
        ifTrue = self.getNodeValue(ctx.ifTrue)
        ifFalse = self.getNodeValue(ctx.ifFalse)
        exp = TernaryExpression(condition, ifTrue, ifFalse)
        self.setNodeValue(ctx, exp)


    def exitTest_method_declaration(self, ctx):
        name = ctx.name.text
        stmts = self.getNodeValue(ctx.stmts)
        exps = self.getNodeValue(ctx.exps)
        errorName = self.getNodeValue(ctx.error)
        error = None if errorName is None else SymbolExpression(errorName)
        self.setNodeValue(ctx, TestMethodDeclaration(name, stmts, exps, error))


    def exitTestMethod(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)



    def exitTextLiteral(self, ctx):
        self.setNodeValue(ctx, TextLiteral(ctx.t.text))



    def exitTimeLiteral(self, ctx):
        self.setNodeValue(ctx, TimeLiteral(ctx.t.text))



    def exitPeriodLiteral(self, ctx):
        self.setNodeValue(ctx, PeriodLiteral(ctx.t.text))



    def exitAttribute_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())



    def exitVariable_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())



    def exitList_literal(self, ctx):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = ListLiteral(items)
        self.setNodeValue(ctx, value)



    def exitDict_literal(self, ctx):
        items = self.getNodeValue(ctx.items)
        value = DictLiteral(items)
        self.setNodeValue(ctx, value)



    def exitTuple_literal(self, ctx):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = TupleLiteral(items)
        self.setNodeValue(ctx, value)


    def exitTupleLiteral(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitSet_literal(self, ctx):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = SetLiteral(items)
        self.setNodeValue(ctx, value)


    def exitSetLiteral(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)



    def exitRange_literal(self, ctx):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))



    def exitRangeLiteral(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)



    def exitDictLiteral(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitDictEntryList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, DictEntryList(item))



    def exitDictEntryListItem(self, ctx):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)



    def exitDict_entry(self, ctx):
        key = self.getNodeValue(ctx.key)
        value = self.getNodeValue(ctx.value)
        entry = DictEntry(key, value)
        self.setNodeValue(ctx, entry)



    def exitLiteralExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)



    def exitIdentifierExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitVariableIdentifier(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, InstanceExpression(name))



    def exitValueList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])



    def exitValueListItem(self, ctx):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)



    def exitValueTuple(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])



    def exitValueTupleItem(self, ctx):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)



    def exitSymbol_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())



    def exitNative_symbol(self, ctx):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NativeSymbol(name, exp))



    def exitSymbolIdentifier(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, SymbolExpression(name))



    def exitBooleanType(self, ctx):
        self.setNodeValue(ctx, BooleanType.instance)



    def exitCharacterType(self, ctx):
        self.setNodeValue(ctx, CharacterType.instance)



    def exitTextType(self, ctx):
        self.setNodeValue(ctx, TextType.instance)



    def exitThisExpression(self, ctx):
        self.setNodeValue(ctx, ThisExpression())



    def exitIntegerType(self, ctx):
        self.setNodeValue(ctx, IntegerType.instance)



    def exitDecimalType(self, ctx):
        self.setNodeValue(ctx, DecimalType.instance)



    def exitDateType(self, ctx):
        self.setNodeValue(ctx, DateType.instance)



    def exitDateTimeType(self, ctx):
        self.setNodeValue(ctx, DateTimeType.instance)



    def exitTimeType(self, ctx):
        self.setNodeValue(ctx, TimeType.instance)



    def exitCodeType(self, ctx):
        self.setNodeValue(ctx, CodeType.instance)


    def exitPrimaryType(self, ctx):
        typ = self.getNodeValue(ctx.p)
        self.setNodeValue(ctx, typ)


    def exitAttribute_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        typ = self.getNodeValue(ctx.typ)
        match = self.getNodeValue(getattr(ctx, "match", None))
        decl = AttributeDeclaration(name, typ, match)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)


    def exitNativeType(self, ctx):
        typ = self.getNodeValue(ctx.n)
        self.setNodeValue(ctx, typ)


    def exitCategoryType(self, ctx):
        typ = self.getNodeValue(ctx.c)
        self.setNodeValue(ctx, typ)


    def exitCategory_type(self, ctx):
        name = ctx.getText()
        self.setNodeValue(ctx, CategoryType(name))


    def exitListType(self, ctx):
        typ = self.getNodeValue(ctx.l)
        self.setNodeValue(ctx, ListType(typ))


    def exitDictType(self, ctx):
        typ = self.getNodeValue(ctx.d)
        self.setNodeValue(ctx, DictType(typ))



    def exitAttribute_identifier_list(self, ctx):
        items = IdentifierList()
        for c in ctx.attribute_identifier():
            item = self.getNodeValue(c)
            items.append(item)
        self.setNodeValue(ctx, items)



    def exitVariable_identifier_list(self, ctx):
        items = IdentifierList()
        for c in ctx.variable_identifier():
            item = self.getNodeValue(c)
            items.append(item)
        self.setNodeValue(ctx, items)



    def exitDerivedList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, IdentifierList(item))



    def exitDerivedListItem(self, ctx):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)



    def exitConcrete_category_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        derived = self.getNodeValue(ctx.derived)
        methods = self.getNodeValue(ctx.methods)
        ccd = ConcreteCategoryDeclaration(name)
        ccd.storable = ctx.STORABLE() is not None
        ccd.setAttributes(attrs)
        ccd.setDerivedFrom(derived)
        ccd.setMethods(methods)
        self.setNodeValue(ctx, ccd)



    def exitConcreteCategoryDeclaration(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)



    def exitType_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())



    def exitTypeIdentifierList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, IdentifierList(item))



    def exitTypeIdentifierListItem(self, ctx):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)



    def exitInstanceExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)



    def exitSelectableExpression(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        self.setNodeValue(ctx, parent)



    def exitSelectorExpression(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.selector)
        selector.setParent(parent)
        self.setNodeValue(ctx, selector)



    def exitMemberSelector(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberSelector(name))



    def exitIsAnExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        typ = self.getNodeValue(ctx.right)
        right = TypeExpression(typ)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.IS_A, right))



    def exitIsNotAnExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        typ = self.getNodeValue(ctx.right)
        right = TypeExpression(typ)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.IS_NOT_A, right))



    def exitIsExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.IS, right))



    def exitIsNotExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.IS_NOT, right))



    def exitItemSelector(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemSelector(exp))



    def exitSliceSelector(self, ctx):
        slice = self.getNodeValue(ctx.xslice)
        self.setNodeValue(ctx, slice)


    def exitTyped_argument(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        exp = self.getNodeValue(ctx.value)
        arg = CategoryArgument(typ, name) if attrs is None else ExtendedArgument(typ, name, attrs)
        arg.defaultExpression = exp
        self.setNodeValue(ctx, arg)


    def exitTypedArgument(self, ctx):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitNamedArgument(self, ctx):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)



    def exitCodeArgument(self, ctx):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitCategoryArgumentType(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, typ)



    def exitArgumentList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, ArgumentList(item))



    def exitArgumentListItem(self, ctx):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)



    def exitMethodTypeIdentifier(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)



    def exitMethodName(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, UnresolvedIdentifier(name))



    def exitMethodParent(self, ctx):
        name = self.getNodeValue(ctx.name)
        parent = self.getNodeValue(ctx.parent)
        self.setNodeValue(ctx, MethodSelector(name, parent))


    def exitCallableMemberSelector(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberSelector(name))

    def exitCallableItemSelector(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemSelector(exp))

    def exitCallableRoot(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)

    def exitCallableSelector(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        select = self.getNodeValue(ctx.select)
        select.setParent(parent)
        self.setNodeValue(ctx, select)

    def exitMethodVariableIdentifier(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)

    def exitMethod_call(self, ctx):
        selector = self.getNodeValue(ctx.method)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, UnresolvedCall(selector, args))

    def exitArgument_assignment(self, ctx):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = UnresolvedArgument(name)
        self.setNodeValue(ctx, ArgumentAssignment(arg, exp))

    def exitExpressionAssignmentList(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        items = ArgumentAssignmentList()
        items.insert(0, ArgumentAssignment(None, exp))
        self.setNodeValue(ctx, items)


    def exitArgumentAssignmentList(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = ArgumentAssignmentList(item=item)
        self.setNodeValue(ctx, items)


    def exitArgumentAssignmentListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitAddExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        exp = AddExpression(left, right) if ctx.op.type == OParser.PLUS else SubtractExpression(left, right)
        self.setNodeValue(ctx, exp)

    def exitNative_member_method_declaration(self, ctx):
        decl = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, decl)

    def exitNativeCategoryMethodList(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = MethodDeclarationList(item)
        self.setNodeValue(ctx, items)


    def exitNativeCategoryMethodListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitCategoryMethodList(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = MethodDeclarationList(item)
        self.setNodeValue(ctx, items)

    def exitCurlyCategoryMethodList(self, ctx):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)

    def exitCurlyStatementList(self, ctx):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)

    def exitCategoryMethodListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitSetter_method_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, SetterMethodDeclaration(name, stmts))



    def exitGetter_method_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, GetterMethodDeclaration(name, stmts))


    def exitNative_setter_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeSetterMethodDeclaration(name, stmts))



    def exitNative_getter_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeGetterMethodDeclaration(name, stmts))

    def exitMember_method_declaration(self, ctx):
        decl = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, decl)


    def exitStatementList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, StatementList(item))



    def exitStatementListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)



    def exitAbstract_method_declaration(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, AbstractMethodDeclaration(name, args, typ))



    def exitConcrete_method_declaration(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ConcreteMethodDeclaration(name, args, typ, stmts))



    def exitSingleStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, StatementList(stmt))



    def exitMethodCallStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitConstructor_expression(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        args = self.getNodeValue(ctx.args)
        if args is None:
            args = ArgumentAssignmentList()
        self.setNodeValue(ctx, ConstructorExpression(typ, args))


    def exitAssertion(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAssertionList(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = [ item ]
        self.setNodeValue(ctx, items)


    def exitAssertionListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitAssign_instance_statement(self, ctx):
        inst = self.getNodeValue(ctx.inst)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, AssignInstanceStatement(inst, exp))



    def exitAssignInstanceStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)



    def exitAssign_variable_statement(self, ctx):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, AssignVariableStatement(name, exp))

    def exitAssign_tuple_statement(self, ctx):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmt = AssignTupleStatement(items)
        stmt.setExpression(exp)
        self.setNodeValue(ctx, stmt)

    def exitRootInstance(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, VariableInstance(name))

    def exitRoughlyEqualsExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.ROUGHLY, right))

    def exitChildInstance(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)

    def exitMemberInstance(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberInstance(None, name))

    def exitItemInstance(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemInstance(None, exp))

    def exitConstructorExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitMethodExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitNativeStatementList(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = StatementList(item)
        self.setNodeValue(ctx, items)

    def exitNativeStatementListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitJava_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())

    def exitCSharpChildIdentifier(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = CSharpIdentifierExpression(parent, name)
        self.setNodeValue(ctx, child)

    def exitCsharp_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())

    def exitCsharp_method_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CSharpMethodExpression(name, args))

    def exitCSharpMethodExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitCSharpSelectorExpression(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.parent = parent
        self.setNodeValue(ctx, child)

    def exitCSharpArgumentList(self,  ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, CSharpExpressionList(item))

    def exitCSharpArgumentListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitPython_identifier(self, ctx):
        name = ctx.getText()
        self.setNodeValue(ctx, name)

    def exitPythonNamedArgumentList(self, ctx):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonNamedArgumentList(PythonNamedArgument(name, exp)))

    def exitPythonNamedArgumentListItem(self, ctx):
        items = self.getNodeValue(ctx.items)
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        items.append(PythonNamedArgument(name, exp))
        self.setNodeValue(ctx, items)

    def exitPythonNamedOnlyArgumentList(self, ctx):
        items = self.getNodeValue(ctx.named)
        self.setNodeValue(ctx, items)

    def exitPythonOrdinalArgumentList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, PythonOrdinalArgumentList(item))

    def exitPythonOrdinalArgumentListItem(self, ctx):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitPythonOrdinalOnlyArgumentList(self, ctx):
        ordinal = self.getNodeValue(ctx.ordinal)
        self.setNodeValue(ctx, ordinal)

    def exitPython_method_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, PythonMethodExpression(name, args))

    def exitPythonMethodExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitPythonGlobalMethodExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitPythonSelectorExpression(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitCSharpIdentifier(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CSharpIdentifierExpression(None, name))


    def exitPythonIdentifier(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, PythonIdentifierExpression(name))

    def exitPythonPromptoIdentifier(self, ctx):
        name = ctx.DOLLAR_IDENTIFIER().getText()
        self.setNodeValue(ctx, PythonIdentifierExpression(name))

    def exitPythonPrimaryExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonIdentifierExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitCsharp_primary_expression(self, ctx):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)

    def exitCsharp_this_expression(self, ctx):
        self.setNodeValue(ctx, CSharpThisExpression())

    def exitPythonChildIdentifier(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = PythonIdentifierExpression(name, parent)
        self.setNodeValue(ctx, child)


    def exitJavaIdentifier(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, JavaIdentifierExpression(name))


    def exitJava_primary_expression(self, ctx):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)

    def exitJavaChildIdentifier(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = JavaIdentifierExpression(name, parent=parent)
        self.setNodeValue(ctx, child)

    def exitJavaClassIdentifier(self, ctx):
        klass = self.getNodeValue(ctx.klass)
        self.setNodeValue(ctx, klass)


    def exitJavaChildClassIdentifier(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        child = JavaIdentifierExpression(parent, ctx.name.getText())
        self.setNodeValue(ctx, child)


    def exitJavaPrimaryExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitJavaSelectorExpression(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitJava_item_expression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaItemExpression(exp))


    def exitJavaItemExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp, False))

    def exitJavaReturnStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp, True))

    def exitCSharpPromptoIdentifier(self, ctx):
        name = ctx.DOLLAR_IDENTIFIER().getText()
        self.setNodeValue(ctx, CSharpIdentifierExpression(None, name))

    def exitCSharpPrimaryExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, False))


    def exitPythonStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, False))

    def exitPython_native_statement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        module = self.getNodeValue(ctx.module)
        self.setNodeValue(ctx, PythonNativeCall(stmt, module))

    def exitPython_module(self, ctx):
        ids = [c.getText() for c in ctx.identifier()]
        module = PythonModule(ids)
        self.setNodeValue(ctx, module)

    def exitCSharpReturnStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, True))


    def exitPythonReturnStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, True))


    def exitJavaNativeStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, JavaNativeCall(stmt))


    def exitCSharpNativeStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, CSharpNativeCall(stmt))


    def exitPython2NativeStatement(self, ctx):
        call = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, Python2NativeCall(call.statement, call.module))


    def exitPython3NativeStatement(self, ctx):
        call = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, Python3NativeCall(call.statement, call.module))


    def exitNative_method_declaration(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeMethodDeclaration(name, args, typ, stmts))


    def exitJavaArgumentList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, JavaExpressionList(item))



    def exitJavaArgumentListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.add(item)
        self.setNodeValue(ctx, items)



    def exitJava_method_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, JavaMethodExpression(name, args))



    def exitJavaMethodExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)



    def exitFullDeclarationList(self, ctx):
        items = self.getNodeValue(ctx.items)
        if items is None:
            items = DeclarationList()
        self.setNodeValue(ctx, items)


    def exitDeclaration(self, ctx):
        stmts = None
        if ctx.comment_statement() is not None:
            stmts = [ self.getNodeValue(ctx_) for ctx_ in ctx.comment_statement() ]
        ctx_ = ctx.attribute_declaration()
        if ctx_ is None:
            ctx_ = ctx.category_declaration()
        if ctx_ is None:
            ctx_ = ctx.enum_declaration()
        if ctx_ is None:
            ctx_ = ctx.method_declaration()
        if ctx_ is None:
            ctx_ = ctx.resource_declaration()
        decl = self.getNodeValue(ctx_)
        if decl is not None:
            decl.comments = stmts
            self.setNodeValue(ctx, decl)


    def exitDeclarationList(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = DeclarationList(item)
        self.setNodeValue(ctx, items)



    def exitDeclarationListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitNativeMethod(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)



    def exitConcreteMethod(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)



    def exitAbstractMethod(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)



    def exitJavaBooleanLiteral(self, ctx):
        self.setNodeValue(ctx, JavaBooleanLiteral(ctx.getText()))



    def exitJavaIntegerLiteral(self, ctx):
        self.setNodeValue(ctx, JavaIntegerLiteral(ctx.getText()))



    def exitJavaDecimalLiteral(self, ctx):
        self.setNodeValue(ctx, JavaDecimalLiteral(ctx.getText()))



    def exitJavaCharacterLiteral(self, ctx):
        self.setNodeValue(ctx, JavaCharacterLiteral(ctx.getText()))



    def exitJavaTextLiteral(self, ctx):
        self.setNodeValue(ctx, JavaTextLiteral(ctx.getText()))



    def exitCSharpBooleanLiteral(self, ctx):
        self.setNodeValue(ctx, CSharpBooleanLiteral(ctx.getText()))



    def exitCSharpIntegerLiteral(self, ctx):
        self.setNodeValue(ctx, CSharpIntegerLiteral(ctx.getText()))



    def exitCSharpDecimalLiteral(self, ctx):
        self.setNodeValue(ctx, CSharpDecimalLiteral(ctx.getText()))



    def exitCSharpCharacterLiteral(self, ctx):
        self.setNodeValue(ctx, CSharpCharacterLiteral(ctx.getText()))



    def exitCSharpTextLiteral(self, ctx):
        self.setNodeValue(ctx, CSharpTextLiteral(ctx.getText()))



    def exitPythonBooleanLiteral(self, ctx):
        self.setNodeValue(ctx, PythonBooleanLiteral(ctx.getText()))


    def exitPythonCharacterLiteral(self, ctx):
        self.setNodeValue(ctx, PythonCharacterLiteral(ctx.getText()))


    def exitPythonIntegerLiteral(self, ctx):
        self.setNodeValue(ctx, PythonIntegerLiteral(ctx.getText()))



    def exitPythonDecimalLiteral(self, ctx):
        self.setNodeValue(ctx, PythonDecimalLiteral(ctx.getText()))



    def exitPythonTextLiteral(self, ctx):
        self.setNodeValue(ctx, PythonTextLiteral(ctx.getText()))



    def exitJava_this_expression(self, ctx):
        self.setNodeValue(ctx, JavaThisExpression())



    def exitPythonLiteralExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaCategoryBinding(self, ctx):
        map = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, JavaNativeCategoryBinding(map))



    def exitCSharpCategoryBinding(self, ctx):
        map = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, CSharpNativeCategoryBinding(map))


    def exitPython_category_binding(self, ctx):
        id_ = ctx.id_.getText()
        module = self.getNodeValue(ctx.module)
        self.setNodeValue(ctx, PythonNativeCategoryBinding(id_, module))


    def exitPython2CategoryBinding(self, ctx):
        map = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, Python2NativeCategoryBinding(map.identifier, map.module))



    def exitPython3CategoryBinding(self, ctx):
        map = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, Python3NativeCategoryBinding(map.identifier, map.module))



    def exitNativeCategoryBindingList(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = NativeCategoryBindingList(item)
        self.setNodeValue(ctx, items)



    def exitNativeCategoryBindingListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)



    def exitNative_category_bindings(self, ctx):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitNative_category_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        decl = NativeCategoryDeclaration(name, attrs, bindings, None, methods)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)


    def exitNativeCategoryDeclaration(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitNative_resource_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        self.setNodeValue(ctx, NativeResourceDeclaration(name, attrs, bindings, None, methods))


    def exitResource_declaration(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitEnumCategoryDeclaration(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitEnumNativeDeclaration(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitParenthesis_expression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ParenthesisExpression(exp))


    def exitParenthesisExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitNativeSymbolList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, NativeSymbolList(item))


    def exitNativeSymbolListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitEnum_native_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        typ = self.getNodeValue(ctx.typ)
        symbols = self.getNodeValue(ctx.symbols)
        self.setNodeValue(ctx, EnumeratedNativeDeclaration(name, typ, symbols))


    def exitFor_each_statement(self, ctx):
        name1 = self.getNodeValue(ctx.name1)
        name2 = self.getNodeValue(ctx.name2)
        source = self.getNodeValue(ctx.source)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ForEachStatement(name1, name2, source, stmts))


    def exitForEachStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitSymbols_token(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitKey_token(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitValue_token(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitNamed_argument(self, ctx):
        name = self.getNodeValue(ctx.name)
        arg = UnresolvedArgument(name)
        exp = self.getNodeValue(ctx.value)
        arg.defaultValue = exp
        self.setNodeValue(ctx, arg)


    def exitClosureStatement(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, DeclarationStatement(decl))

    def exitReturn_statement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ReturnStatement(exp))

    def exitReturnStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)

    def exitClosureExpression(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MethodExpression(name))

    def exitIf_statement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elseIfs = self.getNodeValue(ctx.elseIfs)
        elseStmts = self.getNodeValue(ctx.elseStmts)
        stmt = IfStatement(exp, stmts)
        if elseIfs is not None:
            stmt.addAdditionals(elseIfs)
        if elseStmts is not None:
            stmt.setFinal(elseStmts)
        self.setNodeValue(ctx, stmt)


    def exitElseIfStatementList(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elem = IfElement(exp, stmts)
        self.setNodeValue(ctx, IfElementList(elem))


    def exitElseIfStatementListItem(self, ctx):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elem = IfElement(exp, stmts)
        items.add(elem)
        self.setNodeValue(ctx, items)


    def exitIfStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitSwitchStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitAssignTupleStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitRaiseStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWriteStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWithResourceStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWhileStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitDoWhileStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitTryStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitEqualsExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.EQUALS, right))


    def exitNotEqualsExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.NOT_EQUALS, right))


    def exitGreaterThanExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.GT, right))


    def exitGreaterThanOrEqualExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.GTE, right))


    def exitLessThanExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.LT, right))


    def exitLessThanOrEqualExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.LTE, right))


    def exitAtomicSwitchCase(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(exp, stmts))


    def exitCollectionSwitchCase(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))


    def exitCommentStatement(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.comment_statement()))


    def exitComment_statement(self, ctx):
        self.setNodeValue(ctx, CommentStatement(ctx.getText()))


    def exitSwitchCaseStatementList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, SwitchCaseList(item))


    def exitSwitchCaseStatementListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitSwitch_statement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        cases = self.getNodeValue(ctx.cases)
        stmts = self.getNodeValue(ctx.stmts)
        stmt = SwitchStatement(exp)
        stmt.setSwitchCases(cases)
        stmt.setDefaultCase(stmts)
        self.setNodeValue(ctx, stmt)


    def exitLiteralRangeLiteral(self, ctx):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))


    def exitLiteralSetLiteral(self, ctx):
        items = self.getNodeValue(ctx.exp)
        items = items if items is not None else []
        value = SetLiteral(items)
        self.setNodeValue(ctx, value)

    def exitLiteralListLiteral(self, ctx):
        items = self.getNodeValue(ctx.exp)
        items = items if items is not None else []
        value = ListLiteral(items)
        self.setNodeValue(ctx, value)


    def exitLiteralList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])


    def exitLiteralListItem(self, ctx):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitInExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.IN, right))


    def exitNotInExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_IN, right))


    def exitContainsAllExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS_ALL, right))


    def exitNotContainsAllExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS_ALL, right))


    def exitContainsAnyExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS_ANY, right))


    def exitNotContainsAnyExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS_ANY, right))


    def exitContainsExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS, right))


    def exitNotContainsExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS, right))


    def exitDivideExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, DivideExpression(left, right))


    def exitIntDivideExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, IntDivideExpression(left, right))


    def exitModuloExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ModuloExpression(left, right))


    def exitAndExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, AndExpression(left, right))


    def exitNullLiteral(self, ctx):
        self.setNodeValue(ctx, NullLiteral.instance)


    def exitOperatorArgument(self, ctx):
        arg = self.getNodeValue(ctx.arg)
        arg.mutable = ctx.MUTABLE() is not None
        self.setNodeValue(ctx, arg)


    def exitOperatorPlus(self, ctx):
        self.setNodeValue(ctx, Operator.PLUS)


    def exitOperatorMinus(self, ctx):
        self.setNodeValue(ctx, Operator.MINUS)


    def exitOperatorMultiply(self, ctx):
        self.setNodeValue(ctx, Operator.MULTIPLY)


    def exitOperatorDivide(self, ctx):
        self.setNodeValue(ctx, Operator.DIVIDE)


    def exitOperatorIDivide(self, ctx):
        self.setNodeValue(ctx, Operator.IDIVIDE)


    def exitOperatorModulo(self, ctx):
        self.setNodeValue(ctx, Operator.MODULO)


    def exitOperator_method_declaration(self, ctx):
        op = self.getNodeValue(ctx.op)
        arg = self.getNodeValue(ctx.arg)
        typ = self.getNodeValue(ctx.typ)
        stmts = self.getNodeValue(ctx.stmts)
        decl = OperatorMethodDeclaration(op, arg, typ, stmts)
        self.setNodeValue(ctx, decl)


    def exitOrder_by(self, ctx):
        names = IdentifierList()
        for ctx_ in ctx.variable_identifier():
            names.append(self.getNodeValue(ctx_))
        clause = OrderByClause(names, ctx.DESC() is not None)
        self.setNodeValue(ctx, clause)


    def exitOrder_by_list(self, ctx):
        list_ = OrderByClauseList()
        for ctx_ in ctx.order_by():
            list_.append(self.getNodeValue(ctx_))
        self.setNodeValue(ctx, list_)


    def exitOrExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, OrExpression(left, right))


    def exitMultiplyExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, MultiplyExpression(left, right))


    def exitMutable_category_type(self, ctx):
        typ = self.getNodeValue(ctx.category_type())
        typ.mutable = ctx.MUTABLE() is not None
        self.setNodeValue(ctx, typ)


    def exitMinusExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MinusExpression(exp))


    def exitNotExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NotExpression(exp))


    def exitWhile_statement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WhileStatement(exp, stmts))


    def exitDo_while_statement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, DoWhileStatement(exp, stmts))


    def exitSingleton_category_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        methods = self.getNodeValue(ctx.methods)
        self.setNodeValue(ctx, SingletonCategoryDeclaration(name, attrs, methods))

    def exitSingletonCategoryDeclaration(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitSliceFirstAndLast(self, ctx):
        first = self.getNodeValue(ctx.first)
        last = self.getNodeValue(ctx.last)
        self.setNodeValue(ctx, SliceSelector(first, last))


    def exitSliceFirstOnly(self, ctx):
        first = self.getNodeValue(ctx.first)
        self.setNodeValue(ctx, SliceSelector(first, None))


    def exitSliceLastOnly(self, ctx):
        last = self.getNodeValue(ctx.last)
        self.setNodeValue(ctx, SliceSelector(None, last))


    def exitStoreStatement (self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitStore_statement (self, ctx):
        to_del = self.getNodeValue(ctx.to_del)
        to_add = self.getNodeValue(ctx.to_add)
        stmt = StoreStatement(to_del, to_add)
        self.setNodeValue(ctx, stmt)


    def exitSorted_expression(self, ctx):
        source = self.getNodeValue(ctx.source)
        key = self.getNodeValue(ctx.key)
        self.setNodeValue(ctx, SortedExpression(source, key))


    def exitSortedExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitDocumentExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitDocument_expression(self, ctx):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, DocumentExpression(exp))

    def exitDocumentType(self, ctx):
        self.setNodeValue(ctx, DocumentType.instance)


    def exitFetchExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitFetchList(self, ctx):
        itemName = self.getNodeValue(ctx.name)
        source = self.getNodeValue(ctx.source)
        filter = self.getNodeValue(ctx.xfilter)
        self.setNodeValue(ctx, FetchExpression(itemName, source, filter))


    def exitFetchOne (self, ctx):
        category = self.getNodeValue(ctx.typ)
        xfilter = self.getNodeValue(ctx.xfilter)
        self.setNodeValue(ctx, FetchOneExpression(category, xfilter))


    def exitFetchAll (self, ctx):
        category = self.getNodeValue(ctx.typ)
        xfilter = self.getNodeValue(ctx.xfilter)
        start = self.getNodeValue(ctx.xstart)
        stop = self.getNodeValue(ctx.xstop)
        orderBy = self.getNodeValue(ctx.xorder)
        self.setNodeValue(ctx, FetchAllExpression(category, xfilter, start, stop, orderBy))

    def exitClosure_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MethodExpression(name))


    def exitCode_type(self, ctx):
        self.setNodeValue(ctx, CodeType.instance)


    def exitExecuteExpression(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, ExecuteExpression(name))


    def exitCodeExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CodeExpression(exp))


    def exitCode_argument(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CodeArgument(name))

    def exitCategory_symbol(self, ctx):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CategorySymbol(name, args))

    def exitCategorySymbolList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, CategorySymbolList(item))


    def exitCategorySymbolListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitEnum_category_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        parent = self.getNodeValue(ctx.derived)
        derived = None if parent is None else IdentifierList(parent)
        symbols = self.getNodeValue(ctx.symbols)
        ecd = EnumeratedCategoryDeclaration(name)
        ecd.setAttributes(attrs)
        ecd.setDerivedFrom(derived)
        ecd.setSymbols(symbols)
        self.setNodeValue(ctx, ecd)


    def exitRead_expression(self, ctx):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadExpression(source))


    def exitReadExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitWrite_statement(self, ctx):
        what = self.getNodeValue(ctx.what)
        target = self.getNodeValue(ctx.target)
        self.setNodeValue(ctx, WriteStatement(what, target))


    def exitWith_singleton_statement(self, ctx):
        name = self.getNodeValue(ctx.typ)
        typ = CategoryType(name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WithSingletonStatement(typ, stmts))


    def exitWithSingletonStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWith_resource_statement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WithResourceStatement(stmt, stmts))


    def exitAnyType(self, ctx):
        self.setNodeValue(ctx, AnyType.instance)


    def exitAnyListType(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, ListType(typ))


    def exitAnyDictType(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, DictType(typ))


    def exitAnyArgumentType(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, typ)


    def exitCastExpression(self, ctx):
        typ = self.getNodeValue(ctx.right)
        exp = self.getNodeValue(ctx.left)
        self.setNodeValue(ctx, CastExpression(exp, typ))

    def exitCatchAtomicStatement(self, ctx):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(SymbolExpression(name), stmts))


    def exitCatchCollectionStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))


    def exitCatchStatementList(self, ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, SwitchCaseList(item))


    def exitCatchStatementListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.add(item)
        self.setNodeValue(ctx, items)


    def exitTry_statement(self, ctx):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        handlers = self.getNodeValue(ctx.handlers)
        anyStmts = self.getNodeValue(ctx.anyStmts)
        finalStmts = self.getNodeValue(ctx.finalStmts)
        stmt = SwitchErrorStatement(name, stmts)
        stmt.setSwitchCases(handlers)
        stmt.setDefaultCase(anyStmts)
        stmt.setAlwaysInstructions(finalStmts)
        self.setNodeValue(ctx, stmt)


    def exitRaise_statement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, RaiseStatement(exp))


    def exitMatchingList(self, ctx):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMatchingRange(self, ctx):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMatchingExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MatchingExpressionConstraint(exp))


    def exitMatchingPattern(self, ctx):
        self.setNodeValue(ctx, MatchingPatternConstraint(TextLiteral(ctx.text.text)))


    def exitIteratorExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        name = self.getNodeValue(ctx.name)
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, IteratorExpression(name, source, exp))


    def exitIteratorType(self, ctx):
        typ = self.getNodeValue(ctx.i)
        self.setNodeValue(IteratorType(typ))


    def exitJavascriptBooleanLiteral(self, ctx):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptBooleanLiteral(text))


    def exitJavascript_category_binding(self, ctx):
        identifier = ctx.identifier().getText()
        module = self.getNodeValue(ctx.javascript_module())
        map = JavaScriptNativeCategoryBinding(identifier, module)
        self.setNodeValue(ctx, map)

    def exitJavascriptCharacterLiteral(self, ctx):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptCharacterLiteral(text))

    def exitJavascript_identifier(self, ctx):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJavascript_this_expression(self, ctx):
        self.setNodeValue(ctx, JavaScriptThisExpression())


    def exitJavascript_method_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        method = JavaScriptMethodExpression(name)
        args = self.getNodeValue(ctx.args)
        method.arguments = args
        self.setNodeValue(ctx, method)

    def exitJavascript_module(self, ctx):
        ids = []
        for ic in ctx.javascript_identifier():
            ids.append(ic.getText())
        module = JavaScriptModule(ids)
        self.setNodeValue(ctx, module)

    def exitJavascript_native_statement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        module = self.getNodeValue(ctx.module)
        stmt.module = module
        self.setNodeValue(ctx, stmt)

    def exitJavascript_new_expression(self, ctx):
        method = self.getNodeValue(ctx.javascript_method_expression())
        new = JavaScriptNewExpression(method)
        self.setNodeValue(ctx, new)

    def exitJavascriptArgumentList(self, ctx):
        exp = self.getNodeValue(ctx.item)
        list = JavaScriptExpressionList(exp)
        self.setNodeValue(ctx, list)

    def exitJavascriptArgumentListItem(self, ctx):
        exp = self.getNodeValue(ctx.item)
        list = self.getNodeValue(ctx.items)
        list.append(exp)
        self.setNodeValue(ctx, list)

    def exitJavaScriptCategoryBinding(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.binding))


    def exitJavascript_identifier_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        exp = JavaScriptIdentifierExpression(None, name)
        self.setNodeValue(ctx, exp)

    def exitJavascriptDecimalLiteral(self, ctx):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptDecimalLiteral(text))

    def exitJavascriptIntegerLiteral(self, ctx):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptIntegerLiteral(text))


    def exitJavascriptMethodExpression(self, ctx):
        method = self.getNodeValue(ctx.method)
        self.setNodeValue(ctx, method)

    def exitJavaScriptNativeStatement(self, ctx):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, JavaScriptNativeCall(stmt))

    def exitJavaScriptMethodExpression(self, ctx):
        method = self.getNodeValue(ctx.method)
        self.setNodeValue(ctx, method)

    def exitJavascriptPrimaryExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitJavascriptReturnStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, True))

    def exitJavascriptSelectorExpression(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.parent = parent
        self.setNodeValue(ctx, child)

    def exitJavaScriptMemberExpression(self, ctx):
        name = ctx.name.getText()
        self.setNodeValue(ctx, JavaScriptMemberExpression(name))

    def exitJavascript_primary_expression(self, ctx):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)

    def exitJavascriptStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, False))

    def exitJavascriptTextLiteral(self, ctx):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptTextLiteral(text))
