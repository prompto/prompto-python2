import xml.dom.minidom as minidom
from prompto.type.AnyType import AnyType
from prompto.value.TextValue import TextValue
from prompto.value.ListValue import ListValue
from prompto.value.DocumentValue import DocumentValue

def xmlRead(text, keepNamespaces, keepAttributes):
    return XMLReader(keepNamespaces, keepAttributes).read(text)


# noinspection PyUnresolvedReferences
class XMLReader(object):

    def __init__(self, keepNamespaces, keepAttributes):
        self.keepNamespaces = keepNamespaces
        self.keepAttributes = keepAttributes

    def read(self, text):
        doc = minidom.parseString(text)
        return self.convertDocument(doc)

    def convertDocument(self, doc):
        result = DocumentValue()
        self.convertElement(result, doc.documentElement)
        return result

    def convertElement(self, parent, element):
        tagName = element.tagName
        # cater for repeated elements
        if parent.hasMember(tagName):
            self.convertListElement(parent, tagName, element)
        else:
            parent.setMember(None, tagName, self.convertElementValue(element))

    def convertListElement(self, parent, tagName, element):
        list = None
        current = parent.getMemberValue(None, tagName, False)
        if isinstance(current, ListValue):
            list = current
        else:
            list = ListValue(AnyType.instance)
            list.add(current)
            parent.setMember(None, tagName, list)
        list.add(self.convertElementValue(element))

    def convertElementValue(self, element):
        hasAttributes = self.keepAttributes and element.hasAttributes()
        hasChildren = self.elementHasChildren(element)
        if hasAttributes or hasChildren:
            result = DocumentValue()
            if self.keepAttributes:
                for attr in element.attributes:
                    result.setMember(None, "@" + attr.name, TextValue(attr.value))
            if hasChildren:
                for node in element.childNodes:
                    if isinstance(node, minidom.Element):
                        self.convertElement(result, node)
            else:
                result.setMember(None, "$value", element.firstChild.nodeValue)
            return result
        else:
            return TextValue(element.firstChild.nodeValue)

    def elementHasChildren(self, element):
        return any(isinstance(node, minidom.Element) for node in element.childNodes)
