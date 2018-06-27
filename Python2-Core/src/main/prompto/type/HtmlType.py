from prompto.type.JsxType import JsxType
from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily


class HtmlType(NativeType):

    def __init__(self):
        super(HtmlType, self).__init__(TypeFamily.HTML)


    def isAssignableFrom(self, context, other):
        if other == JsxType.instance:
            return True
        else:
            return super(HtmlType, self).isAssignableFrom(context, other)

HtmlType.instance = HtmlType()