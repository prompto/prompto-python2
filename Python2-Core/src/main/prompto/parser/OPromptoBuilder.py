from antlr4 import Token

from prompto.expression.ExplicitPredicateExpression import ExplicitPredicateExpression
from prompto.expression.PredicateExpression import PredicateExpression
from prompto.expression.ReadBlobExpression import ReadBlobExpression
from prompto.expression.SuperExpression import SuperExpression
from prompto.grammar.ThenWith import ThenWith
from prompto.javascript.JavaScriptItemExpression import JavaScriptItemExpression
from prompto.jsx.JsxFragment import JsxFragment
from prompto.literal.DocEntry import DocEntry
from prompto.literal.DocIdentifierKey import DocIdentifierKey
from prompto.literal.DocTextKey import DocTextKey
from prompto.literal.TypeLiteral import TypeLiteral
from prompto.param.CategoryParameter import CategoryParameter
from prompto.param.CodeParameter import CodeParameter
from prompto.param.ExtendedParameter import ExtendedParameter
from prompto.param.UnresolvedParameter import UnresolvedParameter
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
from prompto.css.CssCode import CssCode
from prompto.css.CssExpression import CssExpression
from prompto.css.CssField import CssField
from prompto.css.CssText import CssText
from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from prompto.declaration.ConcreteWidgetDeclaration import ConcreteWidgetDeclaration
from prompto.declaration.DeclarationList import DeclarationList
from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
from prompto.declaration.GetterMethodDeclaration import GetterMethodDeclaration
from prompto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration
from prompto.declaration.NativeGetterMethodDeclaration import NativeGetterMethodDeclaration
from prompto.declaration.NativeMethodDeclaration import NativeMethodDeclaration
from prompto.declaration.NativeResourceDeclaration import NativeResourceDeclaration
from prompto.declaration.NativeSetterMethodDeclaration import NativeSetterMethodDeclaration
from prompto.declaration.NativeWidgetDeclaration import NativeWidgetDeclaration
from prompto.declaration.OperatorMethodDeclaration import OperatorMethodDeclaration
from prompto.declaration.SetterMethodDeclaration import SetterMethodDeclaration
from prompto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration
from prompto.declaration.TestMethodDeclaration import TestMethodDeclaration
from prompto.expression.MutableExpression import MutableExpression
from prompto.expression.PlusExpression import PlusExpression
from prompto.expression.AndExpression import AndExpression
from prompto.expression.ArrowExpression import ArrowExpression
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
from prompto.expression.FetchManyExpression import FetchManyExpression
from prompto.expression.FilteredExpression import FilteredExpression
from prompto.expression.FetchOneExpression import FetchOneExpression
from prompto.expression.InstanceExpression import InstanceExpression
from prompto.expression.IntDivideExpression import IntDivideExpression
from prompto.expression.ItemSelector import ItemSelector
from prompto.expression.IteratorExpression import IteratorExpression
from prompto.expression.MemberSelector import MemberSelector
from prompto.expression.MinusExpression import MinusExpression
from prompto.expression.ModuloExpression import ModuloExpression
from prompto.expression.MultiplyExpression import MultiplyExpression
from prompto.expression.NativeSymbol import NativeSymbol
from prompto.expression.NotExpression import NotExpression
from prompto.expression.OrExpression import OrExpression
from prompto.expression.ParenthesisExpression import ParenthesisExpression
from prompto.expression.ReadAllExpression import ReadAllExpression
from prompto.expression.ReadOneExpression import ReadOneExpression
from prompto.expression.SliceSelector import SliceSelector
from prompto.expression.SortedExpression import SortedExpression
from prompto.expression.SubtractExpression import SubtractExpression
from prompto.expression.SymbolExpression import SymbolExpression
from prompto.expression.TernaryExpression import TernaryExpression
from prompto.expression.ThisExpression import ThisExpression
from prompto.expression.TypeExpression import TypeExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.expression.UnresolvedSelector import UnresolvedSelector
from prompto.grammar.Annotation import Annotation
from prompto.grammar.Argument import Argument
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
from prompto.jsx.JsxClosing import JsxClosing
from prompto.literal.BooleanLiteral import BooleanLiteral
from prompto.literal.CharacterLiteral import CharacterLiteral
from prompto.literal.DateLiteral import DateLiteral
from prompto.literal.DateTimeLiteral import DateTimeLiteral
from prompto.literal.DecimalLiteral import DecimalLiteral
from prompto.literal.DictEntry import DictEntry
from prompto.literal.DictEntryList import DictEntryList
from prompto.literal.DictIdentifierKey import DictIdentifierKey
from prompto.literal.DictLiteral import DictLiteral
from prompto.literal.DictTextKey import DictTextKey
from prompto.literal.DocEntryList import DocEntryList
from prompto.literal.DocumentLiteral import DocumentLiteral
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
from prompto.literal.UUIDLiteral import UUIDLiteral
from prompto.literal.VersionLiteral import VersionLiteral
from prompto.parser.Dialect import Dialect
from prompto.jsx.JsxSelfClosing import JsxSelfClosing
from prompto.jsx.JsxElement import JsxElement
from prompto.jsx.JsxLiteral import JsxLiteral
from prompto.jsx.JsxProperty import JsxProperty
from prompto.jsx.JsxExpression import JsxExpression
from prompto.jsx.JsxCode import JsxCode
from prompto.jsx.JsxText import JsxText
from prompto.param.ParameterList import ParameterList
from prompto.parser import ParserUtils
from prompto.parser.OLexer import OLexer
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
from prompto.python.PythonNativeCategoryBinding import PythonNativeCategoryBinding, Python2NativeCategoryBinding, \
    Python3NativeCategoryBinding
