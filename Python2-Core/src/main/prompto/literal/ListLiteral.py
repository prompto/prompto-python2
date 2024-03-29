from prompto.expression.IExpression import IExpression
from prompto.literal.Literal import Literal
from prompto.type.CharacterType import CharacterType
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.type.ListType import ListType
from prompto.type.MissingType import MissingType
from prompto.type.TextType import TextType
from prompto.type.TypeMap import TypeMap
from prompto.value.DecimalValue import DecimalValue
from prompto.value.ListValue import ListValue
from prompto.value.TextValue import TextValue


class ListLiteral(Literal):

    def __init__(self, expressions=[], mutable=False):
        strs = [ str(e) for e in expressions]
        super(ListLiteral, self).__init__("[" + ", ".join(strs) + "]", ListValue(MissingType.instance, mutable=mutable))
        self.itemType = None
        self.expressions = expressions
        self.mutable = mutable


    def check(self, context):
        if self.itemType is None:
            self.itemType = self.inferElementType(context)
        return ListType(self.itemType, self.mutable)


    def inferElementType(self, context):
        if len(self.expressions) == 0:
            return MissingType.instance
        else:
            types = TypeMap()
            for exp in self.expressions:
                types.add(exp.check(context))
            return types.inferType(context)


    def interpret(self, context):
        if len(self.expressions)>0:
            self.check(context) # force computation of item type
            value = ListValue(self.itemType, mutable = self.mutable)
            for o in self.expressions:
                o = o.interpret(context)
                o = self.interpretPromotion(o)
                value.items.append(o)
            return value
        else:
            return self.value


    def interpretPromotion(self, item):
        if item is None:
            return item
        if DecimalType.instance == self.itemType and item.itype == IntegerType.instance:
            return DecimalValue(item.DecimalValue())
        elif TextType.instance == self.itemType and item.itype == CharacterType.instance:
            return TextValue(item.value)
        else:
            return item

    def toDialect(self, writer):
        if self.mutable:
            writer.append("mutable ")
        writer.append('[')
        if len(self.expressions)>0:
            for item in self.expressions:
                item.toDialect(writer)
                writer.append(", ")
            writer.trimLast(2)
        writer.append(']')