from prompto.python.PythonSelfExpression import PythonSelfExpression
from prompto.python.PythonStatement import PythonStatement
from prompto.python.PythonTextLiteral import PythonTextLiteral
from prompto.statement.AssignInstanceStatement import AssignInstanceStatement
from prompto.statement.AssignTupleStatement import AssignTupleStatement
from prompto.statement.AssignVariableStatement import AssignVariableStatement
from prompto.statement.ReadStatement import ReadStatement
from prompto.statement.RemoteCall import RemoteCall
from prompto.statement.AtomicSwitchCase import AtomicSwitchCase
from prompto.statement.BreakStatement import BreakStatement
from prompto.statement.CollectionSwitchCase import CollectionSwitchCase
from prompto.statement.CommentStatement import CommentStatement
from prompto.statement.DeclarationStatement import DeclarationStatement
from prompto.statement.DoWhileStatement import DoWhileStatement
from prompto.statement.FetchManyStatement import FetchManyStatement
from prompto.statement.FetchOneStatement import FetchOneStatement
from prompto.statement.FlushStatement import FlushStatement
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
from prompto.type.CssType import CssType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.DateType import DateType
from prompto.type.DecimalType import DecimalType
from prompto.type.DictType import DictType
from prompto.type.DocumentType import DocumentType
from prompto.type.HtmlType import HtmlType
from prompto.type.IntegerType import IntegerType
from prompto.type.IteratorType import IteratorType
from prompto.type.ListType import ListType
from prompto.type.PeriodType import PeriodType
from prompto.type.SetType import SetType
from prompto.type.TextType import TextType
from prompto.type.TimeType import TimeType

# need forward declaration
from prompto.type.UUIDType import UUIDType
from prompto.type.VersionType import VersionType


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


    def getHiddenTokensBefore(self, node):
        return self.getHiddenTokens(node, self.input.getHiddenTokensToLeft)


    def getHiddenTokensAfter(self, node):
        return self.getHiddenTokens(node, self.input.getHiddenTokensToRight)


    # noinspection PyMethodMayBeStatic
    def getHiddenTokens(self, node, fetcher):
        token = node if isinstance(node, Token) else node.symbol
        hidden = fetcher(token.tokenIndex)
        if hidden is None or len(hidden) == 0:
            return None
        return "".join([token.text for token in hidden])


    def readAnnotations(self, contexts):
        return [self.getNodeValue(ctx_) for ctx_ in contexts]


    def readComments(self, contexts):
        return [self.getNodeValue(ctx_) for ctx_ in contexts]


    def exitTypeIdentifier(self, ctx):
        name = self.getNodeValue(ctx.type_identifier())
        self.setNodeValue(ctx, UnresolvedIdentifier(name, Dialect.O))


    def exitMethod_expression(self, ctx):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitAn_expression(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, typ)


    def exitBlob_expression(self, ctx):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, BlobExpression(exp))


    def exitBlobType(self, ctx):
        self.setNodeValue(ctx, BlobType.instance)


    def exitBooleanLiteral(self, ctx):
        self.setNodeValue(ctx, BooleanLiteral(ctx.getText()))


    def exitBreakStatement(self, ctx):
        self.setNodeValue(ctx, BreakStatement())


    def exitMinIntegerLiteral(self, ctx):
        self.setNodeValue(ctx, MinIntegerLiteral())


    def exitMaxIntegerLiteral(self, ctx):
        self.setNodeValue(ctx, MaxIntegerLiteral())


    def exitIntegerLiteral(self, ctx):
        self.setNodeValue(ctx, IntegerLiteral(ctx.getText()))


    def exitDecimalLiteral(self, ctx):
        self.setNodeValue(ctx, DecimalLiteral(ctx.getText()))


    def exitHexadecimalLiteral(self, ctx):
        self.setNodeValue(ctx, HexaLiteral(ctx.getText()))


    def exitCharacterLiteral(self, ctx):
        self.setNodeValue(ctx, CharacterLiteral(ctx.getText()))


    def exitDateLiteral(self, ctx):
        self.setNodeValue(ctx, DateLiteral(ctx.getText()))


    def exitDateTimeLiteral(self, ctx):
        self.setNodeValue(ctx, DateTimeLiteral(ctx.getText()))


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


    def exitTextLiteral(self, ctx):
        self.setNodeValue(ctx, TextLiteral(ctx.getText()))


    def exitTimeLiteral(self, ctx):
        self.setNodeValue(ctx, TimeLiteral(ctx.getText()))


    def exitPeriodLiteral(self, ctx):
        self.setNodeValue(ctx, PeriodLiteral(ctx.getText()))


    def exitPeriodType(self, ctx):
        self.setNodeValue(ctx, PeriodType.instance)


    def exitVersionLiteral(self, ctx):
        self.setNodeValue(ctx, VersionLiteral(ctx.getText()))


    def exitVersionType(self, ctx):
        self.setNodeValue(ctx, VersionType.instance)


    def exitAttribute_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitVariable_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitList_literal(self, ctx):
        mutable = ctx.MUTABLE() is not None
        items = self.getNodeValue(ctx.expression_list())
        items = items if items is not None else []
        value = ListLiteral(items, mutable=mutable)
        self.setNodeValue(ctx, value)


    def exitDict_literal(self, ctx):
        mutable = ctx.MUTABLE() is not None
        items = self.getNodeValue(ctx.dict_entry_list())
        value = DictLiteral(mutable, items)
        self.setNodeValue(ctx, value)


    def exitTuple_literal(self, ctx):
        mutable = ctx.MUTABLE() is not None
        items = self.getNodeValue(ctx.expression_tuple())
        items = items if items is not None else []
        value = TupleLiteral(mutable, items)
        self.setNodeValue(ctx, value)


    def exitSet_literal(self, ctx):
        items = self.getNodeValue(ctx.expression_list())
        items = items if items is not None else []
        value = SetLiteral(items)
        self.setNodeValue(ctx, value)


    def exitRange_literal(self, ctx):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))


    def exitDict_entry(self, ctx):
        key = self.getNodeValue(ctx.key)
        value = self.getNodeValue(ctx.value)
        entry = DictEntry(key, value)
        self.setNodeValue(ctx, entry)


    def exitDict_entry_list(self, ctx):
        items = DictEntryList()
        for rule in ctx.dict_entry():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitDictKeyIdentifier(self, ctx):
        name = ctx.name.getText()
        self.setNodeValue(ctx, DictIdentifierKey(name))


    def exitDictKeyText(self, ctx):
        name = ctx.name.text
        self.setNodeValue(ctx, DictTextKey(name))


    def exitDoc_entry(self, ctx):
        key = self.getNodeValue(ctx.key)
        value = self.getNodeValue(ctx.value)
        entry = DocEntry(key, value)
        self.setNodeValue(ctx, entry)


    def exitDoc_entry_list(self, ctx):
        items = DocEntryList()
        for rule in ctx.doc_entry():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitDocKeyIdentifier(self, ctx):
        name = ctx.name.getText()
        self.setNodeValue(ctx, DocIdentifierKey(name))


    def exitDocKeyText(self, ctx):
        name = ctx.name.text
        self.setNodeValue(ctx, DocTextKey(name))


    def exitLiteral_expression(self, ctx):
        value = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, value)


    def exitLiteralExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitIdentifierExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitVariableIdentifier(self, ctx):
        name = self.getNodeValue(ctx.variable_identifier())
        self.setNodeValue(ctx, InstanceExpression(name))


    def exitSymbol_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitNative_symbol(self, ctx):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NativeSymbol(name, exp))


    def exitSymbolIdentifier(self, ctx):
        name = self.getNodeValue(ctx.symbol_identifier())
        self.setNodeValue(ctx, SymbolExpression(name))


    def exitSymbolLiteral(self, ctx):
        name = ctx.getText()
        self.setNodeValue(ctx, SymbolExpression(name))


    def exitBooleanType(self, ctx):
        self.setNodeValue(ctx, BooleanType.instance)


    def exitCharacterType(self, ctx):
        self.setNodeValue(ctx, CharacterType.instance)


    def exitTextType(self, ctx):
        self.setNodeValue(ctx, TextType.instance)


    def exitHtmlType(self, ctx):
        self.setNodeValue(ctx, HtmlType.instance)


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
        indices = None if ctx.INDEX() is None else IdentifierList()
        if ctx.indices is not None:
            indices.extend(self.getNodeValue(ctx.indices))
        decl = AttributeDeclaration(name, typ, match, indices)
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


    def exitConcrete_widget_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        derived = self.getNodeValue(ctx.derived)
        methods = self.getNodeValue(ctx.methods)
        ccd = ConcreteWidgetDeclaration(name, derived, methods)
        self.setNodeValue(ctx, ccd)


    def exitConcreteCategoryDeclaration(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitConcreteWidgetDeclaration(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitNativeWidgetDeclaration(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitType_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitType_identifier_list(self, ctx):
        items = IdentifierList()
        for rule in ctx.type_identifier():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitTypeLiteral(self, ctx):
        typ = self.getNodeValue(ctx.type_literal())
        self.setNodeValue(ctx, typ)


    def exitType_literal(self, ctx):
        typ = self.getNodeValue(ctx.category_or_any_type())
        self.setNodeValue(ctx, TypeLiteral(typ))


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


    def exitMember_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitMemberSelector(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberSelector(name))


    def exitIsAnExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        typ = self.getNodeValue(ctx.right)
        right = TypeExpression(typ)
        op = EqOp.IS_A if ctx.NOT() is None else EqOp.IS_NOT_A
        self.setNodeValue(ctx, EqualsExpression(left, op, right))


    def exitIsExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        op = EqOp.IS if ctx.NOT() is None else EqOp.IS_NOT
        self.setNodeValue(ctx, EqualsExpression(left, op, right))


    def exitItemSelector(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemSelector(exp))


    def exitSliceSelector(self, ctx):
        xslice = self.getNodeValue(ctx.xslice)
        self.setNodeValue(ctx, xslice)


    def exitTyped_argument(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        exp = self.getNodeValue(ctx.value)
        arg = CategoryParameter(typ, name) if attrs is None else ExtendedParameter(typ, name, attrs)
        arg.defaultExpression = exp
        self.setNodeValue(ctx, arg)


    def exitCodeArgument(self, ctx):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitArgument_list(self, ctx):
        items = ParameterList()
        for rule in ctx.argument():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitMethod_call_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        caller = UnresolvedIdentifier(name, Dialect.O)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, UnresolvedCall(caller, args))


    def exitMethod_call_statement(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        call = self.getNodeValue(ctx.method)
        call.setParent(parent)
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        if name is not None or stmts is not None:
            self.setNodeValue(ctx, RemoteCall(call.caller, call.arguments, name, stmts))
        else:
            self.setNodeValue(ctx, call)


    def exitMethod_declaration(self, ctx):
        value = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, value)


    def exitMethod_identifier(self, ctx):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)


    def exitArgument_assignment(self, ctx):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = UnresolvedParameter(name)
        self.setNodeValue(ctx, Argument(arg, exp))


    def exitExpressionAssignmentList(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        items = ArgumentList()
        items.insert(0, Argument(None, exp))
        self.setNodeValue(ctx, items)


    def exitArgumentAssignmentList(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = ArgumentList(items=[item])
        self.setNodeValue(ctx, items)


    def exitArgumentAssignmentListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitArrow_prefix(self, ctx):
        args = self.getNodeValue(ctx.arrow_args())
        argsSuite = self.getHiddenTokensBefore(ctx.EGT())
        arrowSuite = self.getHiddenTokensAfter(ctx.EGT())
        self.setNodeValue(ctx, ArrowExpression(args, argsSuite, arrowSuite))


    def exitArrowExpression(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitArrowExpressionBody(self, ctx):
        arrow = self.getNodeValue(ctx.arrow_prefix())
        exp = self.getNodeValue(ctx.expression())
        arrow.setExpression(exp)
        self.setNodeValue(ctx, arrow)


    def exitArrowListArg(self, ctx):
        xlist = self.getNodeValue(ctx.variable_identifier_list())
        self.setNodeValue(ctx, xlist)


    def exitArrowSingleArg(self, ctx):
        arg = self.getNodeValue(ctx.variable_identifier())
        self.setNodeValue(ctx, IdentifierList(arg))


    def exitArrowStatementsBody(self, ctx):
        arrow = self.getNodeValue(ctx.arrow_prefix())
        stmts = self.getNodeValue(ctx.statement_list())
        arrow.statements = stmts
        self.setNodeValue(ctx, arrow)


    def exitAddExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        exp = PlusExpression(left, right) if ctx.op.type == OParser.PLUS else SubtractExpression(left, right)
        self.setNodeValue(ctx, exp)


    def exitNative_member_method_declaration(self, ctx):
        comments = self.readComments(ctx.comment_statement())
        annotations = self.readAnnotations(ctx.annotation_constructor())
        ctx_ = ctx.children[ctx.getChildCount() - 1]
        decl = self.getNodeValue(ctx_)
        if decl is not None:
            decl.comments = comments
            decl.annotations = annotations
            self.setNodeValue(ctx, decl)


    def exitNative_member_method_declaration_list(self, ctx):
        items = MethodDeclarationList()
        for rule in ctx.native_member_method_declaration():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitCurlyCategoryMethodList(self, ctx):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitCurlyStatementList(self, ctx):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitMember_method_declaration_list(self, ctx):
        items = MethodDeclarationList()
        for rule in ctx.member_method_declaration():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitSetter_method_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, SetterMethodDeclaration(name, stmts))


    def exitSetType(self, ctx):
        typ = self.getNodeValue(ctx.s)
        self.setNodeValue(ctx, SetType(typ))


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
        comments = self.readComments(ctx.comment_statement())
        annotations = self.readAnnotations(ctx.annotation_constructor())
        ctx_ = ctx.children[ctx.getChildCount() - 1]
        decl = self.getNodeValue(ctx_)
        if decl is not None:
            decl.comments = comments
            decl.annotations = annotations
            self.setNodeValue(ctx, decl)


    def exitStatement_list(self, ctx):
        items = StatementList()
        for rule in ctx.statement():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitAbstract_method_declaration(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        if isinstance(typ, CategoryType):
            typ.mutable = ctx.MUTABLE() is not None
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, AbstractMethodDeclaration(name, args, typ))


    def exitConcrete_method_declaration(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        if isinstance(typ, CategoryType):
            typ.mutable = ctx.MUTABLE() is not None
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


    def exitConstructorFrom(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        copyFrom = self.getNodeValue(ctx.copyExp)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, ConstructorExpression(typ, copyFrom, args))


    def exitConstructorNoFrom(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, ConstructorExpression(typ, None, args))


    def exitCopy_from(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitAssertion(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAssertion_list(self, ctx):
        items = []
        for rule in ctx.assertion():
            item = self.getNodeValue(rule)
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
        name = self.getNodeValue(ctx.variable_identifier())
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, AssignVariableStatement(name, exp))


    def exitAssign_tuple_statement(self, ctx):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmt = AssignTupleStatement(items)
        stmt.setExpression(exp)
        self.setNodeValue(ctx, stmt)


    def exitRootInstance(self, ctx):
        name = self.getNodeValue(ctx.variable_identifier())
        self.setNodeValue(ctx, VariableInstance(name))


    def exitChildInstance(self, ctx):
        parent = self.getNodeValue(ctx.assignable_instance())
        child = self.getNodeValue(ctx.child_instance())
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitMemberInstance(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberInstance(None, name))


    def exitItemInstance(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemInstance(None, exp))


    def exitMethodExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitMethodSelector(self, ctx):
        call = self.getNodeValue(ctx.method)
        if isinstance(call.caller, UnresolvedIdentifier):
            name = call.caller.name
            call.caller = UnresolvedSelector(name)
        self.setNodeValue(ctx, call)


    def exitNative_statement_list(self, ctx):
        items = StatementList()
        for rule in ctx.native_statement():
            item = self.getNodeValue(rule)
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


    def exitCSharpArgumentList(self, ctx):
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


    def exitPythonSelfExpression(self, ctx):
        self.setNodeValue(ctx, PythonSelfExpression())


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
        stmt = self.getNodeValue(ctx.python_statement())
        module = self.getNodeValue(ctx.python_module())
        self.setNodeValue(ctx, PythonNativeCall(stmt, module))


    def exitPython_module(self, ctx):
        ids = [c.getText() for c in ctx.python_identifier()]
        module = PythonModule(ids)
        self.setNodeValue(ctx, module)


    def exitCSharpReturnStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, True))


    def exitPythonReturnStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, True))


    def exitJavaNativeStatement(self, ctx):
        stmt = self.getNodeValue(ctx.java_statement())
        self.setNodeValue(ctx, JavaNativeCall(stmt))


    def exitCSharpNativeStatement(self, ctx):
        stmt = self.getNodeValue(ctx.csharp_statement())
        self.setNodeValue(ctx, CSharpNativeCall(stmt))


    def exitPython2NativeStatement(self, ctx):
        call = self.getNodeValue(ctx.python_native_statement())
        self.setNodeValue(ctx, Python2NativeCall(call.statement, call.module))


    def exitPython3NativeStatement(self, ctx):
        call = self.getNodeValue(ctx.python_native_statement())
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
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitJava_method_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, JavaMethodExpression(name, args))


    def exitJavaMethodExpression(self, ctx):
        exp = self.getNodeValue(ctx.java_method_expression())
        self.setNodeValue(ctx, exp)


    def exitFlush_statement(self, ctx):
        self.setNodeValue(ctx, FlushStatement())


    def exitFlushStatement(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitFullDeclarationList(self, ctx):
        items = self.getNodeValue(ctx.declarations())
        if items is None:
            items = DeclarationList()
        self.setNodeValue(ctx, items)


    def exitDeclaration(self, ctx):
        comments = self.readComments(ctx.comment_statement())
        annotations = self.readAnnotations(ctx.annotation_constructor())
        ctx_ = ctx.children[ctx.getChildCount() - 1]
        decl = self.getNodeValue(ctx_)
        if decl is not None:
            decl.comments = comments
            decl.annotations = annotations
            self.setNodeValue(ctx, decl)


    def exitDeclarations(self, ctx):
        items = DeclarationList()
        for rule in ctx.declaration():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


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
        binding = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, JavaNativeCategoryBinding(binding))


    def exitCSharpCategoryBinding(self, ctx):
        binding = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, CSharpNativeCategoryBinding(binding))


    def exitPython_category_binding(self, ctx):
        id_ = ctx.identifier().getText()
        module = self.getNodeValue(ctx.python_module())
        self.setNodeValue(ctx, PythonNativeCategoryBinding(id_, module))


    def exitPython2CategoryBinding(self, ctx):
        binding = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, Python2NativeCategoryBinding(binding.identifier, binding.module))


    def exitPython3CategoryBinding(self, ctx):
        binding = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, Python3NativeCategoryBinding(binding.identifier, binding.module))


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


    def exitNative_widget_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        decl = NativeWidgetDeclaration(name, bindings, methods)
        self.setNodeValue(ctx, decl)


    def exitNativeCategoryDeclaration(self, ctx):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitNative_resource_declaration(self, ctx):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        decl = NativeResourceDeclaration(name, attrs, bindings, None, methods)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)


    def exitResource_declaration(self, ctx):
        decl = self.getNodeValue(ctx.native_resource_declaration())
        self.setNodeValue(ctx, decl)


    def exitParenthesis_expression(self, ctx):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, ParenthesisExpression(exp))


    def exitParenthesisExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitNative_symbol_list(self, ctx):
        items = NativeSymbolList()
        for rule in ctx.native_symbol():
            item = self.getNodeValue(rule)
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


    def exitUUIDType(self, ctx):
        self.setNodeValue(ctx, UUIDType.instance)


    def exitUUIDLiteral(self, ctx):
        self.setNodeValue(ctx, UUIDLiteral(ctx.getText()))


    def exitValue_token(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitNamed_argument(self, ctx):
        name = self.getNodeValue(ctx.variable_identifier())
        arg = UnresolvedParameter(name)
        exp = self.getNodeValue(ctx.literal_expression())
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


    def exitTypeExpression(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, TypeExpression(CategoryType(name)))


    def exitType_expression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


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


    def exitSuperExpression(self, ctx):
        self.setNodeValue(ctx, SuperExpression())


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
        if ctx.op.type == OLexer.EQ2:
            eqOp = EqOp.EQUALS
        elif ctx.op.type == OLexer.XEQ:
            eqOp = EqOp.NOT_EQUALS
        elif ctx.op.type == OLexer.TEQ:
            eqOp = EqOp.ROUGHLY
        else:
            raise Exception("Operator " + str(ctx.op.type))
        self.setNodeValue(ctx, EqualsExpression(left, eqOp, right))


    def exitCompareExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        if ctx.op.type == OLexer.LT:
            cmpOp = CmpOp.LT
        elif ctx.op.type == OLexer.LTE:
            cmpOp = CmpOp.LTE
        elif ctx.op.type == OLexer.GT:
            cmpOp = CmpOp.GT
        elif ctx.op.type == OLexer.GTE:
            cmpOp = CmpOp.GTE
        else:
            raise Exception("Operator " + str(ctx.op.type))
        self.setNodeValue(ctx, CompareExpression(left, cmpOp, right))


    def exitAtomicSwitchCase(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(exp, stmts))


    def exitCollection_literal(self, ctx):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)


    def exitCollectionSwitchCase(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))


    def exitCommentStatement(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.comment_statement()))


    def exitComment_statement(self, ctx):
        self.setNodeValue(ctx, CommentStatement(ctx.getText()))


    def exitCursorType(self, ctx):
        raise SyntaxError("not implemented")


    def exitSwitch_case_statement_list(self, ctx):
        items = SwitchCaseList()
        for rule in ctx.switch_case_statement():
            item = self.getNodeValue(rule)
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
        items = self.getNodeValue(ctx.literal_list_literal())
        items = items if items is not None else []
        value = SetLiteral(items)
        self.setNodeValue(ctx, value)


    def exitLiteralListLiteral(self, ctx):
        items = self.getNodeValue(ctx.literal_list_literal())
        items = items if items is not None else []
        value = ListLiteral(items)
        self.setNodeValue(ctx, value)


    def exitLiteral_list_literal(self, ctx):
        items = []
        for rule in ctx.atomic_literal():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitInExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        contOp = ContOp.IN if ctx.NOT() is None else ContOp.NOT_IN
        self.setNodeValue(ctx, ContainsExpression(left, contOp, right))


    def exitCssType(self, ctx):
        self.setNodeValue(ctx, CssType.instance)


    def exitHasExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        contOp = ContOp.HAS if ctx.NOT() is None else ContOp.NOT_HAS
        self.setNodeValue(ctx, ContainsExpression(left, contOp, right))


    def exitHasAllExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        contOp = ContOp.HAS_ALL if ctx.NOT() is None else ContOp.NOT_HAS_ALL
        self.setNodeValue(ctx, ContainsExpression(left, contOp, right))


    def exitHasAnyExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        contOp = ContOp.HAS_ANY if ctx.NOT() is None else ContOp.NOT_HAS_ANY
        self.setNodeValue(ctx, ContainsExpression(left, contOp, right))


    def exitContainsExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        eqOp = EqOp.CONTAINS if ctx.NOT() is None else EqOp.NOT_CONTAINS
        self.setNodeValue(ctx, EqualsExpression(left, eqOp, right))


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


    def exitAnnotation_constructor(self, ctx):
        name = self.getNodeValue(ctx.name)
        args = DocEntryList()
        exp = self.getNodeValue(ctx.exp)
        if exp is not None:
            args.append(DocEntry(None, exp))
        for argCtx in ctx.annotation_argument():
            arg = self.getNodeValue(argCtx)
            args.append(arg)
        self.setNodeValue(ctx, Annotation(name, args))


    def exitAnnotation_argument(self, ctx):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, DocEntry(name, exp))


    def exitAnnotation_identifier(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitAnnotation_argument_name(self, ctx):
        self.setNodeValue(ctx, ctx.getText())


    def exitAnnotationLiteralValue(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAnnotationTypeValue(self, ctx):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, TypeExpression(typ))


    def exitAndExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, AndExpression(left, right))


    def exitNullLiteral(self, ctx):
        self.setNodeValue(ctx, NullLiteral.instance)


    def exitOperator_argument(self, ctx):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)


    def exitOperatorArgument(self, ctx):
        arg = self.getNodeValue(ctx.arg)
        arg.setMutable(ctx.MUTABLE() is not None)
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


    def exitMutableInstanceExpression(self, ctx):
        source = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MutableExpression(source))


    def exitMutableSelectableExpression(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitMutableSelectorExpression(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.selector)
        selector.parent = parent
        self.setNodeValue(ctx, selector)


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


    def exitStoreStatement(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitStore_statement(self, ctx):
        to_del = self.getNodeValue(ctx.to_del)
        to_add = self.getNodeValue(ctx.to_add)
        stmts = self.getNodeValue(ctx.stmts)
        stmt = StoreStatement(to_del, to_add, stmts)
        self.setNodeValue(ctx, stmt)


    def exitSorted_expression(self, ctx):
        source = self.getNodeValue(ctx.source)
        desc = ctx.DESC() is not None
        key = self.getNodeValue(ctx.key)
        self.setNodeValue(ctx, SortedExpression(source, desc, key))


    def exitSorted_key(self, ctx):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitDocument_expression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, DocumentExpression(exp))


    def exitDocumentType(self, ctx):
        self.setNodeValue(ctx, DocumentType.instance)


    def exitDocument_literal(self, ctx):
        entries = self.getNodeValue(ctx.doc_entry_list())
        if entries is None:
            entries = DocEntryList()
        self.setNodeValue(ctx, DocumentLiteral(entries))


    def exitFetchStatement(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitFetchMany(self, ctx):
        category = self.getNodeValue(ctx.typ)
        predicate = self.getNodeValue(ctx.predicate)
        start = self.getNodeValue(ctx.xstart)
        stop = self.getNodeValue(ctx.xstop)
        orderBy = self.getNodeValue(ctx.orderby)
        self.setNodeValue(ctx, FetchManyExpression(category, predicate, start, stop, orderBy))


    def exitFetchManyAsync(self, ctx):
        category = self.getNodeValue(ctx.typ)
        predicate = self.getNodeValue(ctx.predicate)
        start = self.getNodeValue(ctx.xstart)
        stop = self.getNodeValue(ctx.xstop)
        orderBy = self.getNodeValue(ctx.orderby)
        thenWith = ThenWith.OrEmpty(self.getNodeValue(ctx.then()))
        self.setNodeValue(ctx, FetchManyStatement(category, predicate, start, stop, orderBy, thenWith))


    def exitThen(self, ctx):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ThenWith(name, stmts))


    def exitFetchOne(self, ctx):
        category = self.getNodeValue(ctx.typ)
        predicate = self.getNodeValue(ctx.predicate)
        self.setNodeValue(ctx, FetchOneExpression(category, predicate))


    def exitFetchOneAsync(self, ctx):
        category = self.getNodeValue(ctx.typ)
        predicate = self.getNodeValue(ctx.predicate)
        thenWith = ThenWith.OrEmpty(self.getNodeValue(ctx.then()))
        self.setNodeValue(ctx, FetchOneStatement(category, predicate, thenWith))


    def exitFiltered_list_expression(self, ctx):
        source = self.getNodeValue(ctx.source)
        itemName = self.getNodeValue(ctx.name)
        predicate = self.getNodeValue(ctx.predicate)
        if itemName is not None:
            expression = ExplicitPredicateExpression(itemName, predicate)
        elif isinstance(predicate, PredicateExpression):
            expression = predicate
        else:
            raise Exception("What?")
        self.setNodeValue(ctx, FilteredExpression(source, expression))


    def exitArrowFilterExpression(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.arrow_expression()))


    def exitExplicitFilterExpression(self, ctx):
        name = self.getNodeValue(ctx.variable_identifier())
        predicate = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, ExplicitPredicateExpression(name, predicate))


    def exitOtherFilterExpression(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.expression()))


    def exitCode_type(self, ctx):
        self.setNodeValue(ctx, CodeType.instance)


    def exitExecuteExpression(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, ExecuteExpression(name))


    def exitExpression_list(self, ctx):
        items = []
        for rule in ctx.expression():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitExpression_tuple(self, ctx):
        items = []
        for rule in ctx.expression():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitCodeExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CodeExpression(exp))


    def exitCode_argument(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CodeParameter(name))


    def exitCategory_or_any_type(self, ctx):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)


    def exitCategory_symbol(self, ctx):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CategorySymbol(name, args))


    def exitCategory_symbol_list(self, ctx):
        items = CategorySymbolList()
        for rule in ctx.category_symbol():
            item = self.getNodeValue(rule)
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


    def exitEnum_declaration(self, ctx):
        value = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, value)


    def exitRead_all_expression(self, ctx):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadAllExpression(source))


    def exitRead_blob_expression(self, ctx):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadBlobExpression(source))


    def exitRead_one_expression(self, ctx):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadOneExpression(source))


    def exitRead_statement(self, ctx):
        source = self.getNodeValue(ctx.source)
        thenWith = ThenWith.OrEmpty(self.getNodeValue(ctx.then()))
        self.setNodeValue(ctx, ReadStatement(source, thenWith))


    def exitReadStatement(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitWrite_statement(self, ctx):
        what = self.getNodeValue(ctx.what)
        target = self.getNodeValue(ctx.target)
        thenWith = self.getNodeValue(ctx.then())
        self.setNodeValue(ctx, WriteStatement(what, target, thenWith))


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
        typ = self.getNodeValue(ctx.any_type())
        self.setNodeValue(ctx, ListType(typ))


    def exitAnyDictType(self, ctx):
        typ = self.getNodeValue(ctx.any_type())
        self.setNodeValue(ctx, DictType(typ))


    def exitCastExpression(self, ctx):
        typ = self.getNodeValue(ctx.right)
        exp = self.getNodeValue(ctx.left)
        self.setNodeValue(ctx, CastExpression(exp, typ, ctx.MUTABLE() is not None))


    def exitCatchAtomicStatement(self, ctx):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(SymbolExpression(name), stmts))


    def exitCatchCollectionStatement(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))


    def exitCatch_statement_list(self, ctx):
        items = SwitchCaseList()
        for rule in ctx.catch_statement():
            item = self.getNodeValue(rule)
            items.append(item)
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


    def exitMatchingSet(self, ctx):
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
        self.setNodeValue(ctx, IteratorType(typ))


    def exitJavascriptBooleanLiteral(self, ctx):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptBooleanLiteral(text))


    def exitJavascript_category_binding(self, ctx):
        identifier = ".".join([cx.getText() for cx in ctx.javascript_identifier()])
        module = self.getNodeValue(ctx.javascript_module())
        xmap = JavaScriptNativeCategoryBinding(identifier, module)
        self.setNodeValue(ctx, xmap)


    def exitJavascriptCharacterLiteral(self, ctx):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptCharacterLiteral(text))


    def exitJavascript_identifier(self, ctx):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJavascript_this_expression(self, ctx):
        self.setNodeValue(ctx, JavaScriptThisExpression())


    def exitJavascript_item_expression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptItemExpression(exp))


    def exitJavaScriptItemExpression(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


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
        stmt = self.getNodeValue(ctx.javascript_statement())
        module = self.getNodeValue(ctx.javascript_module())
        stmt.module = module
        self.setNodeValue(ctx, stmt)


    def exitJavascript_new_expression(self, ctx):
        method = self.getNodeValue(ctx.javascript_method_expression())
        new = JavaScriptNewExpression(method)
        self.setNodeValue(ctx, new)


    def exitJavascriptArgumentList(self, ctx):
        exp = self.getNodeValue(ctx.item)
        xlist = JavaScriptExpressionList(exp)
        self.setNodeValue(ctx, xlist)


    def exitJavascriptArgumentListItem(self, ctx):
        exp = self.getNodeValue(ctx.item)
        xlist = self.getNodeValue(ctx.items)
        xlist.append(exp)
        self.setNodeValue(ctx, xlist)


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


    def exitJavaScriptMethodExpression(self, ctx):
        method = self.getNodeValue(ctx.method)
        self.setNodeValue(ctx, method)


    def exitJavaScriptNativeStatement(self, ctx):
        stmt = self.getNodeValue(ctx.javascript_native_statement())
        self.setNodeValue(ctx, JavaScriptNativeCall(stmt))


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


    def exitJsxChild(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.jsx))


    def exitJsxCode(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        suite = self.getHiddenTokensAfter(ctx.RCURL())
        self.setNodeValue(ctx, JsxCode(exp, suite))


    def exitJsxElement(self, ctx):
        elem = self.getNodeValue(ctx.opening)
        closing = self.getNodeValue(ctx.closing)
        elem.setClosing(closing)
        children = self.getNodeValue(ctx.children_)
        elem.setChildren(children)
        self.setNodeValue(ctx, elem)


    def exitJsxExpression(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitJsxLiteral(self, ctx):
        text = ctx.getText()
        self.setNodeValue(ctx, JsxLiteral(text))


    def exitJsxSelfClosing(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.jsx))


    def exitJsxText(self, ctx):
        text = ParserUtils.getFullText(ctx.text)
        self.setNodeValue(ctx, JsxText(text))


    def exitJsxValue(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JsxExpression(exp))


    def exitJsx_attribute(self, ctx):
        name = self.getNodeValue(ctx.name)
        value = self.getNodeValue(ctx.value)
        stop = ctx.value.stop if value is not None else ctx.name.stop
        suite = None if value is None else self.getHiddenTokensAfter(stop)
        self.setNodeValue(ctx, JsxProperty(name, value, suite))


    def exitJsx_children(self, ctx):
        expressions = [self.getNodeValue(cx) for cx in ctx.jsx_child()]
        self.setNodeValue(ctx, expressions)


    def exitJsx_closing(self, ctx):
        name = self.getNodeValue(ctx.name)
        suite = self.getHiddenTokensAfter(ctx.GT())
        self.setNodeValue(ctx, JsxClosing(name, suite))


    def exitJsx_element_name(self, ctx):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJsx_expression(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.getChild(0)))


    def exitJsx_fragment(self, ctx):
        suite = self.getHiddenTokensAfter(ctx.jsx_fragment_start().stop)
        fragment = JsxFragment(suite)
        fragment.children = self.getNodeValue(ctx.children_)
        self.setNodeValue(ctx, fragment)


    def exitJsx_identifier(self, ctx):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJsx_opening(self, ctx):
        name = self.getNodeValue(ctx.name)
        nameSuite = self.getHiddenTokensAfter(ctx.name.stop)
        attributes = [self.getNodeValue(cx) for cx in ctx.jsx_attribute()]
        openingSuite = self.getHiddenTokensAfter(ctx.GT())
        self.setNodeValue(ctx, JsxElement(name, nameSuite, attributes, openingSuite))


    def exitJsx_self_closing(self, ctx):
        name = self.getNodeValue(ctx.name)
        nameSuite = self.getHiddenTokensAfter(ctx.name.stop)
        attributes = [self.getNodeValue(cx) for cx in ctx.jsx_attribute()]
        suite = self.getHiddenTokensAfter(ctx.GT())
        self.setNodeValue(ctx, JsxSelfClosing(name, nameSuite, attributes, suite))


    def exitCssExpression(self, ctx):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitCss_expression(self, ctx):
        exp = CssExpression()
        [exp.addField(self.getNodeValue(cx)) for cx in ctx.css_field()]
        self.setNodeValue(ctx, exp)


    def exitCss_field(self, ctx):
        name = ctx.name.getText()
        value = self.getNodeValue(ctx.value)
        self.setNodeValue(ctx, CssField(name, value))


    def exitCssText(self, ctx):
        text = self.input.getText(ctx.text.start, ctx.text.stop)
        self.setNodeValue(ctx, CssText(text))


    def exitCssValue(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CssCode(exp))
